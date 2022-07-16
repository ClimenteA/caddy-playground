import jinja2
from .caddy_start import caddy_start
from administrator.models import CaddyfileModel


def caddy_update(payload: CaddyfileModel):
    
    with open("Caddyfile.jinja", "r") as f:
        raw_contents = f.read()

    file_contents = jinja2.Template(raw_contents).render(CaddyfileModel(**payload).dict())

    with open("Caddyfile", 'w') as f:
        f.write(file_contents)

    return caddy_start()

