from dal.repository.userRepo import UserRepo
from database.user import User

class UserService:
    def __init__(self, session):
        self.repo = UserRepo(session, User)

    def get_all_user(self):
        result = self.repo.get_all()
        return result

    def get_user_by_id(self, id):
        result = self.repo.get_by_id(id)
        return result



    
