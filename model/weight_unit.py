"""
Module weight_unit
"""

from enum import Enum


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
        return self.value
