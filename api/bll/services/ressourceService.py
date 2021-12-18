from dal.repository.ressourceRepo import RessourceRepo
from database.ressource import Ressource

class RessourceService:
    def __init__(self, session):
        self.repo = RessourceRepo(session, Ressource)

    def get_all_ressource(self):
        result = self.repo.get_all()
        return result
