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
