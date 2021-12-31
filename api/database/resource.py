from sqlalchemy import Column, Integer, BIGINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Resource(Base):
    __tablename__ = "resource"

    id_res = Column(Integer, primary_key=True)
    id_type_res = Column(Integer)
    id_name_res = Column(Integer)
    id_user = Column(BIGINT)
    quantity = Column(Integer)
    