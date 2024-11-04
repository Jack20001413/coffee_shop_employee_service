from datetime import datetime
from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel


if TYPE_CHECKING:
    from .employee_position import EmployeePosition
    from .job import Job


class Position(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    created_at: datetime = Field(nullable=False)
    updated_at: datetime = Field(nullable=False)

    job_id: int = Field(foreign_key="job.id")
    job: "Job" = Relationship(back_populates="position")

    employee_positions: list["EmployeePosition"] = Relationship(
        back_populates="position"
    )
