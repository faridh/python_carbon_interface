"""
Module fuel_combustion_estimate_request
"""

from model import FuelSourceType, FuelSourceUnit

from .estimate_request import EstimateRequest
from .estimate_type import EstimateType


class FuelCombustionEstimateRequest(EstimateRequest):
    """
    Class that represent the body of the request against the '/estimates'
    endpoint
    """

    fuel_source_type: FuelSourceType
    fuel_source_unit: FuelSourceUnit
    fuel_source_value: float

    def __init__(
        self,
        fuel_source_type: FuelSourceType,
        fuel_source_unit: FuelSourceUnit,
        fuel_source_value: float,
    ):
        super().__init__(EstimateType.FUEL_COMBUSTION)
        self.fuel_source_type = fuel_source_type
        self.fuel_source_unit = fuel_source_unit
        self.fuel_source_value = fuel_source_value
