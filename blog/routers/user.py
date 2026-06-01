from fastapi import APIRouter, Depends, Response, HTTPException
from blog import hashing
from .. import schemas, models, database
from blog.database import get_db
from sqlalchemy.orm import Session
from typing import List  

router = APIRouter()


@router.post('/users', response_model = schemas.ShowUser, tags=['users'])
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


@router.get('/users/{id}', response_model = schemas.ShowUser, tags=['users'])
def getuser(id, response: Response, db : Session = Depends(get_db)):
    u = db.query(models.User).filter(models.User.id == id).first()
    return u


@router.get('/all_users', response_model= List[schemas.ShowUser], tags=['users'])
def get_all_users(db:Session = Depends(get_db)):
    u = db.query(models.User).all()
    return u