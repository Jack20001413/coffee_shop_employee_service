from datetime import datetime
from typing import TYPE_CHECKING, List
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .payroll import Payroll


class Salary(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    amount: float
    bonus: float
    created_at: datetime = Field(nullable=False)
    updated_at: datetime = Field(nullable=False)

    payrolls: List["Payroll"] = Relationship(back_populates="salary")
