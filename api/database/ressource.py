from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Ressource(Base):
    __tablename__ = "ressource"

    id_ress = Column(Integer, primary_key = True)
    idUser = Column(Integer)
    idType = Column(Integer)
    name = Column(String)
    quantity = Column(Integer)
    