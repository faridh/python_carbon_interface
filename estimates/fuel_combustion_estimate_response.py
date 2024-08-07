"""
Module fuel_combustion_estimate_response
"""

from dataclasses import dataclass
from typing import Any

from model import FuelSourceType, FuelSourceUnit
from .estimate_response import EstimateResponse


@dataclass
class FuelCombustionEstimateResponse(EstimateResponse):
    """
    Class that represents a fuel combustion estimate response from CarbonInterface
    API when creating an EstimateRequest.
    """

    fuel_source_type: FuelSourceType
    fuel_source_unit: FuelSourceUnit
    fuel_source_value: float

    def __init__(self, data: dict[str, Any]):
        super().__init__(data)
        attributes: dict[str, Any] = data.get("attributes")
        self.fuel_source_type: FuelSourceType = FuelSourceType(
            attributes.get("fuel_source_type")
        )
        self.fuel_source_unit: FuelSourceUnit = FuelSourceUnit(
            attributes.get("fuel_source_unit")
        )
        self.fuel_source_value = float(attributes.get("fuel_source_value"))
