from app.routers.userRouter import route as r_usr
from app.routers.resourceRouter import route as r_ress
from app.routers.helloRouter import route as r_hello


def main(app):
    app.include_router(r_usr)
    app.include_router(r_ress)
    app.include_router(r_hello)

