import requests
from database.database import session
from dal.repository.weight_resourceRepo import WeightResourceRepo
from database.weight_resource import WeightResource
from datetime import datetime




class GoldService:
    def __init__(self):
        self.weight_res_repo = WeightResourceRepo(session, WeightResource)
        self.base_currency = 'EUR'
        self.endpoint = 'carat'
        self.access_key = '0y3ocp4lz4ptzdz9xgpd73p7fw27q3n1m43j66mc6g58qcgri8v98oh0sk28'

    def update_gold_rate(self):
        self.weight_res_repo.session = session
        resp = requests.get(
            'https://metals-api.com/api/'+self.endpoint+'?access_key='+self.access_key)
        resp_json = resp.json()
        rate_gram = int((resp_json["rates"]["Carat 24K"]*5)*100)
        self.weight_res_repo.update(update={WeightResource.weight: rate_gram},
                                    filter=WeightResource.id_name_res == 5)
