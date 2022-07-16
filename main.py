import fastapi



app = fastapi.FastAPI()

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
