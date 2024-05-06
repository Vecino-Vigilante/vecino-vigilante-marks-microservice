from decimal import Decimal


class MarkerModel:
    def __init__(
        self,
        marker_id: str,
        incident_id: str,
        direction: str,
        latitude: Decimal,
        longitude: Decimal,      
    ) -> None:
        self.marker_id = marker_id
        self.incident_id = incident_id
        self.direction = direction
        self.latitude = latitude
        self.longitude = longitude