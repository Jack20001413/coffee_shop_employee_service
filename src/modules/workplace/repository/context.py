import dotenv
import sqlalchemy
import sqlmodel
import os
import urllib.parse

from typing import Any, Generator

# Ref: https://sqlmodel.tiangolo.com/tutorial/create-db-and-table/#sqlmodel-metadata-order-matters
from . import model

use_dot_env = bool(os.getenv("USE_DOT_ENV"))

if use_dot_env:
    dotenv.load_dotenv()

USER = os.getenv("DATABASE_USER")
PASSWORD = os.getenv("DATABASE_PASSWORD")
HOST = os.getenv("DATABASE_HOST")
DB_NAME = os.getenv("DATABASE_NAME")
PORT = os.getenv("DATABASE_PORT")

connection_string: str = (
    f"postgresql+psycopg2://{USER}:%s@{HOST}:{PORT}/{DB_NAME}"
) % urllib.parse.quote_plus(PASSWORD)
engine: sqlalchemy.Engine = sqlmodel.create_engine(connection_string, echo=True)


def get_session() -> Generator[sqlmodel.Session, Any, None]:
    with sqlmodel.Session(engine) as session:
        yield session
