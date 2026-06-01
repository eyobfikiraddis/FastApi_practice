from fastapi import FastAPI, Depends, Response, HTTPException
from .database import engine, sessionlocal
from sqlalchemy.orm import Session
from . import models
from .routers import blog, user

models.Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)

