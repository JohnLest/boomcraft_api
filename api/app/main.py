from app.routers.userRouter import route as r_usr
from app.routers.resourceRouter import route as r_ress
from app.routers.helloRouter import route as r_hello
from bll.services.goldService import *


def main(app):
    app.include_router(r_usr)
    app.include_router(r_ress)
    app.include_router(r_hello)
    gold = GoldService()
    val = gold.get_gold_rate()


