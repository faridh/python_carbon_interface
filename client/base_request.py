"""
Module BaseRequest.
"""
from typing import Any


class BaseRequest:
    """
    BaseRequest model.
    """

    def __json__(self) -> dict[str, Any]:
        return self.__dict__
