from fastapi import APIRouter, HTTPException
from typing import Optional
from model.userModel import GetUserModel, PostUserModel, PostFriendModel, GetFriendModel
from bll.services.userService import UserService
from database.database import session

route = APIRouter(
    prefix="/user",
    tags=["User Router"]
    )

user_service = UserService(session)


@route.get("/connect", response_model=GetUserModel, status_code=200)
async def connect(mail_user: str, password: str):
    user = user_service.connect(mail_user.lower(), password)
    if user is None:
        raise HTTPException(status_code=404, detail="Not Found : No user found. Mail or password incorrect")
    return user


@route.get("/get_user", response_model=GetUserModel, status_code=200)
async def get_user(mail_user: Optional[str] = None, id_user: Optional[int] = None):
    user: GetUserModel = None
    if mail_user is None and id_user is None:
        raise HTTPException(status_code=400, detail="Bad Request : No parameter")
    elif id_user is not None:
        user = user_service.get_user_by_id(id_user)
    elif mail_user is not None:
        user = user_service.get_user_by_mail(mail_user.lower())
    if user is None:
        raise HTTPException(status_code=404, detail="Not Found : no user found")
    return user


@route.get("/get_friend/{id_user}", response_model=GetFriendModel, status_code=200)
async def get_friend(id_user: int):
    friend_asc: GetUserModel = user_service.get_user_by_id(id_user)
    if friend_asc is None:
        raise HTTPException(status_code=404, detail="Not Found : no user found")
    friend: PostFriendModel = user_service.get_friend_list(id_user)
    if friend_asc is None:
        raise HTTPException(status_code=404, detail="Not Found : no friend found")
    friend_pseudo_lst = []
    for elem in friend:
        if elem.friend_des == id_user:
            user: GetUserModel = user_service.get_user_by_id(elem.friend_asc)
            friend_pseudo_lst.append(user.pseudo)
        else:
            user: GetUserModel = user_service.get_user_by_id(elem.friend_des)
            friend_pseudo_lst.append(user.pseudo)
    friend_model = GetFriendModel(friend_asc= friend_asc.pseudo, friend_des= friend_pseudo_lst)
    return friend_model


@route.post("/post_new_user", response_model=GetUserModel, status_code=200)
async def post_new_user(user: PostUserModel):
    new_user = user_service.post_new_user(user)
    if new_user == "error":
        if user_service.mail_is_exist(user.mail.lower()):
            raise HTTPException(status_code=500, detail="Internal Server Error : mail is already used")
        elif user_service.pseudo_is_exist(user.pseudo.lower()):
            raise HTTPException(status_code=500, detail="Internal Server Error : pseudo is already used")
        else:
            raise HTTPException(status_code=500, detail="Internal Server Error : Unknown Error")
    return new_user


@route.post("/post_new_friend", status_code=200)
async def post_new_friend(friend: PostFriendModel):
    if user_service.already_friend(friend.friend_asc, friend.friend_des):
        raise HTTPException(status_code=500, detail="Internal Server Error : already friend")
    new_friend = user_service.post_new_friend(friend)
    if new_friend == "error":
        raise HTTPException(status_code=404, detail="Not found: Error with users ID")
    return new_friend
