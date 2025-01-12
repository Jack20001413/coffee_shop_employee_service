import fastapi

from .workplace import router as workplace_router
from .healthcheck import router as healthcheck_router

app_router = fastapi.APIRouter()

app_router.include_router(workplace_router)
app_router.include_router(healthcheck_router)
