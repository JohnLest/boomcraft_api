from typing import List
from fastapi import APIRouter, HTTPException
from model.resourceModel import ResourceModel
from model.userResourceModel import UserResourceModel
from bll.services.resourceService import ResourceService
from bll.services.userService import UserService
from database.database import session

route = APIRouter(
    prefix="/resource",
    tags=["Resource Router"]
    )

resource_service = ResourceService(session)
user_service = UserService(session)


@route.get("/get_resources_by_user_id/{user_id}", response_model=UserResourceModel, status_code=200)
async def get_resources(user_id: int):
    resource_list = resource_service.get_resources_by_user_id(user_id)
    user = user_service.get_user_by_id(user_id)
    u_r_model = UserResourceModel(pseudo = user, resource = resource_list)
    return u_r_model


@route.put("/update_user", response_model=ResourceModel, status_code=200)
async def update_resources():
    return None

