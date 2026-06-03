from fastapi import FastAPI, HTTPException
from typing import List
import database
import challange
from challange import CV, CVCreate

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Resume CRUD API"}

@app.post("/resume/", response_model=CV)
def create_CV(resume: CVCreate):
    """Creates a new movie in the database."""
    resume_id = database.create_CV(resume)
    return resume.CV(id=resume_id, **resume.dict())

@app.get("/resume/", response_model=List[CV])
def read_CV():
    """Retrieves all movies from the database."""
    return database.read_CV()

@app.get("/resume/{resume_id}", response_model=CV)
def read_CV(resume_id: int):
    """Retrieves a single movie by its ID."""
    resume = database.read_CV(resume_id)
    if resume is None:
        raise HTTPException(status_code=404, detail="Resume not found")
    return resume

@app.put("/resume/{resume_id}", response_model=CV)
def update_CV(resume_id: int, resume: CVCreate):
    """Updates an existing movie in the database."""
    updated = database.update_CV(resume_id, resume)
    if not updated:
        raise HTTPException(status_code=404, detail="Resume not found")
    return challange.CV(id=resume_id, **resume.dict())

@app.delete("/resume/{resume_id}", response_model=dict)
def delete_CV(resume_id: int):
    """Deletes a movie from the database by its ID."""
    deleted = database.delete_CV(resume_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Resume not found")
    return {"message": "Recipe deleted successfully"}

