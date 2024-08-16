"""
Module estimate_request
"""

from typing import Any

from client import BaseRequest

from .estimate_type import EstimateType


class EstimateRequest(BaseRequest):
    """
    Class that represent a basic estimate request in the Carbon interface
    API. It is the base class for all other types of request types, i.e.:
    'electricity', 'flight', etc.
    """

    type: EstimateType

    def __init__(self, estimate_type: EstimateType):
        self.type = estimate_type

    def __json__(self) -> dict[str, Any]:
        response = {}
        for k, v in self.__dict__.items():
            if v:
                if isinstance(v, list):
                    response[k] = [elem.__json__() for elem in v]
                elif v.__class__ in (int, float, bool):
                    response[k] = v
                else:
                    response[k] = v.__str__()
        return response
