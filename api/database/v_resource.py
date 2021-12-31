from sqlalchemy import Column, Integer, String, BIGINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class VResource(Base):
    __tablename__ = "v_resource"

    id_res = Column(Integer, primary_key=True)
    id_user = Column(BIGINT)
    type = Column(String)
    resource = Column(String)
    quantity = Column(Integer)

