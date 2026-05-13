from pydantic import BaseModel
 
class Blog(BaseModel):
    title: str
    day: int
