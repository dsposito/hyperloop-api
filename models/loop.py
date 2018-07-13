from datetime import datetime
from marshmallow import fields

from models.model import *
from models.pod import PodSchema
from models.station import StationSchema

class Loop():
    def __init__(self, id, pod, origin_station, destination_station, departure_datetime, arrival_datetime, status):
        self.id = id
        self.pod = pod
        self.origin_station = origin_station
        self.destination_station = destination_station
        self.departure_datetime = departure_datetime
        self.arrival_datetime = arrival_datetime
        self.status = status

class LoopStatus(str, ModelEnum):
    SCHEDULED = "scheduled"
    DEPARTING = "departing"
    TRANSITING = "transiting"
    ARRIVING = "arriving"
    COMPLETED = "completed"
    CANCELED = "canceled"

class LoopSchema(ModelSchema):
    id = fields.Int(description="The loop's unique identifier.", example=45671, required=True)
    pod = fields.Nested(PodSchema, description="The pod being transported.", required=True)
    origin_station = fields.Nested(StationSchema, description="The station the pod departs from.", required=True)
    destination_station = fields.Nested(StationSchema, description="The station the pod arrives at.", required=True)
    departure_datetime = fields.DateTime(description="The datetime the pod departs from the origin station.", example="2020-07-16T11:00:00+00:00", required=True)
    arrival_datetime = fields.DateTime(description="The datetime the pod arrives at the destination station.", example="2020-07-16T12:30:00+00:00", required=True)
    status = fields.Str(description="The loop's status.", enum=list(LoopStatus), example=LoopStatus.TRANSITING, required=True)
