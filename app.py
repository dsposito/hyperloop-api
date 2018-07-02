from apispec import APISpec
from flask import Flask, jsonify, redirect, url_for
import json

from docs.docs import docs
from models.pod import *
from models.station import *
from models.tube import *

# Boot the application and its components.
app = Flask(__name__)
app.register_blueprint(docs)


# Create an APISpec
spec = APISpec(
    title='Hyperloop API Documentation',
    info=dict(
        description='API documentation for the future of mobility.'
    ),
    version='1.0.0',
    plugins=[
        'apispec.ext.flask',
        'apispec.ext.marshmallow',
    ],
)

@app.route('/')
def index():
    return redirect(url_for('docs.index'))

@app.route("/api/stations")
def stations():
    """
    ---
    get:
        summary: Stations
        description: Get a list of stations.
        responses:
            200:
                description: List of stations
                schema:
                    type: array
                    items: StationSchema
    """
    schema = StationSchema(many=True)
    stations = schema.dump([
        Station(1, StationType.PUBLIC, "HAW", 33.920659, -118.328278, StationStatus.ACTIVE),
        Station(1900, StationType.PUBLIC, "FRE", 37.492509, -121.944616, StationStatus.INACTIVE),
        Station(6800, StationType.PRIVATE, "EMD", 35.671724, -97.508266, StationStatus.ACTIVE)
    ])

    return jsonify(stations.data)

@app.route("/api/stations/<int:id>")
def station(id):
    """
    ---
    get:
        summary: Station
        description: Get a specific station.
        responses:
            200:
                description: A station
                schema: StationSchema
            404:
                description: Station not found
        parameters:
          - name: id
            in: path
            description: ID of the station to get
            required: true
            type: integer
            format: int32
    """
    schema = StationSchema()
    station = schema.dump(
        Station(id, StationType.PUBLIC, "HAW", 33.920659, -118.328278, StationStatus.ACTIVE),
    )

    return jsonify(station.data)

@app.route("/api/pods")
def pods():
    """
    ---
    get:
        summary: Pods
        description: Get a list of pods.
        responses:
            200:
                description: List of pods
                schema:
                    type: array
                    items: PodSchema
    """
    schema = PodSchema(many=True)
    pods = schema.dump([
        Pod(2000, PodType.PASSENGER, PodStatus.ACTIVE),
        Pod(3005, PodType.CARGO, PodStatus.ACTIVE),
    ])

    return jsonify(pods.data)

@app.route("/api/pods/<int:id>")
def pod(id):
    """
    ---
    get:
        summary: Pod
        description: Get a specific pod.
        responses:
            200:
                description: A pod
                schema: PodSchema
            404:
                description: Pod not found
        parameters:
          - name: id
            in: path
            description: ID of the pod to get
            required: true
            type: integer
            format: int32
    """
    schema = PodSchema()
    pod = schema.dump(
        Pod(id, PodType.PASSENGER, PodStatus.ACTIVE),
    )

    return jsonify(pod.data)

@app.route("/api/tubes")
def tubes():
    """
    ---
    get:
        summary: Tubes
        description: Get a list of tubes.
        responses:
            200:
                description: List of tubes
                schema:
                    type: array
                    items: TubeSchema
    """
    schema = TubeSchema(many=True)
    tubes = schema.dump([
        Tube(15, 'CA-NT1', TubeType.TUNNEL, TubeStatus.ACTIVE),
        Tube(35, 'CA-ST1', TubeType.TUNNEL, TubeStatus.INACTIVE),
        Tube(85, 'CA-NE2', TubeType.ELEVATED, TubeStatus.ACTIVE)
    ])

    return jsonify(tubes.data)

@app.route("/api/tubes/<int:id>")
def tube(id):
    """
    ---
    get:
        summary: Tube
        description: Get a specific tube.
        responses:
            200:
                description: A tube
                schema: TubeSchema
            404:
                description: Tube not found
        parameters:
          - name: id
            in: path
            description: ID of the tube to get
            required: true
            type: integer
            format: int32
    """
    schema = TubeSchema()
    tube = schema.dump(
        Tube(id, 'CA-NT1', TubeType.TUNNEL, TubeStatus.ACTIVE)
    )

    return jsonify(tube.data)


# Register paths.
with app.test_request_context():
    spec.add_path(view=stations)
    spec.add_path(view=station)
    spec.add_path(view=tubes)
    spec.add_path(view=tube)
    spec.add_path(view=pods)
    spec.add_path(view=pod)

# We're good to go! Save this to a file for now.
with open('docs/static/apispec.json', 'w') as f:
    json.dump(spec.to_dict(), f)
