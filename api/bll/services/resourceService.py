from dal.repository.resourceRepo import ResourceRepo
from dal.repository.v_resourceRepo import VResourceRepo
from database.resource import Resource
from database.v_resource import VResource

class ResourceService:
    def __init__(self, session):
        self.resource_repo = ResourceRepo(session, Resource)
        self.v_resource_repo = VResourceRepo(session, VResource)

    def get_all_resource(self):
        result = self.resource_repo.get_all()
        return result

    def get_resources_by_user_id(self, user_id):
        result = self.v_resource_repo.get_all_filter(VResource.id_user == user_id)
        return result
