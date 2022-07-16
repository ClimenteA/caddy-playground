import uuid
import uvicorn
from datetime import datetime, timedelta
from fastapi import FastAPI
from pydantic import BaseModel
import logging as log
from typing import Optional


app = FastAPI()

db = {
    "registered_services": {},
    "valid_app_tokens": {},
    "approved_apps": {
        "auth-service": "secret-token",
        "processing-service": "secret-token",
        "user-service": "secret-token",
        "frontend-service": "secret-token",
    }
}

SECRET = "secret"


@app.get("/")
def index():
    return "discovery-service"


class RegisterModel(BaseModel):
    url: str
    app: str
    token: str
    meta: dict


class TokenModel(BaseModel):
    token: str
    app: Optional[str]


def register_service(register: RegisterModel):

    if register.app in db["approved_apps"]:
        if db["approved_apps"][register.app] == register.token:

            new_token = str(uuid.uuid4())
            db["valid_app_tokens"][register.app] = {
                "token": new_token, 
                "expire": (datetime.utcnow() + timedelta(minutes=30)).isoformat()
            }
            register.token = None
            db["registered_services"][register.app] = register.dict()

            log.info(f"Registration successful for '{register.app}'!")
            return TokenModel(token=new_token)

    return "Invalid credentials"


def validate_token(t: TokenModel):

    registered_app = db["valid_app_tokens"].get(t.app)
    if not registered_app:
        return False

    valid_token = registered_app["token"] == t.token
    if not valid_token:
        return False    

    now = datetime.utcnow()
    expire_stamp = datetime.fromisoformat(registered_app["expire"].replace('Z', '+00:00'))
    expired_token = now > expire_stamp
    if expired_token:
        return False

    return True




@app.post("/register", response_model=TokenModel)
def register(register: RegisterModel):
    return register_service(register)


@app.get("/registered")
def registered():
    return db


@app.get("/services")
def registered_services():
    return db["registered_services"]


@app.post("/validate-token")
def valid_token(t: TokenModel):
    return validate_token(t)
    



if __name__ == "__main__":
    uvicorn.run("main:app", port=3000, reload=True)
