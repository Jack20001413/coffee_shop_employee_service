from datetime import datetime
from typing import TYPE_CHECKING, List
from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy.orm import RelationshipProperty

if TYPE_CHECKING:
    from .position import Position
    from .job_application_history import JobApplicationHistory
    from .payroll import Payroll


class Job(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str
    salary_range: str
    created_at: datetime = Field(nullable=False)
    updated_at: datetime = Field(nullable=False)

    position_id: int = Field(foreign_key="position.id", nullable=False)
    # This is how SQLModel accept the way it configures one-to-one relationship
    # Ref: https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#one-to-one
    # Ref: https://github.com/fastapi/sqlmodel/issues/132#issuecomment-945725885
    position: "Position" = Relationship(
        sa_relationship=RelationshipProperty(
            "Position", back_populates="job", uselist=False
        )
    )

    job_application_histories: List["JobApplicationHistory"] = Relationship(
        back_populates="job"
    )
    payrolls: List["Payroll"] = Relationship(back_populates="job")
