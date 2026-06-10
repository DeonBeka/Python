from pydantic import BaseModel
from typing import List, Optional


# Base model for Book with relevant fields
class EmployeeCreate(BaseModel):
    name: str
    age: int
    departament: str
    position: str  # List of genre names
    salary: int
    hire_date: Optional[int] = None

class employee(EmployeeCreate):
    id: int
