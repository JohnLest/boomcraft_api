from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class WeightResource(Base):
    __tablename__ = "weight_resource"

    id_weight_res = Column(Integer, primary_key=True)
    id_name_res = Column(Integer)
    weight = Column(Integer)

