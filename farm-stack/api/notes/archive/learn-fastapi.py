from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel #, EmailStr

app = FastAPI()

class User(BaseModel):
    name: str
    age: int


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

@app.get("/v1/auth")
async def auth():
    return {"user": {"name": "Bob", "age": 30}}

@app.get("/v1/user")
async def get_user():
    return {"user": {"name": "Bob", "age": 30}}

@app.post("/v1/new")
async def new_user(new_user: User):
    print(new_user)
    print(new_user.dict())
    return {"new_user": new_user}
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