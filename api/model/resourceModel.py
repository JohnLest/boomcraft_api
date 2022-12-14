from pydantic import BaseModel


class ResourceModel(BaseModel):
    id_res: int
    id_type_res: int
    id_name_res: int
    id_user: int
    quantity: int

    class Config:
        orm_mode = True


class GetResourceModel(BaseModel):
    id_res: int
    type: str
    resource: str
    quantity: int

    class Config:
        orm_mode = True


class UpdateResourceModel(BaseModel):
    id_user: int
    id_name_res: int
    quantity: int

    class Config:
        orm_mode = True


class GetWeightResourceModel(BaseModel):
    id_weight_res: int
    id_name_res: int
    name: str
    weight: int

    class Config:
        orm_mode = True


class UpdateWeightResourceModel(BaseModel):
    id_weight_res: int
    id_name_res: int
    weight: int

    class Config:
        orm_mode = True
