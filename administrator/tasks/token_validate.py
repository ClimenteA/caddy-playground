from datetime import datetime
from administrator.models import TokenModel



def validate_token(t: TokenModel, db):

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
