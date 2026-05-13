from fastapi import FastAPI, Depends
from pydantic import BaseModel
from .database import engine, sessionlocal
from sqlalchemy.orm import Session
from . import schemas, models

models.Base.metadata.create_all(engine)

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

# class Blog(BaseModel):
#     title: str
#     day: int

@app.post('/')
def create(request: schemas.Blog, db : Session = Depends(get_db)):
    new = models.Blog(title = request.title, day = request.day)
    db.add(new)
    db.commit()
    db.refresh(new)
    return db

@app.get('/')
def all(db:Session = Depends(get_db)):
    b = db.query(models.Blog).all()
    return b