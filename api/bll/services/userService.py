from sqlalchemy import and_
from datetime import datetime
from dal.repository.userRepo import UserRepo
from dal.repository.friendOfRepo import FriendOfRepo
from database.user import User
from database.friend_of import FriendOf
from model.userModel import PostUserModel, PostFriendModel


class UserService:
    def __init__(self, session):
        self.session = session
        self.user_repo = UserRepo(self.session, User)
        self.friend_repo = FriendOfRepo(self.session, FriendOf)

    def get_all_user(self):
        result = self.user_repo.get_all()
        return result

    def get_user_by_id(self, id):
        result = self.user_repo.get_by_id(id)
        return result

    def get_user_by_mail(self, mail: str):
        result = self.user_repo.get_first(User.mail == mail.lower())
        return result

    def mail_is_exist(self, mail: str):
        if self.user_repo.count_filter(User.mail == mail.lower()) == 0:
            return False
        return True

    def pseudo_is_exist(self, pseudo: str):
        if self.user_repo.count_filter(User.pseudo == pseudo.lower()) == 0:
            return False
        return True

    def already_friend(self, id_asc, id_des):
        if self.friend_repo.count_filter(and_(FriendOf.friend_asc == id_asc,
                                              FriendOf.friend_des == id_des)) != 0:
            return True
        elif self.friend_repo.count_filter(and_(FriendOf.friend_asc == id_des,
                                                FriendOf.friend_des == id_asc)) != 0:
            return True
        return False

    def connect(self, mail: str, psswd):
        user = self.user_repo.get_first(and_(User.mail == mail.lower(),
                                             User.password == psswd))
        return user

    def get_friend_list(self, id):
        friend_id_list = self.friend_repo.get_all_filter(FriendOf.friend_asc == id)
        friend_id_list.extend(self.friend_repo.get_all_filter(FriendOf.friend_des == id))
        return friend_id_list

    def post_new_user(self, data: PostUserModel):
        user = User(id_user=int(datetime.now().timestamp() * 1000),
                    pseudo=data.pseudo.lower(),
                    mail=data.mail.lower(),
                    password=data.password)
        try:
            result = self.user_repo.insert(user)
        except:
            self.session.rollback()
            return "error"
        return result

    def post_new_friend(self, data: PostFriendModel):
        friend = FriendOf(friend_asc=data.friend_asc,
                          friend_des=data.friend_des)
        try:
            result = self.user_repo.insert(friend)
        except:
            self.session.rollback()
            return "error"
        return result
