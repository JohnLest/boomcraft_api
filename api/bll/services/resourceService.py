from sqlalchemy import and_
from dal.repository.resourceRepo import ResourceRepo
from dal.repository.v_resourceRepo import VResourceRepo
from dal.repository.typeResourceRepo import TypeResourceRepo
from dal.repository.nameResourceRepo import NameResourceRepo
from dal.repository.v_weight_resourceRepo import VWeightResourceRepo
from database.resource import Resource
from database.v_resource import VResource
from database.type_resource import TypeResource
from database.name_resource import NameResource
from database.v_weight_resource import VWeightResource
from model.resourceModel import UpdateResourceModel


class ResourceService:
    def __init__(self, session):
        self.session = session
        self.resource_repo = ResourceRepo(self.session, Resource)
        self.v_resource_repo = VResourceRepo(self.session, VResource)
        self.type_resource_repo = TypeResourceRepo(self.session, TypeResource)
        self.name_resource_repo = NameResourceRepo(self.session, NameResource)
        self.weight_res_repo = VWeightResourceRepo(self.session, VWeightResource)

    def get_all_resource(self):
        result = self.resource_repo.get_all()
        return result

    def get_resources_by_user_id(self, user_id):
        result = self.v_resource_repo.get_all_filter(VResource.id_user == user_id)
        return result

    def get_resource_by_id(self, id_res):
        result = self.resource_repo.get_by_id(id_res)
        return result

    def get_code_resource(self):
        type_resource = self.type_resource_repo.get_all()
        name_resource = self.name_resource_repo.get_all()
        return type_resource, name_resource

    def get_weight_resource(self):
        weight_res = self.weight_res_repo.get_all()
        return weight_res

    def update_resource_by_user(self, data: UpdateResourceModel):
        try:
            up = self.resource_repo.update(update={Resource.quantity: data.quantity},
                                           filter=and_(Resource.id_user == data.id_user,
                                                       Resource.id_name_res == data.id_name_res))
        except:
            self.session.rollback()
            return "error"
        return next(iter(up), None)

    def update_resource_by_id(self, id_res, new_quantity):
        try:
            up = self.resource_repo.update(update={Resource.quantity: new_quantity},
                                           filter=Resource.id_res == id_res)
        except:
            self.session.rollback()
            return "error"
        return next(iter(up), None)
