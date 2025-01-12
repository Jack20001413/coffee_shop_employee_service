from pydantic import BaseModel


class WorkplaceResponseDto(BaseModel):
    id: int | None = None
    name: str
    address: str
