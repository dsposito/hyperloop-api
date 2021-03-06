from datetime import datetime
from flask import Blueprint, jsonify

from models.loop import *
from models.pod import *
from models.station import *
from models.tube import *

api = Blueprint("api", "api", url_prefix="/api")

@api.route("/stations")
def stations():
    schema = StationSchema(many=True)
    stations = schema.dump([
        Station(1, StationType.PUBLIC, "HAW", 33.920659, -118.328278, StationStatus.ACTIVE),
        Station(1900, StationType.PUBLIC, "FRE", 37.492509, -121.944616, StationStatus.INACTIVE),
        Station(6800, StationType.PRIVATE, "EMD", 35.671724, -97.508266, StationStatus.ACTIVE),
    ])

    return jsonify(stations.data)

@api.route("/stations/<int:id>")
def station(id):
    schema = StationSchema()
    station = schema.dump(
        Station(id, StationType.PUBLIC, "HAW", 33.920659, -118.328278, StationStatus.ACTIVE),
    )

    return jsonify(station.data)

@api.route("/tubes")
def tubes():
    schema = TubeSchema(many=True)
    tubes = schema.dump([
        Tube(15, TubeType.TUNNEL, "CA", TubeDirection.NORTH, 1, TubeStatus.ACTIVE),
        Tube(35, TubeType.TUNNEL, "WA", TubeDirection.SOUTH, 1, TubeStatus.INACTIVE),
        Tube(85, TubeType.ELEVATED, "CA", TubeDirection.WEST, 2, TubeStatus.ACTIVE),
    ])

    return jsonify(tubes.data)

@api.route("/tubes/<int:id>")
def tube(id):
    schema = TubeSchema()
    tube = schema.dump(
        Tube(id, TubeType.TUNNEL, "CA", TubeDirection.NORTH, 1000, TubeStatus.ACTIVE)
    )

    return jsonify(tube.data)

@api.route("/pods")
def pods():
    schema = PodSchema(many=True)
    pods = schema.dump([
        Pod(2000, PodType.PASSENGER, PodStatus.ACTIVE),
        Pod(3005, PodType.CARGO, PodStatus.ACTIVE),
        Pod(6010, PodType.VEHICLE, PodStatus.INACTIVE),
    ])

    return jsonify(pods.data)

@api.route("/pods/<int:id>")
def pod(id):
    schema = PodSchema()
    pod = schema.dump(
        Pod(id, PodType.PASSENGER, PodStatus.ACTIVE),
    )

    return jsonify(pod.data)

@api.route("/loops")
def loops():
    schema = LoopSchema(many=True)
    loops = schema.dump([
        Loop(
            45671,
            Pod(2000, PodType.PASSENGER, PodStatus.ACTIVE),
            Station(1, StationType.PUBLIC, "HAW", 33.920659, -118.328278, StationStatus.ACTIVE),
            Station(1900, StationType.PUBLIC, "FRE", 37.492509, -121.944616, StationStatus.ACTIVE),
            datetime.strptime('January 1 2020 11:00AM', '%B %d %Y %I:%M%p'),
            datetime.strptime('January 1 2020 11:30AM', '%B %d %Y %I:%M%p'),
            LoopStatus.TRANSITING
        ),
        Loop(
            45865,
            Pod(3005, PodType.CARGO, PodStatus.ACTIVE),
            Station(1, StationType.PUBLIC, "HAW", 33.920659, -118.328278, StationStatus.ACTIVE),
            Station(6800, StationType.PRIVATE, "EMD", 35.671724, -97.508266, StationStatus.ACTIVE),
            datetime.strptime('July 16 2020 11:00AM', '%B %d %Y %I:%M%p'),
            datetime.strptime('July 16 2020 12:30PM', '%B %d %Y %I:%M%p'),
            LoopStatus.DEPARTING
        ),
        Loop(
            45890,
            Pod(2000, PodType.PASSENGER, PodStatus.ACTIVE),
            Station(1900, StationType.PUBLIC, "FRE", 37.492509, -121.944616, StationStatus.ACTIVE),
            Station(1, StationType.PUBLIC, "HAW", 33.920659, -118.328278, StationStatus.ACTIVE),
            datetime.strptime('December 4 2020 2:00PM', '%B %d %Y %I:%M%p'),
            datetime.strptime('December 4 2020 2:30PM', '%B %d %Y %I:%M%p'),
            LoopStatus.COMPLETED
        ),
    ])

    return jsonify(loops.data)

@api.route("/loops/<int:id>")
def loop(id):
    schema = LoopSchema()
    loop = schema.dump(
        Loop(
            id,
            Pod(2000, PodType.PASSENGER, PodStatus.ACTIVE),
            Station(1, StationType.PUBLIC, "HAW", 33.920659, -118.328278, StationStatus.ACTIVE),
            Station(1900, StationType.PUBLIC, "FRE", 37.492509, -121.944616, StationStatus.ACTIVE),
            datetime.strptime('January 1 2020 11:00AM', '%B %d %Y %I:%M%p'),
            datetime.strptime('January 1 2020 11:30AM', '%B %d %Y %I:%M%p'),
            LoopStatus.TRANSITING
        )
    )

    return jsonify(loop.data)
