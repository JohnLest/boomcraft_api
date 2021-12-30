from sqlalchemy import and_
from datetime import datetime
from typing import List
from dal.repository.userRepo import UserRepo
from dal.repository.friendOfRepo import FriendOfRepo
from database.user import User
from database.friend_of import FriendOf
from model.userModel import PostUserModel, PostFriendModel


class UserService:
    def __init__(self, session):
        self.user_repo = UserRepo(session, User)
        self.friend_repo = FriendOfRepo(session, FriendOf)


    def get_all_user(self):
        result = self.user_repo.get_all()
        return result

    def get_user_by_id(self, id):
        result = self.user_repo.get_by_id(id)
        return result

    def get_user_by_mail(self, mail):
        result = self.user_repo.get_first(User.mail == mail)
        return result

    def connect(self, mail, psswd):
        user = self.user_repo.get_first(and_(User.mail == mail,
                                             User.password == psswd))
        return user

    def get_friend_list(self, id):
        friend_id_list = self.friend_repo.get_all_filter(FriendOf.friend_asc == id)
        friend_id_list.extend(self.friend_repo.get_all_filter(FriendOf.friend_des == id))
        return friend_id_list

    def post_new_user(self, data: PostUserModel):
        user = User(id_user = int(datetime.now().timestamp()*1000), pseudo = data.pseudo, mail = data.mail, password = data.password)
        result = self.user_repo.insert(user)
        return result

    def post_new_friend(self, data: PostFriendModel):
        friend = FriendOf(friend_asc=data.friend_asc, friend_des=data.friend_des)
        result = self.user_repo.insert(friend)
        return result
