"""
Module electricity_estimate_request
"""

from typing import Any

import json_fix

from model import Country, ElectricityUnit

from .estimate_request import EstimateRequest
from .estimate_type import EstimateType


class ElectricityEstimateRequest(EstimateRequest):
    """
    Class that represent the body of the request against the '/estimates'
    endpoint
    """

    electricity_unit: ElectricityUnit
    electricity_value: float
    country: Country
    state: str | None

    def __init__(
        self,
        electricity_unit: ElectricityUnit,
        electricity_value: float,
        country: Country,
        state: str | None = "",
    ):
        super().__init__(EstimateType.ELECTRICITY)
        self.electricity_unit = electricity_unit
        self.electricity_value = electricity_value
        self.country = country
        self.state = state

    def __json__(self) -> dict[str, Any]:
        return self.__dict__
