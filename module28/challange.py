from pydantic import BaseModel

class CVCreate(BaseModel):
    name: str
    age: int
    personal_info : str
    skills:str
    work_exp: str
    education: str
    more_info: str


class CV(CVCreate):
    id: int