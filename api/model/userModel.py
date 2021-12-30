from pydantic import BaseModel
from typing import List


class UserModel(BaseModel):
    id_user: int
    pseudo: str
    mail: str
    password: str

    class Config:
        orm_mode = True


class GetUserModel(BaseModel):
    id_user: int
    pseudo: str
    mail: str

    class Config:
        orm_mode = True


class PostUserModel(BaseModel):
    pseudo: str
    mail: str
    password: str

    class Config:
        orm_mode = True


class GetFriendModel(BaseModel):
    friend_asc: str
    friend_des: List[str]

    class Config:
        orm_mode = True


class PostFriendModel(BaseModel):
    friend_asc: int
    friend_des: int

    class Config:
        orm_mode = True
