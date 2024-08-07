"""
Module estimate_request
"""

from typing import Any

import json_fix

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
        return {k: v for k, v in self.__dict__.items() if v is not None}
