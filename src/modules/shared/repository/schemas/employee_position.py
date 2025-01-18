from datetime import datetime
from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel


if TYPE_CHECKING:
    from .employee import Employee
    from .position import Position


class EmployeePosition(SQLModel, table=True):
    employee_id: int | None = Field(
        default=None, primary_key=True, foreign_key="employee.id"
    )
    position_id: int = Field(default=None, primary_key=True, foreign_key="position.id")
    start_date: datetime = Field(nullable=False)
    end_date: datetime = Field(nullable=False)

    employee: "Employee" = Relationship(back_populates="employee_positions")
    position: "Position" = Relationship(back_populates="employee_positions")
