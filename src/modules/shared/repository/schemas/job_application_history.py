from datetime import date, datetime
from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .employee import Employee
    from .job import Job


class JobApplicationHistory(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    join_date: date
    created_at: datetime = Field(nullable=False)
    updated_at: datetime = Field(nullable=False)

    job_id: int = Field(foreign_key="job.id", nullable=False)
    job: "Job" = Relationship(back_populates="job_application_histories")

    employee_id: int = Field(foreign_key="employee.id", nullable=False)
    employee: "Employee" = Relationship(
        back_populates="job_application_histories"
    )
