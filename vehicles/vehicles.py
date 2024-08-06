"""
Module vehicles
"""

import json
from typing import Any

from client import Client
from .vehicle_model import VehicleModel
from .vehicle_make import VehicleMake


class Vehicles:
    """
    Class that provides methods to interact against the "/vehicle_makes" endpoint
    from Carbon Interface API.
    """

    def __init__(self):
        pass

    @classmethod
    def get_vehicle_makes(cls) -> list[VehicleMake]:
        """
        Gets the list of `VehicleMake` available via CarbonInterface API.
        :return: a list of `VehicleMake` objects.
        :except: RuntimeError if there's a problem when deserializing the response.
        """
        client: Client = Client()
        response_str: str = client.get("vehicle_makes")
        try:
            data: list[dict[str, Any]] = json.loads(response_str)
            response = [VehicleMake(d.get("data")) for d in data]
            return response
        except Exception as exc:
            raise RuntimeError("Error deserializing response from API.") from exc

    @classmethod
    def get_vehicle_models(cls, vehicle_make_id: str) -> list[VehicleModel]:
        """
        Gets the list of `VehicleModel` available for the VehicleMake identified by
        `vehicle_make_id` via Carbon Interface API.
        :param vehicle_make_id: a (str) representing the ID of a `VehicleMake`.
        :return: a list of `VehicleModel` objects.
        :except: RuntimeError if there's a problem when deserializing the response.
        """
        client: Client = Client()
        response_str: str = client.get(
            f"vehicle_makes/{vehicle_make_id}/vehicle_models"
        )
        print(response_str)
        try:
            data: list[dict[str, Any]] = json.loads(response_str)
            response = [VehicleModel(d.get("data")) for d in data]
            return response
        except Exception as exc:
            raise RuntimeError("Error deserializing response from API.") from exc
