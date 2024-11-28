from contextlib import asynccontextmanager

from fastapi import FastAPI
from .config.router import AppRouterConfig
from .config.db import DBContext


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    db_context = DBContext()
    db_context.initialize_database()

    yield


app = FastAPI(lifespan=lifespan)
app.include_router(AppRouterConfig.inject_api_routers())
