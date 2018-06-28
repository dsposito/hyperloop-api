from apispec import APISpec
from flask import Flask, jsonify, render_template
from models.tube import *

import json

app = Flask(__name__, template_folder='docs')

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


@app.route("/")
@app.route("/docs")
def home():
    return render_template("index.html")

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


# Register paths.
with app.test_request_context():
    spec.add_path(view=tubes)

# We're good to go! Save this to a file for now.
with open('static/apispec.json', 'w') as f:
    json.dump(spec.to_dict(), f)
