"""
Module shipping_estimate_response
"""

from dataclasses import dataclass
from typing import Any
from uuid import UUID

from model import DistanceUnit

from .estimate_response import EstimateResponse


@dataclass
class VehicleEstimateResponse(EstimateResponse):
    """
    Class that represents a vehicle estimate response from CarbonInterface API when
    creating an EstimateRequest.
    """

    distance_unit: DistanceUnit
    distance_value: float
    vehicle_make: str
    vehicle_model: str
    vehicle_year: int
    vehicle_model_id: UUID

    def __init__(self, data: dict[str, Any]):
        super().__init__(data)
        attributes: dict[str, Any] = data.get("attributes")
        self.distance_unit: DistanceUnit = DistanceUnit(attributes.get("distance_unit"))
        self.distance_value: float = float(attributes.get("distance_value"))
        self.vehicle_make: str = attributes.get("vehicle_make")
        self.vehicle_model: str = attributes.get("vehicle_model")
        self.vehicle_year: int = int(attributes.get("vehicle_year"))
        self.vehicle_model_id: UUID = UUID(attributes.get("vehicle_model_id"))
