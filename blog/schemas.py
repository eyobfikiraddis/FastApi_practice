from pydantic import BaseModel
 
class Blog(BaseModel):
    title: str
    day: int

class ShowBlog(BaseModel):
    title: str
    class Config():
        orm_mode = True






class User(BaseModel):
    name: str
    password: str



class ShowUser(BaseModel):
    name: str
    class Config():
        orm_mode = True
    