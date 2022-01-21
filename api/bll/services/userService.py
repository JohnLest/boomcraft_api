import uuid
from sqlalchemy import and_
from datetime import datetime
from database.database import Session
from dal.repository.userRepo import UserRepo
from dal.repository.friendOfRepo import FriendOfRepo
from database.user import User
from database.friend_of import FriendOf
from model.userModel import PostUserModel, PostFriendModel
from model.facebookModel import FacebookModel


class UserService:
    def __init__(self):
        _session = Session()
        self.user_repo = UserRepo(_session, User)
        self.friend_repo = FriendOfRepo(_session, FriendOf)

    def get_all_user(self):
        self.user_repo.session = Session()
        try:
            result = self.user_repo.get_all()
        except:
            self.user_repo.session.rollback()
            self.user_repo.session.close()
            return "error"
        self.user_repo.session.close()
        return result

    def get_user_by_id(self, id):
        self.user_repo.session = Session()
        try:
            result = self.user_repo.get_by_id(id)
        except:
            self.user_repo.session.rollback()
            self.user_repo.session.close()
            return "error"
        self.user_repo.session.close()
        return result

    def get_user_by_mail(self, mail: str):
        self.user_repo.session = Session()
        try:
            result = self.user_repo.get_first(User.mail == mail.lower())
        except:
            self.user_repo.session.rollback()
            self.user_repo.session.close()
            return "error"
        self.user_repo.session.close()
        return result

    def mail_is_exist(self, mail: str):
        self.user_repo.session = Session()
        try:
            if self.user_repo.count_filter(User.mail == mail.lower()) == 0:
                self.user_repo.session.close()
                return False
        except:
            self.user_repo.session.rollback()
        self.user_repo.session.close()
        return True

    def pseudo_is_exist(self, pseudo: str):
        self.user_repo.session = Session()
        try:
            if self.user_repo.count_filter(User.pseudo == pseudo.lower()) == 0:
                self.user_repo.session.close()
                return False
        except:
            self.user_repo.session.rollback()
        self.user_repo.session.close()
        return True

    def already_friend(self, id_asc, id_des):
        self.friend_repo.session = Session()
        try:
            if self.friend_repo.count_filter(and_(FriendOf.friend_asc == id_asc,
                                                  FriendOf.friend_des == id_des)) != 0:
                self.friend_repo.session.close()
                return True
            elif self.friend_repo.count_filter(and_(FriendOf.friend_asc == id_des,
                                                    FriendOf.friend_des == id_asc)) != 0:
                self.friend_repo.session.close()
                return True
        except:
            self.friend_repo.session.rollback()
            self.friend_repo.session.close()
            return True

    def connect(self, mail: str, psswd):
        self.user_repo.session = Session()
        try:
            user = self.user_repo.get_first(and_(User.mail == mail.lower(),
                                                 User.password == psswd))
        except:
            self.user_repo.session.rollback()
            self.user_repo.session.close()
            return "error"
        self.user_repo.session.close()
        return user

    def get_friend_list(self, id):
        self.friend_repo.session = Session()
        try:
            friend_id_list = self.friend_repo.get_all_filter(FriendOf.friend_asc == id)
            friend_id_list.extend(self.friend_repo.get_all_filter(FriendOf.friend_des == id))
        except:
            self.friend_repo.session.rollback()
            self.friend_repo.session.close()
            return "error"
        self.friend_repo.session.close()
        return friend_id_list

    def post_new_user(self, data: PostUserModel):
        self.user_repo.session = Session()
        user = User(id_user=int(datetime.now().timestamp() * 1000),
                    pseudo=data.pseudo.lower(),
                    mail=data.mail.lower(),
                    password=data.password)
        try:
            result = self.user_repo.insert(user)
        except:
            self.user_repo.session.rollback()
            self.user_repo.session.close()
            return "error"
        self.user_repo.session.close()
        return result

    def post_new_fb_user(self, data: FacebookModel):
        self.user_repo.session = Session()
        user = User(id_user=int(data.id),
                    pseudo=f"{data.name}#{str(data.id)[10:]}",
                    mail=data.email,
                    password=str(uuid.uuid4()))
        try:
            result = self.user_repo.insert(user)
        except:
            self.user_repo.session.rollback()
            self.user_repo.session.close()
            return "error"
        self.user_repo.session.close()
        return result

    def post_new_friend(self, data: PostFriendModel):
        self.friend_repo.session = Session()
        friend = FriendOf(friend_asc=data.friend_asc,
                          friend_des=data.friend_des)
        try:
            result = self.user_repo.insert(friend)
        except:
            self.friend_repo.session.rollback()
            self.friend_repo.session.close()
            return "error"
        self.friend_repo.session.close()
        return result
