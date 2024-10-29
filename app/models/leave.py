from datetime import date, datetime
from sqlmodel import Field, Relationship, SQLModel

from app.models.employee import Employee
from app.models.payroll import Payroll


class Leave(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    reason: str = Field(nullable=True)
    leave_date: date = Field(nullable=False)
    created_at: datetime = Field(nullable=False)
    updated_at: datetime = Field(nullable=False)

    employee_id: int = Field(foreign_key="employee.id")
    employee: Employee = Relationship(back_populates="leaves")

    # TODO: Re-evaluate the relationship between Leave and Payroll
    payroll_id: int = Field(foreign_key="payroll.id")
    payroll: Payroll = Relationship(back_populates="leaves")
