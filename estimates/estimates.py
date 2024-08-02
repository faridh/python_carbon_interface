"""
Module estimates
"""
import json
from typing import Any

from client import Client

from .estimate_request import EstimateRequest
from .estimate_response import EstimateResponse


class Estimates:
    """
    Class that provides methods to interact against the '/estimates' endpoint
    from Carbon Interface API.
    """

    def __init__(self):
        pass

    @classmethod
    def create_estimate_request(cls, request: EstimateRequest) -> EstimateResponse:
        """
        Creates an EstimateRequest against Carbon Interface API.
        :param request: the EstimateRequest object to send.
        :return: an EstimateResponse.
        :except: IOError if there's a problem when deserializing the response.
        """
        client = Client()
        response_str: str = client.post("estimates", request)
        print(response_str)
        try:
            data: dict[str, Any] = json.loads(response_str)
            response_object = EstimateResponse.from_json(data.get("data"))
            return response_object
        except IOError as io_error:
            raise IOError("Error deserializing response from API.") from io_error
