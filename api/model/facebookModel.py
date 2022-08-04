from pydantic import BaseModel


class FacebookModel(BaseModel):
    id: str
    name: str
    email: str
