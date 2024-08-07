"""
Module estimate_response_factory
"""

import json
from typing import Any, TypeVar

from .electricity_estimate_response import ElectricEstimateResponse
from .estimate_response import EstimateResponse
from .flight_estimate_response import FlightEstimateResponse
from .shipping_estimate_response import ShippingEstimateResponse
from .vehicle_estimate_response import VehicleEstimateResponse


class EstimateResponseFactory:
    """
    Class that determines which response subtype is appropriate to initialize
    given the API response.
    """

    T: TypeVar = TypeVar("T", bound=EstimateResponse)

    @staticmethod
    def from_json(data: dict[str, Any]) -> T:
        """
        Deserializes an EstimateResponse instance based on
        the contents of data
        :param data: the data that represents an EstimateResponse.
        :return: an EstimateResponse instance.
        """
        attributes: dict[str, Any] | None | Any = data.get("attributes")
        if "electricity_value" in attributes:
            return ElectricEstimateResponse(data)
        if "passengers" in attributes:
            return FlightEstimateResponse(data)
        if "weight_value" in attributes:
            return ShippingEstimateResponse(data)
        if "vehicle_make" in attributes:
            return VehicleEstimateResponse(data)

        raise NotImplementedError(f"Response type not implemented {json.dumps(data)}.")
