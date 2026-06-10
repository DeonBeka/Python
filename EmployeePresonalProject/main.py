from fastapi import FastAPI, HTTPException
from typing import List
import database
import employees
from employees import employee, EmployeeCreate

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Employee CRUD API"}

@app.post("/employees/", response_model=employee)
def create_employee(employee: EmployeeCreate):
    """Creates a new movie in the database."""
    employee_id = database.create_employee(employee)
    return employee.employee(id=employee_id, **employee.dict())

@app.get("/employees/", response_model=List[employee])
def read_employee():
    """Retrieves all movies from the database."""
    return database.read_employees()

@app.get("/employees/{employee_id}", response_model=employee)
def read_employee(employee_id: int):
    """Retrieves a single movie by its ID."""
    employee = database.read_employee(employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@app.put("/employees/{employee_id}", response_model=employee)
def update_employee(employee_id: int, employee: EmployeeCreate):
    """Updates an existing movie in the database."""
    updated = database.update_employee(employee_id, employee)
    if not updated:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employees.employee(id=employee_id, **employee.dict())

@app.delete("/employees/{employee_id}", response_model=dict)
def delete_employee(employee_id: int):

    deleted = database.delete_employee(employee_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}