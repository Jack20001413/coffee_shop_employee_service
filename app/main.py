from fastapi import FastAPI
from .config.router import AppRouterConfig
from .repository.schema import DBContext


app = FastAPI()

app.include_router(AppRouterConfig.inject_api_routers())

dbcontext = DBContext()
dbcontext.initialize_database()
