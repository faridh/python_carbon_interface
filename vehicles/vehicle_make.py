"""
Module vehicle_make
"""
from typing import Any


class VehicleMake:
    """
    Class that represents a VehicleMake instance.
    """

    id: str
    name: str
    number_of_models: int

    def __init__(self, data: dict[str, Any]):
        self.id = data.get("id")
        attributes: dict[str, Any] = data.get("attributes")
        self.name = attributes.get("name")
        self.number_of_models = attributes.get("number_of_models")