from datetime import datetime
from uuid import UUID
from sqlmodel import SQLModel


class Employee(SQLModel, table=True):
    name: str
    employee_id: UUID | None = None
    sex: str = "male"
    base_salary: float
    date_of_birth: datetime | None = None
