"""
Module test_estimate_response_factory
"""

import unittest
from uuid import UUID

from estimates import (
    ElectricEstimateResponse,
    EstimateResponseFactory,
    FlightEstimateResponse,
    ShippingEstimateResponse,
    VehicleEstimateResponse,
)
from model import Country, DistanceUnit, ElectricityUnit, TransportMethod, WeightUnit


class TestEstimateResponseFactory(unittest.TestCase):
    """
    UTs for module estimate_response_factory
    """

    def test_should_deserialize_electricity_successfully(self) -> None:
        """
        Tests that EstimateResponseFactory deserializes an ElectricEstimateResponse
        successfully.
        """
        sample_response = {
            "id": "00000000-0000-0000-0000-000000000000",
            "type": "estimate",
            "attributes": {
                "country": "us",
                "state": "fl",
                "electricity_unit": "mwh",
                "electricity_value": 42.0,
                "estimated_at": "2024-08-01T20:23:05.018Z",
                "carbon_g": 16710476,
                "carbon_lb": 36840.29,
                "carbon_kg": 16710.48,
                "carbon_mt": 16.71,
            },
        }
        subject: ElectricEstimateResponse = EstimateResponseFactory.from_json(
            sample_response
        )
        self.assertTrue(isinstance(subject, ElectricEstimateResponse))
        self.assertEqual(subject.country, Country.US)
        self.assertEqual(subject.electricity_unit, ElectricityUnit.MWH)
        self.assertEqual(subject.electricity_value, 42.0)
        self.assertEqual(subject.carbon_g, 16710476)
        self.assertEqual(subject.carbon_kg, 16710.48)
        print(subject)

    def test_should_deserialize_flight_successfully(self) -> None:
        """
        Tests that EstimateResponseFactory deserializes a FlightEstimateResponse
        successfully.
        """
        sample_response = {
            "id": "00000000-0000-0000-0000-000000000000",
            "type": "estimate",
            "attributes": {
                "passengers": 2,
                "legs": [
                    {
                        "departure_airport": "SFO",
                        "destination_airport": "YYZ",
                        "cabin_class": "economy",
                    },
                    {
                        "departure_airport": "YYZ",
                        "destination_airport": "SFO",
                        "cabin_class": "economy",
                    },
                ],
                "distance_value": 7454.15,
                "distance_unit": "km",
                "estimated_at": "2024-08-02T20:11:01.487Z",
                "carbon_g": 859824,
                "carbon_lb": 1895.59,
                "carbon_kg": 859.82,
                "carbon_mt": 0.86,
            },
        }
        subject: FlightEstimateResponse = EstimateResponseFactory.from_json(
            sample_response
        )
        self.assertTrue(isinstance(subject, FlightEstimateResponse))
        self.assertEqual(subject.passengers, 2)
        self.assertEqual(len(subject.legs), 2)
        self.assertEqual(subject.distance_unit, DistanceUnit.KM)
        self.assertEqual(subject.distance_value, 7454.15)
        self.assertEqual(subject.carbon_lb, 1895.59)
        self.assertEqual(subject.carbon_mt, 0.86)

    def test_should_deserialize_shipping_successfully(self) -> None:
        """
        Tests that EstimateResponseFactory deserializes a ShippingEstimateResponse
        successfully.
        """
        sample_response = {
            "id": "00000000-0000-0000-0000-000000000000",
            "type": "estimate",
            "attributes": {
                "distance_value": "2000.0",
                "distance_unit": "km",
                "weight_value": "200.0",
                "weight_unit": "g",
                "transport_method": "truck",
                "estimated_at": "2020-07-31T13:00:04.446Z",
                "carbon_g": 25,
                "carbon_lb": 0.06,
                "carbon_kg": 0.03,
                "carbon_mt": 0.0,
            },
        }
        subject: ShippingEstimateResponse = EstimateResponseFactory.from_json(
            sample_response
        )
        self.assertTrue(isinstance(subject, ShippingEstimateResponse))
        self.assertEqual(subject.distance_unit, DistanceUnit.KM)
        self.assertEqual(subject.distance_value, 2000.00)
        self.assertEqual(subject.weight_unit, WeightUnit.GRAMS)
        self.assertEqual(subject.weight_value, 200.00)
        self.assertEqual(subject.transport_method, TransportMethod.TRUCK)
        self.assertEqual(subject.carbon_g, 25)
        self.assertEqual(subject.carbon_lb, 0.06)
        self.assertEqual(subject.carbon_kg, 0.03)
        self.assertEqual(subject.carbon_mt, 0.0)
        self.assertEqual(subject.estimated_at.year, 2020)
        self.assertEqual(subject.estimated_at.month, 7)
        self.assertEqual(subject.estimated_at.day, 31)

    def test_should_deserialize_vehicle_successfully(self) -> None:
        """
        Tests that EstimateResponseFactory deserializes a VehicleEstimateResponse
        successfully.
        """
        sample_response = {
            "id": "00000000-0000-0000-0000-000000000000",
            "type": "estimate",
            "attributes": {
                "distance_value": 100.0,
                "vehicle_make": "Toyota",
                "vehicle_model": "Corolla",
                "vehicle_year": 1993,
                "vehicle_model_id": "00000000-0000-0000-0000-000000000000",
                "distance_unit": "mi",
                "estimated_at": "2021-01-10T15:24:32.568Z",
                "carbon_g": 37029,
                "carbon_lb": 81.64,
                "carbon_kg": 37.03,
                "carbon_mt": 0.04,
            },
        }
        subject: VehicleEstimateResponse = EstimateResponseFactory.from_json(
            sample_response
        )
        self.assertTrue(isinstance(subject, VehicleEstimateResponse))
        self.assertEqual(subject.id, UUID("00000000-0000-0000-0000-000000000000"))
        self.assertEqual(subject.distance_value, 100.00)
        self.assertEqual(subject.vehicle_make, "Toyota")
        self.assertEqual(subject.vehicle_model, "Corolla")
        self.assertEqual(subject.vehicle_year, 1993)
        self.assertEqual(
            subject.vehicle_model_id, UUID("00000000-0000-0000-0000-000000000000")
        )
        self.assertEqual(subject.distance_unit, DistanceUnit.MI)
        self.assertEqual(subject.carbon_g, 37029)
        self.assertEqual(subject.carbon_lb, 81.64)
        self.assertEqual(subject.carbon_kg, 37.03)
        self.assertEqual(subject.carbon_mt, 0.04)

    def test_should_throw_not_implemented_error(self) -> None:
        """
        Tests that EstimateResponseFactory throws a NonImplementedError
        successfully.
        """

        def test_function():
            sample_response = {
                "id": "2d968fce-859d-4dc1-9489-987e795f42bb",
                "type": "estimate",
                "attributes": {
                    "fuel_source_type": "dfo",
                    "fuel_source_unit": "btu",
                    "fuel_source_value": 2,
                    "estimated_at": "2020-07-24T02:23:24.441Z",
                    "carbon_g": 146320,
                    "carbon_lb": 322.58,
                    "carbon_kg": 146.32,
                    "carbon_mt": 0.15,
                },
            }
            EstimateResponseFactory.from_json(sample_response)

        self.assertRaises(NotImplementedError, test_function)
