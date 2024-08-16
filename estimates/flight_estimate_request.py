"""
Module flight_estimate_request
"""

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
        distance_unit: DistanceUnit = DistanceUnit.KM,
    ):
        super().__init__(EstimateType.FLIGHT)
        self.passengers = passengers
        self.legs = legs
        self.distance_unit = distance_unit
