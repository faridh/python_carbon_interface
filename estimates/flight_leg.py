"""
Module flight_leg
"""

from typing import Any

import json_fix

from model.cabin_class import CabinClass


class FlightLeg:
    """
    Model class that represents a Leg object from the CarbonInterface API.
    """

    departure_airport: str
    destination_airport: str
    cabin_class: CabinClass | None

    def __init__(
        self,
        departure_airport: str,
        destination_airport: str,
        cabin_class: CabinClass | None,
    ):
        if len(departure_airport) != 3:
            raise ValueError(
                f"IATA code length should be 3 characters ({departure_airport})"
            )
        if len(destination_airport) != 3:
            raise ValueError(
                f"IATA code length should be 3 characters ({destination_airport})"
            )

        self.departure_airport = departure_airport.lower()
        self.destination_airport = destination_airport.lower()
        self.cabin_class = cabin_class

    def __json__(self) -> dict[str, Any]:
        return self.__dict__
