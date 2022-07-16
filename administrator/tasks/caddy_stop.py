import os
import signal



def caddy_stop():
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
