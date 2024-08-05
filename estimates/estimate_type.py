"""
Module estimate_type
"""

from enum import Enum

import json_fix


class EstimateType(Enum):
    """
    Represents an enum-model with the different types of valida estimations.
    """

    ELECTRICITY = "electricity"
    FLIGHT = "flight"
    SHIPPING = "shipping"

    def __json__(self) -> str:
        return self.name.lower()
