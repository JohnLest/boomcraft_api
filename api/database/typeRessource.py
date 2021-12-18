from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TypeRessource(Base):
    __tablename__ = "typeRessource"

    id_type = Column(Integer, primary_key=True)
    name = Column(String)

