"""
Module flight_estimate_response
"""

from dataclasses import dataclass
from typing import Any

from model import DistanceUnit

from .estimate_response import EstimateResponse
from .flight_leg import FlightLeg


@dataclass
class FlightEstimateResponse(EstimateResponse):
    """
    Class that represents a flight estimate response from CarbonInterface API when
    creating an EstimateRequest.
    """

    passengers: int
    legs: list[FlightLeg]
    distance_unit: DistanceUnit | None
    distance_value: float

    def __init__(self, data: dict[str, Any]):
        super().__init__(data)
        attributes: dict[str, Any] = data.get("attributes")
        self.passengers: int = int(attributes.get("passengers"))
        self.legs: list[FlightLeg] = attributes.get("legs")
        self.distance_unit: DistanceUnit = DistanceUnit(attributes.get("distance_unit"))
        self.distance_value: float = float(attributes.get("distance_value"))
