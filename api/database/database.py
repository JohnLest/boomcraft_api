from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('mariadb+mariadbconnector://boomcraft:123_BmCraft@192.168.0.101:3307/boomcraft_api')
Session = sessionmaker(bind=engine)


