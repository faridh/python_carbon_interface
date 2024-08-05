"""
Module main
"""

import json

from estimates import (
    ElectricityEstimateRequest,
    FlightEstimateRequest,
    FlightLeg,
    ShippingEstimateRequest,
)
from model import (
    CabinClass,
    Country,
    DistanceUnit,
    ElectricityUnit,
    TransportMethod,
    WeightUnit,
)

if __name__ == "__main__":

    electric_request = ElectricityEstimateRequest(
        country=Country.US, electricity_value=42, electricity_unit=ElectricityUnit.MWH
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

    shipping_request = ShippingEstimateRequest(
        weight_unit=WeightUnit.GRAMS,
        weight_value=200.0,
        distance_unit=DistanceUnit.KM,
        distance_value=2000,
        transport_method=TransportMethod.TRUCK,
    )
    print(json.dumps(shipping_request))

    # response = Estimates.create_estimate_request(shipping_request)
    # print(response)
