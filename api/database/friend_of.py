from sqlalchemy import Column, Integer, BIGINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class FriendOf(Base):
    __tablename__ = "friend_of"

    id_friend_of = Column(Integer, primary_key=True)
    friend_asc = Column("id_user_asc", BIGINT)
    friend_des = Column("id_user_des", BIGINT)
