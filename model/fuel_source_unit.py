"""
Module fuel_source_unit
"""

from enum import Enum


class FuelSourceUnit(Enum):
    """
    FuelSourceUnit enum-model to represent valid fuel units.
    """

    SHORT_TON = "short_ton"
    GALLON = "gallon"
    THOUSAND_CUBIC_FEET = "thousand_cubic_feet"
    BARREL = "barrel"
    BTU = "btu"

    def __repr__(self):
        return f"FuelSourceUnit('{self.value}')"

    def __str__(self):
        return self.value
