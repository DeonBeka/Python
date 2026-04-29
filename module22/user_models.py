from pydantic import BaseModel, conint , constr
from typing import Optional

#class User(BaseModel):
 #   id: int
 #   name:str
  #  age: int
  #  email: str

#user = User(id=1, name="Deon",age=15,email="deon@gmail.com")

#print(user)

class User(BaseModel):
    id: int
    name:str
    age:int = 0
    email:str = "test@gmail.com"

user1 = User(id=1,name="dreni")
print(user1)