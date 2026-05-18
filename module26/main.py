from fastapi import FastAPI, HTTPException
from typing import List
import database
import challange
from challange import Recipe, RecipeCreate

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Recipe CRUD API"}

@app.post("/recipes/", response_model=Recipe)
def create_recipe(recipe: RecipeCreate):
    """Creates a new movie in the database."""
    recipe_id = database.create_recipe(recipe)
    return recipe.Recipe(id=recipe_id, **recipe.dict())

@app.get("/recipes/", response_model=List[Recipe])
def read_recipe():
    """Retrieves all movies from the database."""
    return database.read_recipes()

@app.get("/recipes/{recipe_id}", response_model=Recipe)
def read_recipe(recipe_id: int):
    """Retrieves a single movie by its ID."""
    recipe = database.read_recipe(recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@app.put("/recipes/{recipe_id}", response_model=Recipe)
def update_recipe(recipe_id: int, recipe: RecipeCreate):
    """Updates an existing movie in the database."""
    updated = database.update_recipe(recipe_id, recipe)
    if not updated:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return challange.Recipe(id=recipe_id, **recipe.dict())

@app.delete("/recipes/{recipe_id}", response_model=dict)
def delete_recipe(recipe_id: int):
    """Deletes a movie from the database by its ID."""
    deleted = database.delete_recipe(recipe_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return {"message": "Recipe deleted successfully"}





