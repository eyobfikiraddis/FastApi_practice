from pydantic import BaseModel
 







class User(BaseModel):
    name: str
    password: str



class ShowUser(BaseModel):
    name: str
    class Config():
        orm_mode = True


class Blog(BaseModel):
    title: str
    day: int
    user_id: int

class ShowBlog(BaseModel):
    title: str
    created_by: ShowUser
    class Config():
        orm_mode = True
    