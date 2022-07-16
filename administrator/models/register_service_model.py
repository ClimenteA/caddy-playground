from pydantic import BaseModel


class RegisterServiceModel(BaseModel):
    url: str
    app: str
    token: str
    meta: dict
