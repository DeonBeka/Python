

from pydantic import BaseModel, FieldValidationInfo, field_validator, conint, constr, Field

class User(BaseModel):
    id:int
    name:str
    age:int

    @field_validator('age')
    def age_must_be_positive(cls,v, info: FieldValidationInfo):
        if v<= 0:
            raise ValueError('Age must be positive')
        return v

try:
    user = User(id=1, name="dren", age=-1)
except ValueError as e:
    print(e)

class Adress(BaseModel):
    id:int
    street:str = Field(min_length= 2, max_length=50)
    city:str
    @field_validator('id')
    def id_number(cls, v, info:FieldValidationInfo):
        if v <=0:
            raise ValueError("Id must be => than 1")
        return v
try:
    user1 = Adress(id=0, street="u", city="Prishtina")
except ValueError as e:
    print(e)
