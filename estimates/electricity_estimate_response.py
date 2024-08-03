"""
Module electricity_estimate_response
"""

from dataclasses import dataclass
from typing import Any

from model import Country, ElectricityUnit

from .estimate_response import EstimateResponse


@dataclass
class ElectricEstimateResponse(EstimateResponse):
    """
    Class that represents an electricity estimate response from Carbon Interface API when
    creating an EstimateRequest.
    """

    country: Country
    state: str
    electricity_unit: ElectricityUnit
    electricity_value: float

    def __init__(self, data: dict[str, Any]):
        super().__init__(data)
        attributes: dict[str, Any] = data.get("attributes")
        self.country: Country = Country.from_value(attributes.get("country"))
        self.state: str = attributes.get("state")
        self.electricity_unit: ElectricityUnit = ElectricityUnit(
            attributes.get("electricity_unit")
        )
        self.electricity_value: float = float(attributes.get("electricity_value"))
