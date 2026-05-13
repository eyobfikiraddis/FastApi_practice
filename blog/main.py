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

@app.get('/{id}')
#to get those with the same id
def getin(id, db : Session = Depends(get_db)):
    b = db.query(models.Blog).filter(models.Blog.id == id).first() #to return only the fist one but if we wanted to return all we use .all()
    return b

@app.delete('/{id}')

def delet(id, db : Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return {'done'}

#update
@app.put('/{id}')
def update(id, request: schemas.Blog,db : Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).update({'title': request.title, 'day': request.day}) #or we can say .update(request)
    db.commit()
    return 'updated'