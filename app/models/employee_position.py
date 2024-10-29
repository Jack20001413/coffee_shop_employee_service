from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel

from app.models.employee import Employee
from app.models.position import Position


class EmployeePosition(SQLModel, table=True):
    employee_id: int | None = Field(
        default=None, primary_key=True, foreign_key="employee.id"
    )
    position_id: int = Field(
        default=None, primary_key=True, foreign_key="position.id"
    )
    start_date: datetime = Field(nullable=False)
    end_date: datetime = Field(nullable=False)

    employee: Employee = Relationship(back_populates="employee_positions")
    position: Position = Relationship(back_populates="employee_positions")
