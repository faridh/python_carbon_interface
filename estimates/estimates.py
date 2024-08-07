"""
Module estimates
"""

import json
from json import JSONDecodeError
from typing import Any, TypeVar

from client import Client

from .estimate_request import EstimateRequest
from .estimate_response import EstimateResponse
from .estimate_response_factory import EstimateResponseFactory


class Estimates:
    """
    Class that provides methods to interact against the '/estimates' endpoint
    from Carbon Interface API.
    """

    T = TypeVar("T", bound=EstimateResponse)

    @classmethod
    def create_estimate_request(cls, request: EstimateRequest) -> T:
        """
        Creates an EstimateRequest against Carbon Interface API.
        :param request: the EstimateRequest object to send.
        :return: an EstimateResponse.
        :except: RuntimeError if there's a problem when deserializing the response.
        """
        client: Client = Client()
        response_str: str = client.post("estimates", request)
        try:
            data: dict[str, Any] = json.loads(response_str)
            response_object = EstimateResponseFactory.from_json(data.get("data"))
            return response_object
        except JSONDecodeError as exc:
            raise RuntimeError("Error deserializing response from API.") from exc
