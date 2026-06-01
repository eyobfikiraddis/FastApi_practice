from pydantic import BaseModel
from typing import List
 


class Blog(BaseModel):
    title: str
    day: int
    # user_id: int




class User(BaseModel):
    name: str
    password: str



class ShowUser(BaseModel):
    name: str
    blogs: List[Blog] = []
    class Config():
        orm_mode = True




class ShowBlog(BaseModel):
    title: str
    created_by: ShowUser
    class Config():
        orm_mode = True
    