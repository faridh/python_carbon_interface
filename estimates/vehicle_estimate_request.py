"""
Module vehicle_estimate_request
"""

from model import DistanceUnit

from .estimate_request import EstimateRequest
from .estimate_type import EstimateType


class VehicleEstimateRequest(EstimateRequest):
    """
    Class that represent the body of the request against the '/estimates'
    endpoint
    """

    distance_unit: DistanceUnit
    distance_value: float
    vehicle_model_id: str

    def __init__(
        self, distance_unit: DistanceUnit, distance_value: float, vehicle_model_id: str
    ):
        super().__init__(EstimateType.VEHICLE)
        self.distance_unit = distance_unit
        self.distance_value = distance_value
        self.vehicle_model_id = vehicle_model_id
