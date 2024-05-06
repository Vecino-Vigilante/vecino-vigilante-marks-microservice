from decimal import Decimal
from uuid import UUID
from pydantic import BaseModel


class MarkerRequestDTO(BaseModel):
    incident_id: UUID
    direction: str
    latitude: Decimal
    longitude: Decimal 