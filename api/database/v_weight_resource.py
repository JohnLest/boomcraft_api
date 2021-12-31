from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class VWeightResource(Base):
    __tablename__ = "v_weight_resource"

    id_weight_res = Column(Integer, primary_key=True)
    id_name_res = Column(Integer)
    name = Column(String)
    weight = Column(Integer)

