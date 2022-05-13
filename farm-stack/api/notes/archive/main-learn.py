from fastapi import FastAPI, Depends
from fastapi.params import Body
# from pydantic import BaseModel #, EmailStr
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.dialects.postgresql import UUID
import uuid 
import uvicorn
# from .models2 import User

# SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:KJjhdzg567fKSk97f879gJ8975GHGFkjlk@localhost:5432/fastapi"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

Base = declarative_base()
# from .database import Base



class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    user_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    api_key = Column(UUID(as_uuid=True), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

# Create SQL tables if none 
Base.metadata.create_all(bind=engine)

# class Post(Base):
#     __tablename__ = "posts"

#     id = Column(Integer, primary_key=True, nullable=False)
#     title = Column(String, nullable=False)
#     content = Column(String, nullable=False)
#     published = Column(Boolean, server_default='TRUE', nullable=False)
#     created_at = Column(TIMESTAMP(timezone=True),
#                         nullable=False, server_default=text('now()'))
#     owner_id = Column(Integer, ForeignKey(
#         "users.id", ondelete="CASCADE"), nullable=False)

#     owner = relationship("User")

# class Vote(Base):
#     __tablename__ = "votes"
#     user_id = Column(Integer, ForeignKey(
#         "users.id", ondelete="CASCADE"), primary_key=True)
#     post_id = Column(Integer, ForeignKey(
#         "posts.id", ondelete="CASCADE"), primary_key=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

description = """
FastapiAppTemplate API helps you do awesome stuff. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""
app = FastAPI(
    title="Fastapi App API Template",
    description=description,
    version="0.0.1"
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)

@app.get("/", include_in_schema=False)
async def root():
    return {
        "website": "MySite.com",
        "Docs 1": "api.MySite.com/docs",
        "Docs 2": "api.MySite.com/redoc"
    }

@app.get("/test")
async def test(db: Session = Depends(get_db)):
    
    users = db.query(User).all()
    return {"data": users}

@app.get("/v1/auth", include_in_schema=False)
async def auth():
    return {"user": {"name": "Bob", "age": 30}}

@app.get("/v1/user")
async def get_user():
    return {"name": "Bob", "age": 30}

# @app.post("/v1/new")
# async def new_user(new_user: User):
#     print(new_user)
#     print(new_user.dict())
#     return {"new_user": new_user}
# 
# @app.post("/v1/new")
# async def new_user(new_user: User):
#     print(new_user)
#     return {"new_user": F"name {new_user.name}"}
#
# @app.post("/v1/new")
# async def new_user(payLoad: dict = Body(...)):
#     print(payLoad)
#     return {"new_user": f"{payLoad['name']}"}