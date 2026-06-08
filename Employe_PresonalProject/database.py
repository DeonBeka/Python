import sqlite3


# Function to establish a connection to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('Employees.db')
    conn.row_factory = sqlite3.Row  # This allows the rows returned to behave like dictionaries
    return conn


def create_database():
    # Set up the SQLite database
    conn = sqlite3.connect('Employees.db')
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


def insert_employees(employee_dict, cursor):
    for (name), info in employee_dict.items():
        cursor.execute('''
            INSERT INTO books (name, age, department, position, salary, hire_date)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            name,
            info['link'],
        ))


def insert_data(employee_dict,):
    conn, cursor = create_database()




    insert_employees(employee_dict, cursor)

    conn.commit()
    conn.close()
