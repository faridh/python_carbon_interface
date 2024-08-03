"""
Module distance_unit
"""

from enum import Enum

import json_fix


class DistanceUnit(Enum):
    """
    DistanceUnit enum-model to represent valid distance units.
    """

    MI = "mi"
    KM = "km"

    def __json__(self) -> str:
        return self.value
