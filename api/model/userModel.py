from pydantic import BaseModel


class UserModel(BaseModel):
    idUser: int
    name: str
    age: int

    class Config:
        orm_mode = True
        