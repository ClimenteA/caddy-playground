import uvicorn
import fastapi
import requests
from pydantic import BaseModel
import logging as log
from typing import Optional


class RegisterModel(BaseModel):
    url: str
    app: str
    token: str
    meta: dict



class TokenModel(BaseModel):
    token: str
    app: Optional[str]


app = fastapi.FastAPI()


db = {}


def register():

    response = requests.post(
        url="http://127.0.0.1/api/discovery-service/register",
        json=RegisterModel(
            url="http://127.0.0.1:3001",
            app="auth-service",
            token="secret-token",
            meta={}
        ).dict()
    )

    if response.status_code != 200:
        log.error("Registration failed!")
        log.error(response.content)
        return {}

    log.info("Registration successful!")

    data = response.json()
    return data



@app.get("/")
def index():
    return register()
    

@app.get("/data")
def data():
    return {"some": "data"}
    

@app.get("/protected")
def protectedroute(token: str = fastapi.Header(None)):

    response = requests.post(
        url="http://127.0.0.1/api/discovery-service/validate-token",
        json=TokenModel(
            app="auth-service",
            token=token,
        ).dict()
    )

    if response.json() is True:
        return "Ok, authentificated"
        
    return "Invalid token"
    



if __name__ == "__main__":
    register()
    uvicorn.run("main:app", port=3001, reload=True)
