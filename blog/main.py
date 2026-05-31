from fastapi import FastAPI, Depends, Response
from pydantic import BaseModel
from .database import engine, sessionlocal
from sqlalchemy.orm import Session
from typing import List
from . import schemas, models, hashing

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


#adding the response model that only contains the title and not the day
#response model allows us to display only the things we want to
@app.get('/all_b', response_model= List[schemas.ShowBlog])
def get_all_blogs(db:Session = Depends(get_db)):
    b = db.query(models.Blog).all()
    return b

@app.get('/{id}')
#to get those with the same id
def getin(id, db : Session = Depends(get_db)):
    b = db.query(models.Blog).filter(models.Blog.id == id).first() #to return only the fist one but if we wanted to return all we use .all()
    return b

@app.delete('/{id}')

def delete(id, db : Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return {'done'}

#update
@app.put('/{id}')
def update(id, request: schemas.Blog,db : Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).update({'title': request.title, 'day': request.day}) #or we can say .update(request)
    db.commit()
    return 'updated'

#2:08:31


@app.get('/blog/{id}', response_model = schemas.ShowBlog)
def getblog(id, response = Response, db : Session = Depends(get_db)):
    b = db.query(models.Blog).filter(models.Blog.id == id).first()
    return b









@app.post('/users', response_model = schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    hashed_password = hashing.Hash.bcrypt(request.password)

    new = models.User(
        name=request.name,
        password=hashed_password
    )

    db.add(new)
    db.commit()
    db.refresh(new)

    return new

@app.get('/users/{id}', response_model = schemas.ShowUser)
def getuser(id, response = Response, db : Session = Depends(get_db)):
    u = db.query(models.User).filter(models.User.id == id).first()
    return u

#2:26:53

@app.get('/users', response_model= List[schemas.ShowUser])
def get_all_users(db:Session = Depends(get_db)):
    u = db.query(models.User).all()
    return u