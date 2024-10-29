from datetime import datetime
from typing import List
from sqlmodel import Field, Relationship, SQLModel

from app.models.position import Position


class Job(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str
    salary_range: List[float]
    created_at: datetime = Field(nullable=False)
    updated_at: datetime = Field(nullable=False)

    position_id: int = Field(foreign_key="position.id")
    position: Position = Relationship(back_populates="job")

    job_application_histories: List["JobApplicationHistory"] = Relationship(
        back_populates="job"
    )
    payrolls: List["Payroll"] = Relationship(back_populates="job")
