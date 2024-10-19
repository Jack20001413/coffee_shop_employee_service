from fastapi import FastAPI, APIRouter
from .routes import employee


app = FastAPI()
api_router = APIRouter()

api_router.include_router(employee.router, tags=["employees"])

app.include_router(api_router)
