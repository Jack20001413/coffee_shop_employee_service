from typing import Self
import uuid

import psycopg2


class PostgresTestConnector:
    """
    This class is used for creating a temporary Postgres database for testing.
    """

    def __init__(
        self,
        default_db: str = "postgres",
        user: str = "postgres",
        password: str = "password",
        host: str = "localhost",
        port: str = "5432",
        be_async: bool = False,
    ) -> None:
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.db_name = f"A{str(uuid.uuid4()).replace("-", "")}Z".lower()
        self.conn = psycopg2.connect(
            database=default_db, user=user, password=password, host=host, port=port
        )
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()

        statement = f"CREATE DATABASE {self.db_name};"
        self.cursor.execute(statement)
        print("Database has been created successfully!")

        self.db_url = f"postgresql://{user}:{password}@{host}:{port}/{self.db_name}"
        if be_async:
            self.db_url = (
                f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{self.db_name}"
            )

    def get_db_url(self) -> str:
        return self.db_url

    def _drop_db(self) -> None:
        if not self.conn:
            self.conn = psycopg2.connect(
                database="postgres",
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
            )

        self.cursor = self.conn.cursor()

        statement = f"DROP DATABASE {self.db_name} WITH (FORCE);"
        self.cursor.execute(statement)
        print("Database has been successfully deleted!")

        self.conn.close()
        self.conn = None

    def __enter__(self) -> Self:
        return self

    def __exit__(self, type, value, traceback) -> None:
        self._drop_db()
