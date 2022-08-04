import time
import threading
from starlette.responses import RedirectResponse
from app.routers.userRouter import route as r_usr
from app.routers.resourceRouter import route as r_res
from bll.services.goldService import *


def loop_gold_rate():
    gold = GoldService()
    while True:
        # gold.update_gold_rate()
        time.sleep(3600*24)


def main(app):
    app.include_router(r_usr)
    app.include_router(r_res)
    thread = threading.Thread(target=loop_gold_rate)
    thread.start()

    @app.get('/')
    def hello():
        return RedirectResponse(url='/docs')


