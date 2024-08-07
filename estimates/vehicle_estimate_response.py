"""
Module shipping_estimate_response
"""

from dataclasses import dataclass
from typing import Any

from model import DistanceUnit

from .estimate_response import EstimateResponse


@dataclass
class VehicleEstimateResponse(EstimateResponse):
    """
    Class that represents a shipping estimate response from Carbon Interface API when
    creating an EstimateRequest.
    """

    distance_unit: DistanceUnit
    distance_value: float
    vehicle_make: str
    vehicle_model: str
    vehicle_year: int
    vehicle_model_id: str

    def __init__(self, data: dict[str, Any]):
        super().__init__(data)
        attributes: dict[str, Any] = data.get("attributes")
        self.distance_unit = DistanceUnit(attributes.get("distance_unit"))
        self.distance_value = float(attributes.get("distance_value"))
        self.vehicle_make = attributes.get("vehicle_make")
        self.vehicle_model = attributes.get("vehicle_model")
        self.vehicle_year = int(attributes.get("vehicle_year"))
        self.vehicle_model_id = attributes.get("vehicle_model_id")
