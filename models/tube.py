from enum import Enum
from marshmallow import Schema, fields

class Tube():
    def __init__(self, id, name, type, status):
        self.id = id
        self.name = name
        self.type = type
        self.status = status

class TubeType(str, Enum):
    ELEVATED = "elevated"
    TUNNEL = "tunnel"

    def __str__(self):
        return str(self.value)

class TubeStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

    def __str__(self):
        return str(self.value)

class TubeSchema(Schema):
    id = fields.Int(description="The tube's unique identifier.", example=35, required=True)
    name = fields.Str(description="The tube's name.", example="CA-NT1", required=True)
    type = fields.Str(description="The tube's type.", enum=list(TubeType), example=TubeType.TUNNEL, required=True)
    status = fields.Str(description="The tube's status.", enum=list(TubeStatus), example=TubeStatus.ACTIVE, required=True)
