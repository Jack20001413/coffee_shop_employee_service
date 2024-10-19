from fastapi.testclient import TestClient
from httpx import Response
from app.main import app

test_client = TestClient(app)


def test_list_employees() -> None:
    response: Response = test_client.get("/employees")
    assert response.status_code == 200
