from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id_user = Column(Integer, primary_key = True)
    pseudo = Column(String)
    age = Column(Integer)
    password = Column(String)