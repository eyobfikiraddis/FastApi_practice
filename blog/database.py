from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()


SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

engine = create_engine(
	SQLALCHEMY_DATABASE_URL,
	connect_args={"check_same_thread": False},
)

base = declarative_base()
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)