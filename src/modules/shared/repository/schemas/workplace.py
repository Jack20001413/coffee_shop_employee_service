from datetime import datetime
from typing import TYPE_CHECKING, List
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .employee import Employee


class Workplace(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    address: str
    created_at: datetime | None = Field(nullable=False, default_factory=datetime.now)
    updated_at: datetime | None = Field(nullable=False, default_factory=datetime.now)

    employees: List["Employee"] = Relationship(back_populates="workplace")
