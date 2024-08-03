"""
Module cabin_class
"""

from enum import Enum

import json_fix


class CabinClass(Enum):
    """
    CabinClass enum-model to represent valid cabin classes.
    """

    ECONOMY = "economy"
    PREMIUM = "premium"

    def __json__(self) -> str:
        return self.value
