"""
Module main
"""

import json

from estimates import (
    ElectricityEstimateRequest,
    Estimates,
    FlightEstimateRequest,
    FlightLeg,
)
from model import CabinClass, Country, DistanceUnit, ElectricityUnit

if __name__ == "__main__":

    electric_request = ElectricityEstimateRequest(
        electricity_unit=ElectricityUnit.MWH,
        electricity_value=42,
        country=Country.US,
        state="fl",
    )
    print(json.dumps(electric_request))

    flight_request = FlightEstimateRequest(
        passengers=2,
        legs=[
            FlightLeg("sfo", "yyz", CabinClass.ECONOMY),
            FlightLeg("yyz", "sfo", CabinClass.ECONOMY),
        ],
        distance_unit=DistanceUnit.KM,
    )
    print(json.dumps(flight_request))
    response = Estimates.create_estimate_request(flight_request)
    print(response)
