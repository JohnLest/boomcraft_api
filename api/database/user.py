from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id_user = Column("idUser", Integer, primary_key = True)
    pseudo = Column(String)
    mail = Column("mailAddress", String)
    password = Column(String)
