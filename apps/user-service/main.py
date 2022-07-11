from imp import reload
import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def index():
    return "user-service"




if __name__ == "__main__":
    uvicorn.run("main:app", port=3000, reload=True)
