from fastapi import APIRouter
from app.routes import employee


class AppRouterConfig:

    @staticmethod
    def inject_api_routers() -> APIRouter:
        app_router = APIRouter()

        app_router.include_router(employee.router, tags=["employee"])

        return app_router
