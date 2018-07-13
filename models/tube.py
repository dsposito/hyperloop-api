from marshmallow import fields

from models.model import *

class Tube():
    def __init__(self, id, type, region, direction, elevation, status):
        self.id = id
        self.type = type
        self.region = region
        self.direction = direction
        self.elevation = elevation
        self.status = status
        self.name = self.getName()

    def getName(self) -> str:
        region = self.region
        direction = self.direction.capitalize()[:1]
        type = self.type.capitalize()[:1]
        elevation = self.elevation

        return "%s-%s%s%d" % (region, direction, type, elevation)

class TubeType(str, ModelEnum):
    ELEVATED = "elevated"
    TUNNEL = "tunnel"

class TubeDirection(str, ModelEnum):
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"

class TubeStatus(str, ModelEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class TubeSchema(ModelSchema):
    id = fields.Int(description="The tube's unique identifier.", example=35, required=True)
    type = fields.Str(description="The tube's type.", enum=list(TubeType), example=TubeType.TUNNEL, required=True)
    region = fields.Str(description="The tube's region (state or county).", example="CA", required=True)
    direction = fields.Str(description="The tube's primary direction.", enum=list(TubeDirection), example="north", required=True)
    elevation = fields.Int(description="The tube's elevation.", example=1, validate=lambda e: 1 <= e <= 100, required=True)
    status = fields.Str(description="The tube's status.", enum=list(TubeStatus), example=TubeStatus.ACTIVE, required=True)
    name = fields.Str(description="The tube's memorable name.", example="CA-NT1", required=True)
