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
        url="http://127.0.0.1:3000/register",
        json=RegisterModel(
            url="http://127.0.0.1:3002",
            app="processing-service",
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
        print("!!!!!!!!!!!!!!! Failed registration !!!!!!!!!!!!!!!")

    return response.json()



@app.get("/")
def index():
    return register()
    



if __name__ == "__main__":
    register()
    uvicorn.run("main:app", port=3002, reload=True)
