# Caddy Playground

Trying Caddy2 webserver in a simulated microservice environment. 


Steps:
- download caddy binary from [caddyserver.com](https://caddyserver.com/);
- set permision to lower ports to caddy binary with `sudo setcap CAP_NET_BIND_SERVICE=+eip ./caddy`;
- each service in `apps` folder must provide a public url (auth is handled on the service);
- when opening `localhost` in the browser the js application (SPA) will load and interact with the microservices; 
- start the services by cd into service's package and run `python3 main.py`;
- update Caddyfile for each new service added (TODO - use caddy api to update it automatically);
- start caddy webserver with `./caddy run --pidfile caddy.pid`;


Dependencies:
- FastAPI
- uvicorn
- requests


Ocasional issues:
- Kill in use port with: `sudo fuser -k 3000/tcp`; 