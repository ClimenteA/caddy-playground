import subprocess
from .caddy_stop import caddy_stop



def caddy_start():
    caddy_stop()
    args = ("./caddy", "run", "--pidfile", "caddy.pid")
    proc = subprocess.Popen(args, stdout=subprocess.PIPE)
    return proc.pid
