from datetime import datetime
from sqlmodel import Field, SQLModel


class Workplace(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    address: str
    created_at: datetime | None = Field(nullable=False, default_factory=datetime.now)
    updated_at: datetime | None = Field(nullable=False, default_factory=datetime.now)
