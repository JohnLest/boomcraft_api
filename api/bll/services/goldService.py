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
        self.access_key = 'iu11miori1q84ubzp0o28j73qp99v2gxy55vw9p7yu1jrm58n4t3mkofa003'

    def update_gold_rate(self):
        resp = requests.get(
            'https://metals-api.com/api/'+self.endpoint+'?access_key='+self.access_key)
        resp_json = resp.json()
        rate_gram = int((resp_json["rates"]["Carat 24K"]*5)*100)
        print(resp_json["timestamp"])
        print(datetime.fromtimestamp(resp_json["timestamp"]))
        print(rate_gram)
        self.weight_res_repo.update(update={WeightResource.weight: rate_gram},
                                    filter=WeightResource.id_name_res == 5)
