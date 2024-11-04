from datetime import date, datetime
from typing import TYPE_CHECKING, List
from sqlmodel import Field, Relationship, SQLModel
# from app.models.workplace import Workplace

# if TYPE_CHECKING:
#     from .workplace import Workplace
#     from app.models.employee_position import EmployeePosition
#     # from app.models.position import Position
#     from app.models.leave import Leave
#     from app.models.payroll import Payroll
#     from app.models.job_application_history import JobApplicationHistory


class Employee(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    gender: str
    date_of_birth: date = Field(nullable=False)
    contact_address: str
    phone_number: str
    created_at: datetime = Field(nullable=False, default_factory=datetime.now)
    updated_at: datetime = Field(nullable=False, default_factory=datetime.now)

    workplace_id: int = Field(foreign_key="workplace.id")
    workplace: "Workplace" = Relationship(back_populates="employees")

    # positions: List["Position"] = Relationship(
    #     back_populates="employees", link_model=EmployeePosition
    # )
    # employee_positions: list["EmployeePosition"] = Relationship(
    #     back_populates="employee"
    # )
    # leaves: List["Leave"] = Relationship(back_populates="employee")
    # payrolls: List["Payroll"] = Relationship(back_populates="employee")
    # job_application_histories: List["JobApplicationHistory"] = Relationship(
    #     back_populates="employee"
    # )
