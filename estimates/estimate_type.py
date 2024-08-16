"""
Module estimate_type
"""

from enum import Enum


class EstimateType(Enum):
    """
    Represents an enum-model with the different types of valida estimations.
    """

    ELECTRICITY = "electricity"
    FLIGHT = "flight"
    SHIPPING = "shipping"
    VEHICLE = "vehicle"
    FUEL_COMBUSTION = "fuel_combustion"

    def __repr__(self) -> str:
        return f"EstimateType('{self.value}')"

    def __str__(self) -> str:
        return self.value
