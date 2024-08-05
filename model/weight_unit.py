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

    def __json__(self) -> str:
        return self.value
