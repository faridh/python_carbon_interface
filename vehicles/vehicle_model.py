"""
Module vehicle_model
"""
from dataclasses import dataclass
from typing import Any


@dataclass
class VehicleModel:
    """
    Class that represents a `Vehiclemodel` instance.
    """

    id: str
    name: str
    year: int
    vehicle_make: str

    def __init__(self, data: dict[str, Any]):
        self.id = data.get("id")
        attributes: dict[str, Any] = data.get("attributes")
        self.name = attributes.get("name")
        self.year = int(attributes.get("year"))
        self.vehicle_make = attributes.get("vehicle_make")