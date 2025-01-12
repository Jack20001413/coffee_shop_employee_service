import fastapi


router = fastapi.APIRouter(tags=["healthcheck"])


@router.get("/healthz")
def health_check() -> fastapi.Response:
    return fastapi.Response(
        status_code=fastapi.status.HTTP_200_OK, content="App is up and running..."
    )
