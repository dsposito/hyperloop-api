from apispec.ext.marshmallow.swagger import schema2jsonschema
import json, yaml

from models.loop import LoopSchema
from models.pod import PodSchema
from models.station import StationSchema
from models.tube import TubeSchema

class OpenAPI():
    # Export each model's schema to YAML for API documentation.
    # Export final YAML spec to JSON for ReDoc documentation UI.
    def buildSpec():
        schemas = {
            "loop": LoopSchema(),
            "pod": PodSchema(),
            "station": StationSchema(),
            "tube": TubeSchema(),
        }

        for name, schema in schemas.items():
            # Convert each schema class to a dictionary.
            content = schema2jsonschema(schema)

            # Convert dictionary to valid JSON string and back again. Without this conversion,
            # YAML output has !!python tags and extra "dictitems" key within "properties".
            content = json.loads(json.dumps(content))

            with open("docs/static/openapi/schemas/" + name + ".yaml", "w") as file:
                yaml.dump(content, file, default_flow_style=False, allow_unicode=True)

        # Export combined YAML to JSON for ReDoc.
        spec = open("docs/static/openapi/spec.yaml", "r")
        with open("docs/static/openapi/spec.json", "w") as f:
            json.dump(yaml.load(spec), f)
