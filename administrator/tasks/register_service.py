import uuid
from datetime import datetime, timedelta
from administrator.models import RegisterServiceModel, TokenModel



def register_service(register: RegisterServiceModel, db):

    if register.app in db["approved_apps"]:
        if db["approved_apps"][register.app] == register.token:

            new_token = str(uuid.uuid4())
            db["valid_app_tokens"][register.app] = {
                "token": new_token, 
                "expire": (datetime.utcnow() + timedelta(minutes=30)).isoformat()
            }
            register.token = None
            db["registered_services"][register.app] = register.dict()

            return TokenModel(token=new_token)

    return "Invalid credentials"

