import sqlite3
connection = sqlite3.connect('example.db')

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    departament TEXT NOT NULL,
    salary REAL
    )

''')

connection.commit()

cursor.execute('''
INSERT INTO employees(name, position, departament, salary)
VALUES(?,?,?,?)
''',('Gerti', 'Software Engineer', 'IT', 120000))
connection.commit()
cursor.execute('Select * From employees')