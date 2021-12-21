from typing import List
from fastapi import APIRouter, HTTPException, Request
from model.userModel import UserModel
from bll.services.userService import UserService
from database.database import session

route = APIRouter(
    prefix="/hello",
    tags=["Hello Router"]
    )

helloService = UserService(session)

@route.get("/helloWorld", response_model=List[UserModel], status_code=200)
async def hello_world():
    return helloService.get_all_user()

@route.post("/post_test_json", status_code=200)
async def post_json(user: UserModel):
    print(user)
    return user

@route.get("/make_coffee", status_code=201)
async def make_coffee():
    raise HTTPException(status_code=418, detail="I'm a teapot")
    return "Cup of coffee"


@route.get("/byebye")
async def byebye():
    return {"message": "ByeBye"}