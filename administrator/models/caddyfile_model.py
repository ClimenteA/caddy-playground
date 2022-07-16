from typing import List
from pydantic import BaseModel


class PathUrlModel(BaseModel):
    path:str
    url:str

class CaddyfileModel(BaseModel):
    base_url: str
    routes: List[PathUrlModel]


# {
#     'base_url': "http://127.0.0.1",
#     'routes': [
#         {
#             "path": "/api/discovery-service",
#             "url": "http://127.0.0.1:3000"
#         },
#         {
#             "path": "/api/auth-service",
#             "url": "http://127.0.0.1:3001"
#         },
#     ]
# }