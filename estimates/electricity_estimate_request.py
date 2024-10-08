"""
Module electricity_estimate_request
"""

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
        country: Country,
        electricity_value: float,
        electricity_unit: ElectricityUnit = ElectricityUnit.MWH,
        state: str | None = None,
    ):
        super().__init__(EstimateType.ELECTRICITY)
        self.electricity_unit = electricity_unit
        self.electricity_value = electricity_value
        self.country = country
        self.state = state
