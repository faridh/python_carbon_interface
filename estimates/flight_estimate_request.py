"""
Module flight_estimate_request
"""

from typing import Any

import json_fix

from model import DistanceUnit

from .estimate_request import EstimateRequest
from .estimate_type import EstimateType
from .flight_leg import FlightLeg


class FlightEstimateRequest(EstimateRequest):
    """
    Class that represent the body of the request against the '/estimates'
    endpoint
    """

    passengers: int
    legs: list[FlightLeg]
    distance_unit: DistanceUnit

    def __init__(
        self,
        passengers: int,
        legs: list[FlightLeg],
        distance_unit: DistanceUnit | None = DistanceUnit.KM,
    ):
        super().__init__(EstimateType.FLIGHT)
        self.passengers = passengers
        self.legs = legs
        self.distance_unit = distance_unit

    def __json__(self) -> dict[str, Any]:
        return {k: v for k, v in self.__dict__.items() if v is not None}
