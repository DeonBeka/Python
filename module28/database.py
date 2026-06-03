import sqlite3

from fontTools.ttLib.tables.ttProgram import instructions

from challange import CV, CVCreate


def create_connection():
    """Creates a connection to the SQLite database."""
    connection = sqlite3.connect("Resume.db")
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    """Creates the movies table in the database if it doesn't exist."""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            personal_info TEXT NOT NULL,
            skills TEXT NOT NULL,
            work_exp TEXT NOT NULL,
            education TEXT NOT NULL,
            more_info TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()


create_table()

def create_CV(cv: CVCreate) -> int:

    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO resume (name, age, personal_info, skills, work_exp, education, more_info) VALUES (?, ?, ?, ?, ?, ?, ?)", (cv.name, cv.age, cv.personal_info, cv.skills, cv.work_exp, cv.education, cv.more_info))
    connection.commit()
    cv_id = cursor.lastrowid
    connection.close()
    return cv_id

def read_CV():

    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM resume")
    rows = cursor.fetchall()
    connection.close()
    resume = [
        CV(
            id=row[0],
            name=row[1],
            age=row[2],
            personal_info=row[3],
            skills=row[4],
            work_exp=row[5],
            education=row[6],
            more_info=row[7],
        )
        for row in rows
    ]
    return resume

def read_CV(resume_id: int):

    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM resume WHERE id = ?", (resume_id,))
    row = cursor.fetchone()
    connection.close()
    if row is None:
        return None
    return CV(id=row["id"], name=row["name"], age=row["age"],personal_info=row["personal_info"], skills=row["skills"], work_exp=row["work_exp"], education=row["education"], more_info=row["more_info"])

def update_CV(resume_id: int, cv: CVCreate) -> bool:

    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE resume SET name = ?, age = ?, personal_info = ?, skills = ?, work_exp = ?, education = ?, more_info = ? WHERE id = ?",
        (cv.name, cv.age, cv.personal_info, cv.skills, cv.work_exp, cv.education, cv.more_info, resume_id)
    )
    connection.commit()
    updated = cursor.rowcount
    connection.close()
    return updated > 0

def delete_CV(resume_id: int) -> bool:

    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM resume WHERE id = ?", (resume_id,))
    connection.commit()
    deleted = cursor.rowcount
    connection.close()
    return deleted > 0
