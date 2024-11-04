from sqlmodel import create_engine, SQLModel
from urllib.parse import quote_plus

# Ref: https://sqlmodel.tiangolo.com/tutorial/create-db-and-table/#sqlmodel-metadata-order-matters
import app.models


class DBContext:
    DB_USERNAME = "postgres"
    DB_PASSWORD = "J@ckStune286"
    DB_HOST = "db"
    DB_NAME = "employee_management"
    DB_PORT = "5432"
    DB_CONNECTION_STRING = (
        f"postgresql+psycopg2://{DB_USERNAME}:%s@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    ) % quote_plus(DB_PASSWORD)

    def __init__(self) -> None:
        self._db_engine = create_engine(DBContext.DB_CONNECTION_STRING, echo=True)

    def initialize_database(self) -> None:
        print(f"SQLModel metadata: {SQLModel.metadata.tables}")
        SQLModel.metadata.create_all(self._db_engine)
