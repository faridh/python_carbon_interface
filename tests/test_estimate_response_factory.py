"""
Module test_estimate_response_factory
"""
import unittest

from estimates import (
    ElectricEstimateResponse,
    EstimateResponseFactory,
    FlightEstimateResponse,
)
from model import Country, DistanceUnit, ElectricityUnit


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
