from fastapi import FastAPI
from .config.router import AppRouterConfig
from .repository.schema import initialize_database


app = FastAPI()

app.include_router(AppRouterConfig.inject_api_routers())

initialize_database()
