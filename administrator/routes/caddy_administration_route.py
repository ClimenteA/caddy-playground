import fastapi
from administrator import tasks


router = fastapi.APIRouter()


@router.get("/start")
def start():
    return tasks.caddy_start()


@router.get("/stop")
def stop():
    return tasks.caddy_stop()


@router.get("/update")
def update():
    return tasks.caddy_update()



