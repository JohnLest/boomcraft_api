from typing import List
from fastapi import APIRouter, HTTPException
from model.ressourceModel import RessourceModel
from bll.services.ressourceService import RessourceService
from database.database import session

route = APIRouter(
    prefix="/ressource",
    tags=["Ressource Router"]
    )

ressource_service = RessourceService(session)


@route.get("/get_ressources", response_model=RessourceModel, status_code=200)
async def get_ressources():
    return None


@route.put("/update_user", response_model=RessourceModel, status_code=200)
async def update_ressources():
    return None

