from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from sqlalchemy.orm import Session
from . import models

app = FastAPI()

# Setup templates directory
templates = Jinja2Templates(directory="app/templates")

# Dependency to get database session
def get_db():
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "Homepage"}
    )

# Example database read endpoint
@app.get("/notes")
def read_notes(db: Session = Depends(get_db)):
    notes = db.query(models.Note).all()
    return notes

# Example database write endpoint
@app.post("/notes")
def create_note(content: str, db: Session = Depends(get_db)):
    note = models.Note(content=content)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note
