"""
Module vehicles
"""

import json
from json import JSONDecodeError
from typing import Any

from client import Client

from .vehicle_make import VehicleMake
from .vehicle_model import VehicleModel


class Vehicles:
    """
    Class that provides methods to interact against the "/vehicle_makes" endpoint
    from Carbon Interface API.
    """

    @classmethod
    def get_vehicle_makes(cls) -> list[VehicleMake]:
        """
        Gets the list of `VehicleMake` available via CarbonInterface API.
        :return: a list of `VehicleMake` objects.
        :raises: RuntimeError if there's a problem when deserializing the response.
        """
        client: Client = Client()
        response_str: str = client.get("vehicle_makes")
        try:
            data: list[dict[str, Any]] = json.loads(response_str)
            response = [VehicleMake(d.get("data")) for d in data]
            return response
        except JSONDecodeError as exc:
            raise RuntimeError("Error deserializing response from API.") from exc

    @classmethod
    def get_vehicle_models(cls, vehicle_make_id: str) -> list[VehicleModel]:
        """
        Gets the list of `VehicleModel` available for the VehicleMake identified by
        `vehicle_make_id` via Carbon Interface API.
        :param vehicle_make_id: a (str) representing the ID of a `VehicleMake`.
        :return: a list of `VehicleModel` objects.
        :raises: RuntimeError if there's a problem when deserializing the response.
        """
        client: Client = Client()
        response_str: str = client.get(
            f"vehicle_makes/{vehicle_make_id}/vehicle_models"
        )
        try:
            data: list[dict[str, Any]] = json.loads(response_str)
            response = [VehicleModel(d.get("data")) for d in data]
            return response
        except JSONDecodeError as exc:
            raise RuntimeError("Error deserializing response from API.") from exc
