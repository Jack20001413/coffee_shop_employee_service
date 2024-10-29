from datetime import datetime
from typing import List
from sqlmodel import Field, Relationship, SQLModel

# from app.models.payroll import Payroll


class Salary(SQLModel, table=True):
    int: id | None = Field(default=None, primary_key=True)
    amount: float
    bonus: float
    created_at: datetime = Field(nullable=False)
    updated_at: datetime = Field(nullable=False)

    payrolls: List["Payroll"] = Relationship(back_populates="salary")
