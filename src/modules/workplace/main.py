import fastapi

from .routes.app import app_router


def run() -> fastapi.FastAPI:
    app = fastapi.FastAPI()
    app.include_router(app_router)

    return app


app = run()
