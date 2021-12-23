from fastapi import APIRouter, HTTPException
from typing import Optional
from model.resourceModel import ResourceModel
from model.userResourceModel import UserResourceModel
from model.userModel import GetUserModel
from model.codeResourceModel import CodeModel
from bll.services.resourceService import ResourceService
from bll.services.userService import UserService
from database.database import session

route = APIRouter(
    prefix="/resource",
    tags=["Resource Router"]
    )

resource_service = ResourceService(session)
user_service = UserService(session)


@route.get("/get_user_resources", response_model=UserResourceModel, status_code=200)
async def get_resources(id_user: Optional[int] = None, mail_user:Optional[str] = None):
    user: GetUserModel = None
    if mail_user is None and id_user is None:
        raise HTTPException(status_code=400, detail="Bad Request : No parameter")
    elif id_user is not None:
        user = user_service.get_user_by_id(id_user)
    elif mail_user is not None:
        user = user_service.get_user_by_mail(mail_user)
    if user is None:
        raise HTTPException(status_code=404, detail="Not Found : no user found")
    resource_list = resource_service.get_resources_by_user_id(user.id_user)
    u_r_model = UserResourceModel(pseudo=user, resource=resource_list)
    return u_r_model


@route.get("/get_code_resource", response_model=CodeModel, status_code=200)
async def get_code_resource():
    type_res, name_res = resource_service.get_code_resource()
    return CodeModel(type_resource=type_res, name_resource=name_res)


@route.put("/update_user", response_model=ResourceModel, status_code=200)
async def update_resources():
    return None

