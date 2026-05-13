from sqlalchemy import Column, Integer, String
from .database import base as Base

class Blog(Base):
    __tablename__ = "blogss"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    day = Column(Integer)