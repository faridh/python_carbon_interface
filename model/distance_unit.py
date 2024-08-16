"""
Module distance_unit
"""

from enum import Enum


class DistanceUnit(Enum):
    """
    DistanceUnit enum-model to represent valid distance units.
    """

    MI = "mi"
    KM = "km"

    def __repr__(self):
        return f"DistanceUnit('{self.value}')"

    def __str__(self):
        return self.value
