"""
Module shipping_estimate_request
"""

from typing import Any

import json_fix

from model import DistanceUnit, TransportMethod, WeightUnit

from .estimate_request import EstimateRequest
from .estimate_type import EstimateType


class ShippingEstimateRequest(EstimateRequest):
    """
    Class that represent the body of the request against the '/estimates'
    endpoint
    """

    weight_unit: WeightUnit
    weight_value: float
    distance_unit: DistanceUnit
    distance_value: float
    transport_method: TransportMethod

    def __init__(
        self,
        weight_unit: WeightUnit,
        weight_value: float,
        distance_unit: DistanceUnit,
        distance_value: float,
        transport_method: TransportMethod,
    ):
        super().__init__(EstimateType.SHIPPING)
        self.weight_unit = weight_unit
        self.weight_value = weight_value
        self.distance_unit = distance_unit
        self.distance_value = distance_value
        self.transport_method = transport_method

    def __json__(self) -> dict[str, Any]:
        return {k: v for k, v in self.__dict__.items() if v is not None}
