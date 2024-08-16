"""
Module cabin_class
"""

from enum import Enum


class CabinClass(Enum):
    """
    CabinClass enum-model to represent valid cabin classes.
    """

    ECONOMY = "economy"
    PREMIUM = "premium"

    def __repr__(self):
        return f"CabinClass('{self.value}')"

    def __str__(self):
        return self.value
