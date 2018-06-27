from enum import Enum
from marshmallow import Schema, fields

class Tube():
    def __init__(self, id, name, type, status):
        self.id = id
        self.name = name
        self.type = type
        self.status = status

class TubeSchema(Schema):
    id = fields.Int(required=True, example=35)
    name = fields.Str(required=True, example='CA-NT1')
    type = fields.Str(required=True, example='tunnel')
    status = fields.Str(required=True, example='active')

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
