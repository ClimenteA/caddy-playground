import uvicorn
import fastapi
import requests
from pydantic import BaseModel



class RegisterModel(BaseModel):
    url: str
    app: str
    token: str
    meta: dict


app = fastapi.FastAPI()


def register():

    response = requests.post(
        url="http://localhost/api/discovery-service/register",
        json=RegisterModel(
            url="http://127.0.0.1:3001",
            app="auth-service",
            token="secret-token",
            meta={
                "extracustom": [
                    "some",
                    "info"
                ]
            }
        ).dict()
    )

    if response.status_code != 200:
        print("Registration failed!")
        print(response.content)
        return {}

    print("Registration successful!")
    return response.json()



@app.get("/")
def index():
    return register()
    



if __name__ == "__main__":
    register()
    uvicorn.run("main:app", port=3001, reload=True)
