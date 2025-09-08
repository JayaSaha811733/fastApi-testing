import os
from django.core.asgi import get_asgi_application
from fastapi_app import app as fastapi_app
from starlette.middleware.wsgi import WSGIMiddleware
from starlette.routing import Mount
from starlette.applications import Starlette

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

django_asgi_app = get_asgi_application()

# Mount Django under /django and FastAPI under /api (or root)
routes = [
    Mount("/admin", app=django_asgi_app),
    Mount("/api", app=fastapi_app),
]

application = Starlette(routes=routes)