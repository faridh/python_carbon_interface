"""
Module fuel_source_type
"""

from enum import Enum


class FuelSourceType(Enum):
    """
    FuelSourceType enum-model to represent valid fuel source types.
    """

    BITUMINOUS_COAL = "bit"
    HOME_HEATING_DIESEL_FUEL = "dfo"
    JET_FUEL = "jf"
    KEROSENE = "ker"
    LIGNITE_COAL = "lig"
    MUNICIPAL_SOLID_WASTE = "msw"
    NATURAL_GAS = "ng"
    PETROLEUM_COKE = "pc"
    PROPANE_GAS = "pg"
    RESIDUAL_FUEL_OIL = "rfo"
    SUBBITUMINOUS_COAL = "sub"
    TIRE_DERIVED_FUEL = "tdf"
    WASTE_OIL = "wo"

    def __repr__(self):
        return f"FuelSourceType('{self.value}')"

    def __str__(self):
        return self.value
