from datetime import datetime
from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy.orm import RelationshipProperty


if TYPE_CHECKING:
    from .employee_position import EmployeePosition
    from .job import Job


class Position(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    created_at: datetime = Field(nullable=False)
    updated_at: datetime = Field(nullable=False)

    # This is how SQLModel accept the way it configures one-to-one relationship
    job: "Job" = Relationship(
        sa_relationship=RelationshipProperty(
            "Job", back_populates="position", uselist=False
        )
    )

    employee_positions: list["EmployeePosition"] = Relationship(
        back_populates="position"
    )
