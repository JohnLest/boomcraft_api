from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class NameResource(Base):
    __tablename__ = "name_resource"

    id_name_res = Column(Integer, primary_key=True)
    name = Column(String)

