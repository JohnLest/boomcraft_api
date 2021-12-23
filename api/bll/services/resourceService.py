from dal.repository.resourceRepo import ResourceRepo
from dal.repository.v_resourceRepo import VResourceRepo
from dal.repository.typeResourceRepo import TypeResourceRepo
from dal.repository.nameResourceRepo import NameResourceRepo
from database.resource import Resource
from database.v_resource import VResource
from database.type_resource import TypeResource
from database.name_resource import NameResource


class ResourceService:
    def __init__(self, session):
        self.resource_repo = ResourceRepo(session, Resource)
        self.v_resource_repo = VResourceRepo(session, VResource)
        self.type_resource_repo = TypeResourceRepo(session, TypeResource)
        self.name_resource_repo = NameResourceRepo(session, NameResource)

    def get_all_resource(self):
        result = self.resource_repo.get_all()
        return result

    def get_resources_by_user_id(self, user_id):
        result = self.v_resource_repo.get_all_filter(VResource.id_user == user_id)
        return result

    def get_code_resource(self):
        type_resource = self.type_resource_repo.get_all()
        name_resource = self.name_resource_repo.get_all()
        return type_resource, name_resource
