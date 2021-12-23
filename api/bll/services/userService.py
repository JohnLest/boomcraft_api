from sqlalchemy import and_
from datetime import datetime
from dal.repository.userRepo import UserRepo
from database.user import User
from model.userModel import PostUserModel


class UserService:
    def __init__(self, session):
        self.repo = UserRepo(session, User)

    def get_all_user(self):
        result = self.repo.get_all()
        return result

    def get_user_by_id(self, id):
        result = self.repo.get_by_id(id)
        return result

    def get_user_by_mail(self, mail):
        result = self.repo.get_first(User.mail == mail)
        return result

    def connect(self, mail, psswd):
        user = self.repo.get_first(and_(User.mail == mail,
                                        User.password == psswd))
        return user

    def post_new_user(self, data: PostUserModel):
        user = User(id_user = int(datetime.now().timestamp()*1000), pseudo = data.pseudo, mail = data.mail, password = data.password)
        result = self.repo.insert(user)
        return result

    
