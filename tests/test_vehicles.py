"""
Module test_vehicles
"""

from unittest import TestCase, mock

from vehicles import VehicleMake, Vehicles


class TestVehicles(TestCase):
    """
    UTs for vehicles module.
    """

    @mock.patch("vehicles.vehicles.Client.get")
    def test_should_get_vehicle_makes_successfully(self, mock_client) -> None:
        """
        Tests that the vehicles module can parse successfully the response from
        the `/vehicle_makes` endpoint.
        """

        mock_client.return_value = """
        [{"data": {"id": "00000000-0000-0000-0000-000000000000", 
        "type": "vehicle_make", "attributes": 
        {"name": "Alfa Romeo", "number_of_models": 69}}}]
        """
        subject: list[VehicleMake] = Vehicles.get_vehicle_makes()
        self.assertEqual(len(subject), 1)
        response_object: VehicleMake = subject[0]
        self.assertEqual(response_object.id, "00000000-0000-0000-0000-000000000000")
        self.assertEqual(response_object.name, "Alfa Romeo")
        self.assertEqual(response_object.number_of_models, 69)

    @mock.patch("vehicles.vehicles.Client.get")
    def test_should_raise_error_when_malformed_response(self, mock_client) -> None:
        """
        Tests that the `vehicles` module raises an exception when it can't parse
        the response from the `/vehicle_makes` endpoint.
        """
        mock_client.return_value = "not json data"
        self.assertRaises(RuntimeError, Vehicles.get_vehicle_makes)
