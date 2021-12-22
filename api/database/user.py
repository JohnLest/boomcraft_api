from sqlalchemy import Column, String, BIGINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id_user = Column(BIGINT, primary_key = True)
    pseudo = Column(String)
    mail = Column("mail_address", String)
    password = Column(String)
