from marshmallow import Schema, fields
from models.model import ModelEnum

class Tube():
    def __init__(self, id, name, type, status):
        self.id = id
        self.name = name
        self.type = type
        self.status = status

class TubeType(str, ModelEnum):
    ELEVATED = "elevated"
    TUNNEL = "tunnel"

class TubeStatus(str, ModelEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class TubeSchema(Schema):
    id = fields.Int(description="The tube's unique identifier.", example=35, required=True)
    name = fields.Str(description="The tube's name.", example="CA-NT1", required=True)
    type = fields.Str(description="The tube's type.", enum=list(TubeType), example=TubeType.TUNNEL, required=True)
    status = fields.Str(description="The tube's status.", enum=list(TubeStatus), example=TubeStatus.ACTIVE, required=True)
