from marshmallow import Schema, fields
from models.model import ModelEnum

class Station():
    def __init__(self, id, type, region, latitude, longitude, status):
        self.id = id
        self.type = type
        self.region = region
        self.latitude = latitude
        self.longitude = longitude
        self.status = status
        self.name = self.getName()

    def getName(self):
        region = self.region
        type = self.type.upper()[:3]
        latitude = int(abs(self.latitude))
        longitude = int(abs(self.longitude))

        return "%s-%s%d%d" % (region, type, latitude, longitude)

class StationType(str, ModelEnum):
    PUBLIC = "public"
    PRIVATE = "private"

class StationStatus(str, ModelEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class StationSchema(Schema):
    id = fields.Int(description="The station's unique identifier.", example=1, required=True)
    type = fields.Str(description="The station's type.", enum=list(StationType), example=StationType.PUBLIC, required=True)
    region = fields.Str(description="The station's region (city).", example="HAW", required=True)
    latitude = fields.Float(description="The station's latitude location measurement.", example=33.920659, validate=lambda p: -90 <= p <= 90, required=True)
    longitude = fields.Float(description="The station's longitude location measurement.", example=-118.328278, validate=lambda p: -180 <= p <= 180, required=True)
    status = fields.Str(description="The station's status.", enum=list(StationStatus), example=StationStatus.ACTIVE, required=True)
    name = fields.Str(description="The station's memorable name.", example="LA-PUB33118", required=True)
