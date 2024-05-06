from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel
from decimal import Decimal

class Marker(SQLModel, table=True):
    marker_id: UUID | None = Field(default=uuid4(), primary_key=True)
    incident_id: UUID 
    direction: str
    latitude: Decimal
    longitude: Decimal
    