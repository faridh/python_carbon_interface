"""
Module flight_leg
"""
from typing import Any

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
                f"IATA code length should be 3 characters ({departure_airport=})"
            )
        if len(destination_airport) != 3:
            raise ValueError(
                f"IATA code length should be 3 characters ({destination_airport=})"
            )

        self.departure_airport = departure_airport.lower()
        self.destination_airport = destination_airport.lower()
        self.cabin_class = cabin_class

    def __repr__(self) -> str:
        return (f"FlightLeg('{self.departure_airport}', "
                f"'{self.destination_airport}', "
                f"{self.cabin_class})")

    def __json__(self) -> dict[str, Any]:
        return {'departure_airport': self.departure_airport,
                'destination_airport': self.destination_airport,
                'cabin_class': self.cabin_class.__str__()}
