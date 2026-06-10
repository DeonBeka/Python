import sqlite3
from employees import employee, EmployeeCreate

# Function to establish a connection to the SQLite database
def create_connection():
    """Creates a connection to the SQLite database."""
    connection = sqlite3.connect("Employees.db")
    connection.row_factory = sqlite3.Row
    return connection



def create_database():
    # Set up the SQLite database
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()

    # Create a table to store book information
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR,
            age INTEGER,
            department VARCHAR,
            position VARCHAR,
            salary INTEGER,
            hire_date VARCHAR,
            
        )
    ''')
    conn.commit()
    return conn, cursor


def create_employee(employees: EmployeeCreate) -> int:
    """
    Adds a new movie to the database.

    Args:
        movie (MovieCreate): A pydantic model containing the title and director of the movie to be created.

    Returns:
        int: The ID of the newly created movie in the database.
    """
    connection = create_database()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO employees (name, age, department, position, salary, hire_date) VALUES (?, ?, ?, ?, ?, ?)", (employees.name, employees.age, employees.department, employees.position, employees.salary, employees.hire_date))
    connection.commit()
    employee_id = cursor.lastrowid
    connection.close()
    return employee_id


def read_employees():

    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    connection.close()
    employees = [
        employee(
            id=row[0],
            name=row[1],
            age=row[2],
            department=row[3],
            position=row[4],
            salary=row[5],
            hire_date=row[6],
        )
        for row in rows
    ]
    return employees


def read_employee(employee_id: int):

    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees WHERE id = ?", (employee_id,))
    row = cursor.fetchone()
    connection.close()
    if row is None:
        return None
    return employee(id=row["id"], name=row["name"], age=row["age"],department=row["department"], position=row["position"], salary=row["salary"], hire_date=row["hire_date"])


def update_employee(employee_id: int, employees: EmployeeCreate) -> bool:

    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE employees SET name = ?, age = ?, department = ?, position=?, salary=?, hire_date=?  WHERE id = ?",
        (employees.name, employees.age, employees.departament, employees.position, employees.salary, employees.hire_date, employee_id)
    )
    connection.commit()
    updated = cursor.rowcount
    connection.close()
    return updated > 0


def delete_employee(employee_id: int) -> bool:

    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM employees WHERE id = ?", (employee_id,))
    connection.commit()
    deleted = cursor.rowcount
    connection.close()
    return deleted > 0
