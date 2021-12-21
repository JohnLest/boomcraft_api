from typing import List
from fastapi import APIRouter, HTTPException
from model.userModel import UserModel
from bll.services.userService import UserService
from database.database import session

route = APIRouter(
    prefix="/user",
    tags=["User Router"]
    )

user_service = UserService(session)


@route.get("/get_user/{id_user}", response_model=UserModel, status_code=200)
async def get_user(id_user: int):
    return user_service.get_user_by_id(id_user)


@route.post("/post_user", response_model=UserModel, status_code=200)
async def post_user():
    return None

