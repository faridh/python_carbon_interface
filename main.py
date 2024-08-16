"""
Module main
"""


from estimates import (
    ElectricityEstimateRequest,
    Estimates,
    FlightEstimateRequest,
    FlightLeg,
    FuelCombustionEstimateRequest,
    ShippingEstimateRequest,
    VehicleEstimateRequest,
)
from model import (
    CabinClass,
    Country,
    DistanceUnit,
    ElectricityUnit,
    FuelSourceType,
    FuelSourceUnit,
    TransportMethod,
    WeightUnit,
)

if __name__ == "__main__":

    electric_request = ElectricityEstimateRequest(
        country=Country.US, electricity_value=42, electricity_unit=ElectricityUnit.MWH
    )
    # print(electric_request.__json__())
    print(Estimates.create_estimate_request(electric_request))

    flight_request = FlightEstimateRequest(
        passengers=2,
        legs=[
            FlightLeg("sfo", "yyz", CabinClass.ECONOMY),
            FlightLeg("yyz", "sfo", CabinClass.ECONOMY),
        ],
        distance_unit=DistanceUnit.KM,
    )
    # print(flight_request.__json__())
    print(Estimates.create_estimate_request(flight_request))

    shipping_request = ShippingEstimateRequest(
        weight_unit=WeightUnit.GRAMS,
        weight_value=200.0,
        distance_unit=DistanceUnit.KM,
        distance_value=2000,
        transport_method=TransportMethod.TRUCK,
    )
    # print(shipping_request.__json__())
    print(Estimates.create_estimate_request(shipping_request))

    vehicle_request = VehicleEstimateRequest(
        distance_unit=DistanceUnit.MI,
        distance_value=100,
        vehicle_model_id="7268a9b7-17e8-4c8d-acca-57059252afe9",
    )
    # print(vehicle_request.__json__())
    print(Estimates.create_estimate_request(vehicle_request))

    fuel_request = FuelCombustionEstimateRequest(
        fuel_source_type=FuelSourceType.HOME_HEATING_DIESEL_FUEL,
        fuel_source_unit=FuelSourceUnit.BTU,
        fuel_source_value=2,
    )
    # print(fuel_request.__json__())
    print(Estimates.create_estimate_request(fuel_request))
