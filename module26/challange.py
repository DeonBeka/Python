from pydantic import BaseModel

class RecipeCreate(BaseModel):
    name: str
    instructions: str
    author: str

class Recipe(RecipeCreate):
    id: int