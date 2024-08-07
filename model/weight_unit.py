"""
Module weight_unit
"""

from enum import Enum

import json_fix


class WeightUnit(Enum):
    """
    WeightUnit enum-model to represent valid weight units.
    """

    GRAMS = "g"
    POUNDS = "lb"
    KILOGRAMS = "kg"
    TONNES = "mt"

    def __repr__(self):
        return f"WeightUnit('{self.value}')"

    def __str__(self):
        return self.__repr__()

    def __json__(self) -> str:
        return self.value
