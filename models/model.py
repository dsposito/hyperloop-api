from enum import Enum

class ModelEnum(Enum):
    def __str__(self):
        return str(self.value)
