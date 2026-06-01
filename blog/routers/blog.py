from fastapi import APIRouter, Depends, Response, HTTPException
from .. import schemas, models, database
from blog.database import get_db
from sqlalchemy.orm import Session
from typing import List  


router = APIRouter()

@router.get('/all_blogs', response_model= List[schemas.ShowBlog], tags=['blogs'])
def all(db:Session = Depends(get_db)):
    b = db.query(models.Blog).all()
    return b


@router.post('/blogs', tags=['blogs'])
def create(request: schemas.Blog, db : Session = Depends(get_db)):
    new = models.Blog(title = request.title, day = request.day, user_id = 1)
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


@router.get('/blogs/{id}', response_model = schemas.ShowBlog, tags=['blogs'])
def get_blog(id, response: Response, db : Session = Depends(get_db)):
    b = db.query(models.Blog).filter(models.Blog.id == id).first()
    return b

@router.delete('/blogs/{id}',response_model= schemas.ShowBlog, tags=['blogs'])
def delete(id, db : Session = Depends(get_db)):
    b = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not b:
        raise HTTPException(status_code=404, detail='Blog not found')
    db.delete(b)
    db.commit()
    return b


@router.put('/edit_blogs/{id}', response_model = schemas.ShowBlog, tags=['blogs'])
def update(id, request: schemas.Blog,db : Session = Depends(get_db)):
    b = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not b:
        raise HTTPException(status_code=404, detail='Blog not found')
    b.title = request.title
    b.day = request.day
    db.commit()
    db.refresh(b)
    return b