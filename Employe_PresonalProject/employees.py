from pydantic import BaseModel
from typing import List, Optional


# Base model for Book with relevant fields
class EmployeeBase(BaseModel):
    name: str
    age: int
    departament: str
    position: str  # List of genre names
    salary: int
    hire_date: Optional[int] = None


# Model for creating a new book
class EmployeeCreate(EmployeeBase):
    pass


# Model for the response of a book, which includes both id and all fields
class EmployeeResponse(EmployeeBase):
    id: int


# Model for a book with id, inheriting from BookBase
class Employee(EmployeeBase):
    id: int
