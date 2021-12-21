from pydantic import BaseModel


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