import os
import signal
import subprocess
import fastapi
import uvicorn
import jinja2


app = fastapi.FastAPI()





def stop_caddy():
    try:
        if not os.path.exists("caddy.pid"): 
            return 0
        
        with open("caddy.pid", "r") as f:
            lines = f.readlines()
        
        pid = int((lines[0]).strip())
        os.kill(pid, signal.SIGTERM) 
        
        return 0
    except:
        return 1


def start_caddy():
    stop_caddy()
    args = ("./caddy", "run", "--pidfile", "caddy.pid")
    proc = subprocess.Popen(args, stdout=subprocess.PIPE)
    return proc.pid



def update_caddyfile():

    with open("Caddyfile.jinja", "r") as f:
        raw_contents = f.read()

    file_contents = jinja2.Template(raw_contents).render(
        **{
            'base_url': "http://127.0.0.1",
            'routes': [
                {
                    "path": "/api/discovery-service",
                    "url": "http://127.0.0.1:3000"
                },
                {
                    "path": "/api/auth-service",
                    "url": "http://127.0.0.1:3001"
                },
            ]
        }
    )

    with open("Caddyfile", 'w') as f:
        f.write(file_contents)

    return start_caddy()


@app.get("/start")
def start():
    return start_caddy()


@app.get("/stop")
def stop():
    return stop_caddy()


@app.get("/update")
def update():
    return update_caddyfile()



if __name__ == "__main__":
    uvicorn.run("manage:app", port=3004, reload=True)

