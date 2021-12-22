from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TypeResource(Base):
    __tablename__ = "type_resource"

    id_type_res = Column(Integer, primary_key=True)
    name = Column(String)

