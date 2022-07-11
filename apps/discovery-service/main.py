import uuid
import uvicorn
from datetime import datetime, timedelta
from fastapi import FastAPI
from pydantic import BaseModel

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


def register_service(register: RegisterModel):

    if register.app in db["approved_apps"]:
        if db["approved_apps"][register.app] == register.token:

            new_token = str(uuid.uuid5(uuid.NAMESPACE_OID, SECRET + register.app + register.token))
            db["valid_app_tokens"][register.app] = {
                "token": new_token, 
                "expire": (datetime.utcnow() + timedelta(days=30)).isoformat()
            }
            register.token = None
            db["registered_services"][register.app] = register.dict()

            return new_token

    return "Invalid credentials"


@app.post("/register")
def register(register: RegisterModel):
    return register_service(register)


@app.get("/registered")
def registered():
    return db




if __name__ == "__main__":
    uvicorn.run("main:app", port=3000, reload=True)
