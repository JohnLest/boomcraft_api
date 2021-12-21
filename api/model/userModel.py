from pydantic import BaseModel


class UserModel(BaseModel):
    id_user: int
    pseudo: str
    mail: str

    class Config:
        orm_mode = True
        