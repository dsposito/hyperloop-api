from enum import Enum
from marshmallow import Schema

class ModelEnum(Enum):
    def __str__(self):
        return str(self.value)

class ModelSchema(Schema):
    pass

    # Order serialization output according to the order in which schema fields were declared.
    # http://marshmallow.readthedocs.io/en/latest/api_reference.html#marshmallow.Schema.Meta
    class Meta:
        ordered = True
