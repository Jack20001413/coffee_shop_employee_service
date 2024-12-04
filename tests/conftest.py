import logging
from fastapi.testclient import TestClient
import pytest
from sqlmodel import SQLModel, create_engine

from tests.utils.postgres_connector import PostgresTestConnector
from src.main import app


LOGGER: logging.Logger = logging.getLogger(__name__)


@pytest.fixture
def db_connector():
    with PostgresTestConnector(user="", password="", host="", port="") as connector:
        yield connector


@pytest.fixture
def setup_test_db(db_connector):
    engine = create_engine(db_connector.get_db_url(), echo=True)
    SQLModel.metadata.create_all(engine)
    LOGGER.info("Creating database...")
    LOGGER.info(db_connector.get_db_url())

    yield engine


@pytest.fixture
def test_client() -> TestClient:
    return TestClient(app=app)
