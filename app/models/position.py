from datetime import datetime
from typing import List
from sqlmodel import Field, Relationship, SQLModel

# from app.models.employee_position import EmployeePosition
from app.models.job import Job


class Position(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    created_at: datetime = Field(nullable=False)
    updated_at: datetime = Field(nullable=False)

    employee_positions: List["EmployeePosition"] = Relationship(
        back_populates="position"
    )
    job: Job = Relationship(back_populates="position")
