from enum import Enum
from marshmallow import Schema, fields

class Tube():
    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type

class TubeSchema(Schema):
    id = fields.Int(required=True, example=35)
    name = fields.Str(required=True, example='CA-NT1')
    type = fields.Str(required=True, example='tunnel')

class TubeType(Enum):
    ELEVATED = "elevated"
    TUNNEL = "tunnel"

    def __str__(self):
        return str(self.value)
