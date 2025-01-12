from datetime import datetime
import fastapi
import sqlalchemy.exc
import sqlmodel

from typing import Annotated, List
from workplace.repository.model import Workplace
from workplace.dtos.workplace_response import WorkplaceResponseDto
from workplace.repository import context as db_context
from shared.utils.logger import logger


router = fastapi.APIRouter(prefix="/workplaces", tags=["workplace"])
DBSession = Annotated[sqlmodel.Session, fastapi.Depends(db_context.get_session)]


@router.get(
    "/",
    status_code=fastapi.status.HTTP_200_OK,
    response_model=List[WorkplaceResponseDto],
)
def list_workplaces(session: DBSession) -> List[WorkplaceResponseDto]:
    return session.exec(sqlmodel.select(Workplace)).all()


@router.get(
    "/{workplace_id}",
    status_code=fastapi.status.HTTP_200_OK,
    response_model=WorkplaceResponseDto,
)
def get_workplace(workplace_id: int, session: DBSession) -> WorkplaceResponseDto:
    workplace = _get_workplace_by_id(workplace_id, session)
    if workplace is None:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_404_NOT_FOUND,
            detail=f"Workplace with ID {workplace_id} not found",
        )
    return workplace


@router.post(
    "/",
    status_code=fastapi.status.HTTP_201_CREATED,
    response_model=WorkplaceResponseDto,
)
def create_workplace(workplace: Workplace, session: DBSession) -> WorkplaceResponseDto:
    session.add(workplace)
    session.commit()
    session.refresh(workplace)

    return workplace


@router.patch("/{workplace_id}", status_code=fastapi.status.HTTP_204_NO_CONTENT)
def update_workplace(
    workplace_id: int, workplace: Workplace, session: DBSession
) -> None:
    current_workplace = _get_workplace_by_id(workplace_id, session)

    if current_workplace is None:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_404_NOT_FOUND,
            detail=f"Workplace with ID {workplace_id} not found",
        )

    current_workplace.name = (
        workplace.name if workplace.name else current_workplace.name
    )
    current_workplace.address = (
        workplace.address if workplace.address else current_workplace.address
    )
    if workplace.name and workplace.address:
        current_workplace.updated_at = datetime.now()

    session.add(current_workplace)
    session.commit()


@router.delete("/{workplace_id}", status_code=fastapi.status.HTTP_204_NO_CONTENT)
def delete_workplace(workplace_id: int, session: DBSession) -> None:
    try:
        current_workplace = session.exec(
            sqlmodel.select(Workplace).where(Workplace.id == workplace_id)
        ).one()

        session.delete(current_workplace)
    except sqlalchemy.exc.NoResultFound as e:
        logger.exception(e)
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_404_NOT_FOUND,
            detail=f"Workplace with ID {workplace_id} not found",
        )
    finally:
        session.commit()


def _get_workplace_by_id(workplace_id: int, session: DBSession) -> Workplace | None:
    return session.exec(
        sqlmodel.select(Workplace).where(Workplace.id == workplace_id)
    ).first()
