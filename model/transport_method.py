"""
Module transport_method
"""

from enum import Enum

import json_fix


class TransportMethod(Enum):
    """
    TransportMethod enum-model to represent valid transportation methods.
    """

    SHIP = "ship"
    TRAIN = "train"
    TRUCK = "truck"
    PLANE = "plane"

    def __repr__(self):
        return f"TransportMethod('{self.value}')"

    def __str__(self):
        return self.__repr__()

    def __json__(self) -> str:
        return self.value
