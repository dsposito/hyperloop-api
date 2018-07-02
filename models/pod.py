from marshmallow import Schema, fields
from models.model import ModelEnum

import random, string

class Pod():
    def __init__(self, id, type, status, max_speed=None, max_weight=None):
        self.id = id
        self.type = type
        self.status = status
        self.max_speed = self.getMaxSpeed() if max_speed is None else max_speed
        self.max_weight = self.getMaxWeight() if max_weight is None else max_weight
        self.name = self.getName()

    def getMaxSpeed(self):
        if (self.isCargo() or self.isVehicle()):
            return 760
        else:
            return 700

    def getMaxWeight(self):
        if (self.isCargo() or self.isVehicle()):
            # 2 vehicles @ 5000lbs each
            return 10000
        else:
            # 12 passengers @ 250lbs each
            return 3000

    def getName(self):
        type = self.type.capitalize()[:1]
        id_alpha = "".join(random.choices(string.ascii_uppercase, k=1))
        id_numeric = "".join(random.choices(string.digits, k=4))

        return "%s%s-%s" % (type, id_alpha, id_numeric)

    def isCargo(self):
        return self.type == PodType.CARGO

    def isPassenger(self):
        return self.type == PodType.PASSENGER

    def isVehicle(self):
        return self.type == PodType.VEHICLE

class PodType(str, ModelEnum):
    CARGO = "cargo"
    PASSENGER = "passenger"
    VEHICLE = "vehicle"

class PodStatus(str, ModelEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class PodSchema(Schema):
    id = fields.Int(description="The pod's unique identifier.", example=4597, required=True)
    type = fields.Str(description="The pod's type.", example=PodType.PASSENGER, required=True)
    status = fields.Str(description="The pod's status.", example=PodStatus.ACTIVE, required=True)
    max_speed = fields.Int(description="The max speed the pod can travel at.", example=700, validate=lambda w: 1 <= w <= 760, required=True)
    max_weight = fields.Int(description="The max weight the pod can carry.", example=3000, validate=lambda w: 1 <= w <= 10000, required=True)
    name = fields.Str(description="The pod's memorable name.", example="CA-1440", required=True)
