from fastapi import FastAPI
from pydantic import BaseModel
from .database import engine
from . import schemas, models

models.Base.metadata.create_all(engine)


app = FastAPI()

# class Blog(BaseModel):
#     title: str
#     day: int

@app.post('/')
def create(request: schemas.Blog):
    return 'eyoba'