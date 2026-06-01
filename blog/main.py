from fastapi import FastAPI, Depends, Response, HTTPException
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

@app.post('/blogs', tags=['blogs'])
def create(request: schemas.Blog, db : Session = Depends(get_db)):
    new = models.Blog(title = request.title, day = request.day, user_id = 1)
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


#adding the response model that only contains the title and not the day
#response model allows us to display only the things we want to
@app.get('/all_blogs', response_model= List[schemas.ShowBlog], tags=['blogs'])
def get_all_blogs(db:Session = Depends(get_db)):
    b = db.query(models.Blog).all()
    return b

@app.get('/blogs/{id}', response_model = schemas.ShowBlog, tags=['blogs'])
#to get those with the same id
def get_blog(id, response: Response, db : Session = Depends(get_db)):
    b = db.query(models.Blog).filter(models.Blog.id == id).first()
    return b
# @app.get('/blog/{id}', response_model = schemas.ShowBlog)
# def getblog(id, response = Response, db : Session = Depends(get_db)):
#     b = db.query(models.Blog).filter(models.Blog.id == id).first()
#     return b


@app.delete('/blogs/{id}',response_model= schemas.ShowBlog, tags=['blogs'])
def delete(id, db : Session = Depends(get_db)):
    b = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not b:
        raise HTTPException(status_code=404, detail='Blog not found')
    db.delete(b)
    db.commit()
    return b

#update
@app.put('/edit_blogs/{id}', response_model = schemas.ShowBlog, tags=['blogs'])
def update(id, request: schemas.Blog,db : Session = Depends(get_db)):
    b = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not b:
        raise HTTPException(status_code=404, detail='Blog not found')
    b.title = request.title
    b.day = request.day
    db.commit()
    db.refresh(b)
    return b

#2:08:31











@app.post('/users', response_model = schemas.ShowUser, tags=['users'])
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

@app.get('/users/{id}', response_model = schemas.ShowUser, tags=['users'])
def getuser(id, response: Response, db : Session = Depends(get_db)):
    u = db.query(models.User).filter(models.User.id == id).first()
    return u

#2:26:53

@app.get('/all_users', response_model= List[schemas.ShowUser], tags=['users'])
def get_all_users(db:Session = Depends(get_db)):
    u = db.query(models.User).all()
    return u