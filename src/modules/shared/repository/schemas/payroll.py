from datetime import datetime
from typing import TYPE_CHECKING, List
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .leave import Leave
    from .employee import Employee
    from .job import Job
    from .salary import Salary


class Payroll(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    payday: datetime = Field(nullable=False)
    total_amount: float

    employee_id: int = Field(foreign_key="employee.id", nullable=False)
    employee: "Employee" = Relationship(back_populates="payrolls")

    salary_id: int = Field(foreign_key="salary.id")
    salary: "Salary" = Relationship(back_populates="payrolls")

    job_id: int = Field(foreign_key="job.id")
    job: "Job" = Relationship(back_populates="payrolls")

    leaves: List["Leave"] = Relationship(back_populates="payroll")
