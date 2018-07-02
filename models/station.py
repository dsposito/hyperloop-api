from marshmallow import Schema, fields
from models.model import ModelEnum

class Station():
    def __init__(self, id, type, status, latitude, longitude):
        self.id = id
        self.type = type
        self.status = status
        self.latitude = latitude
        self.longitude = longitude

class StationType(str, ModelEnum):
    PUBLIC = "public"
    PRIVATE = "private"

class StationStatus(str, ModelEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class StationSchema(Schema):
    id = fields.Int(description="The station's unique identifier.", example=1, required=True)
    type = fields.Str(description="The station's type.", example=StationType.PUBLIC, required=True)
    status = fields.Str(description="The station's status.", example=StationStatus.ACTIVE, required=True)
    latitude = fields.Float(description="The station's latitude location measurement.", example=33.920659, validate=lambda p: -90 <= p <= 90, required=True)
    longitude = fields.Float(description="The station's longitude location measurement.", example=-118.328278, validate=lambda p: -180 <= p <= 180, required=True)
