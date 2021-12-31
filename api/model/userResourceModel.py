from pydantic import BaseModel
from typing import List
from model.userModel import GetUserModel
from model.resourceModel import GetResourceModel


class UserResourceModel(BaseModel):
    pseudo: GetUserModel
    resource: List[GetResourceModel]
