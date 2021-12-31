import time
import threading
from app.routers.userRouter import route as r_usr
from app.routers.resourceRouter import route as r_res
from app.routers.helloRouter import route as r_hello
from bll.services.goldService import *


def loop_gold_rate():
    gold = GoldService()
    while True:
        gold.update_gold_rate()
        time.sleep(3600)


def main(app):
    app.include_router(r_usr)
    app.include_router(r_res)
    app.include_router(r_hello)
    thread = threading.Thread(target=loop_gold_rate)
    thread.start()


