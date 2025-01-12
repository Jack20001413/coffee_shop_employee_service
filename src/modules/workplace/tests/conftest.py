import logging
import fastapi.testclient
import pytest

from ..main import app


LOGGER: logging.Logger = logging.getLogger(__name__)


@pytest.fixture
def test_client() -> fastapi.testclient.TestClient:
    return fastapi.testclient.TestClient(app=app, base_url="http://localhost:8000")
