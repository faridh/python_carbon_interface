"""
Module fuel_unit
"""

from enum import Enum

import json_fix


class FuelUnit(Enum):
    """
    FuelUnit enum-model to represent valid fuel units.
    """

    SHORT_TON = "short_ton"
    GALLON = "gallon"
    THOUSAND_CUBIC_FEET = "thousand_cubic_feet"
    BARREL = "barrel"
    BTU = "btu"

    def __repr__(self):
        return f"FuelUnit('{self.value}')"

    def __str__(self):
        return self.__repr__()

    def __json__(self) -> str:
        return self.value
