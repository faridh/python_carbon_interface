"""
Module electricity_unit
"""

from enum import Enum

import json_fix


class ElectricityUnit(Enum):
    """
    ElectricityUnit enum-model to represent valid electricity units.
    """

    MWH = "mwh"
    KWH = "kwh"

    def __repr__(self):
        return f"ElectricityUnit('{self.value}')"

    def __str__(self):
        return self.__repr__()

    def __json__(self) -> str:
        return self.value
