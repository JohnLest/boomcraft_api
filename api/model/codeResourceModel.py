from pydantic import BaseModel
from typing import List


class TypeResourceModel(BaseModel):
    id_type_res: int
    name: str

    class Config:
        orm_mode = True


class NameResourceModel(BaseModel):
    id_name_res: int
    name: str

    class Config:
        orm_mode = True


class CodeModel(BaseModel):
    type_resource: List[TypeResourceModel]
    name_resource: List[NameResourceModel]

    class Config:
        orm_mode = True
