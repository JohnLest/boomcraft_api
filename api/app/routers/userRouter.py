from fastapi import APIRouter, HTTPException
from typing import Optional
from model.userModel import GetUserModel, PostUserModel
from bll.services.userService import UserService
from database.database import session

route = APIRouter(
    prefix="/user",
    tags=["User Router"]
    )

user_service = UserService(session)


@route.get("/get_user/", response_model=GetUserModel, status_code=200)
async def get_user(mail_user: Optional[str] = None, id_user: Optional[int] = None):
    user: GetUserModel = None
    if mail_user is None and id_user is None:
        raise HTTPException(status_code=400, detail="Bad Request : No parameter")
    elif id_user is not None:
        user = user_service.get_user_by_id(id_user)
    elif mail_user is not None:
        user = user_service.get_user_by_mail(mail_user)
    if user is None:
        raise HTTPException(status_code=404, detail="Not Found : no user found")
    return user


@route.post("/post_new_user", response_model=GetUserModel, status_code=200)
async def post_new_user(user: PostUserModel):
    new_user = user_service.post_new_user(user)
    return new_user

