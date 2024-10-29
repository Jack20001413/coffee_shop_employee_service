from datetime import datetime
from typing import List
from sqlmodel import Field, Relationship, SQLModel


class Workplace(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    address: str
    created_at: datetime = Field(nullable=False)
    updated_at: datetime = Field(nullable=False)

    employees: List["Employee"] = Relationship(back_populates="workplace")
