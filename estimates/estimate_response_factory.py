"""
Module estimate_response_factory
"""

import json
from typing import Any

from .electricity_estimate_response import ElectricEstimateResponse
from .estimate_response import EstimateResponse
from .flight_estimate_response import FlightEstimateResponse


class EstimateResponseFactory:
    """
    Class that determines which response subtype is appropriate to initialize
    given the API response.
    """

    @staticmethod
    def from_json(data: dict[str, Any]) -> EstimateResponse:
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

        raise NotImplementedError(f"Response type not implemented {json.dumps(data)}.")
