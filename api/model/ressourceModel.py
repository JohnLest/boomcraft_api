from pydantic import BaseModel


class RessourceModel(BaseModel):
    id_ress: int
    name: str
    quantity: int

    class Config:
        orm_mode = True
