from datetime import date, datetime
from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .employee import Employee
    from .payroll import Payroll


class Leave(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    reason: str = Field(nullable=True)
    leave_date: date = Field(nullable=False)
    created_at: datetime = Field(nullable=False)
    updated_at: datetime = Field(nullable=False)

    employee_id: int = Field(foreign_key="employee.id")
    employee: "Employee" = Relationship(back_populates="leaves")

    payroll_id: int = Field(foreign_key="payroll.id")
    payroll: "Payroll" = Relationship(back_populates="leaves")
