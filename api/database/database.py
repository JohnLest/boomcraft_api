from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('mariadb+mariadbconnector://root:ettuobel1970!@192.113.50.7:40000/boomcraft_api')
Session = sessionmaker(bind=engine)
session = Session()

