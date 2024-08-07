"""
Module test_estimates
"""

import os
from datetime import datetime
from unittest import TestCase, mock

from estimates import (
    ElectricEstimateResponse,
    ElectricityEstimateRequest,
    EstimateResponse,
    Estimates,
)
from model import Country, ElectricityUnit


@mock.patch.dict(os.environ, {"CARBON_INTERFACE_API_KEY": "someApiKey"})
class TestEstimates(TestCase):
    """
    UTs for estimates module.
    """

    @mock.patch("estimates.estimates.Client.post")
    def test_should_create_estimate_successfully(self, mock_client) -> None:
        """
        Tests that the estimates module can parse successfully the response from
        the `/estimates` endpoint.
        """

        mock_client.return_value = """
        {"data":{"id":"00000000-0000-0000-0000-000000000000","type":"estimate",
        "attributes":{"country":"us","state":"fl","electricity_unit":"mwh",
        "electricity_value":42.0,"estimated_at":"2024-08-01T20:23:05.018Z",
        "carbon_g":16710476,"carbon_lb":36840.29,"carbon_kg":16710.48,
        "carbon_mt":16.71}}}
        """

        test_estimate: ElectricityEstimateRequest = ElectricityEstimateRequest(
            Country.US, 42.0
        )
        subject: ElectricEstimateResponse = Estimates.create_estimate_request(
            test_estimate
        )
        self.assertTrue(isinstance(subject, ElectricEstimateResponse))
        self.assertTrue(issubclass(subject.__class__, EstimateResponse))
        self.assertEqual(subject.id, "00000000-0000-0000-0000-000000000000")
        self.assertEqual(subject.country, Country.US)
        self.assertEqual(subject.state, "fl")
        self.assertEqual(subject.electricity_unit, ElectricityUnit.MWH)
        self.assertEqual(subject.electricity_value, 42.0)
        self.assertEqual(
            subject.estimated_at,
            datetime.strptime("2024-08-01T20:23:05.018Z", "%Y-%m-%dT%H:%M:%S.%fZ"),
        )
        self.assertEqual(subject.carbon_g, 16710476)
        self.assertEqual(subject.carbon_lb, 36840.29)
        self.assertEqual(subject.carbon_kg, 16710.48)
        self.assertEqual(subject.carbon_mt, 16.71)

    @mock.patch("estimates.estimates.Client.post")
    def test_should_raise_error_when_malformed_response(self, mock_client) -> None:
        """
        Tests that the `estimates` module raises an exception when it can't parse
        the response from the `/estimates` endpoint.
        """
        mock_client.return_value = "not json data"

        test_estimate: ElectricityEstimateRequest = ElectricityEstimateRequest(
            Country.US, 42.0
        )
        self.assertRaises(
            RuntimeError, lambda: Estimates.create_estimate_request(test_estimate)
        )
