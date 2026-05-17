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

# class UserOut(BaseModel):
#     id: int
#     name: str
#     class Config():
#         orm_mode = True
    