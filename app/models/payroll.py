from datetime import datetime
from typing import List
from sqlmodel import Field, Relationship, SQLModel

from app.models.employee import Employee
from app.models.job import Job
# from app.models.leave import Leave
from app.models.salary import Salary


class Payroll(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    payday: datetime = Field(nullable=False)
    total_amount: float

    employee_id: int = Field(foreign_key="employee.id")
    employee: Employee = Relationship(back_populates="payrolls")

    salary_id: int = Field(foreign_key="salary.id")
    salary: Salary = Relationship(back_populates="payrolls")

    job_id: int = Field(foreign_key="job.id")
    job: Job = Relationship(back_populates="payrolls")

    leaves: List["Leave"] = Relationship(back_populates="payroll")
