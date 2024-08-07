"""
Module shipping_estimate_response
"""

from dataclasses import dataclass
from typing import Any

from model import DistanceUnit, TransportMethod, WeightUnit

from .estimate_response import EstimateResponse


@dataclass
class ShippingEstimateResponse(EstimateResponse):
    """
    Class that represents a shipping estimate response from CarbonInterface API when
    creating an EstimateRequest.
    """

    distance_unit: DistanceUnit
    distance_value: float
    weight_unit: WeightUnit
    weight_value: float
    transport_method: TransportMethod

    def __init__(self, data: dict[str, Any]):
        super().__init__(data)
        attributes: dict[str, Any] = data.get("attributes")
        self.distance_unit: DistanceUnit = DistanceUnit(attributes.get("distance_unit"))
        self.distance_value: float = float(attributes.get("distance_value"))
        self.weight_unit: WeightUnit = WeightUnit(attributes.get("weight_unit"))
        self.weight_value: float = float(attributes.get("weight_value"))
        self.transport_method: TransportMethod = TransportMethod(attributes.get("transport_method"))
