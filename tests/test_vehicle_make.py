"""
Module test_vehicle_make
"""

import unittest

from vehicles import VehicleMake


class TestVehicleMake(unittest.TestCase):
    """
    Defines UTs for vehicle_make module
    """

    def test_should_initialize_successfully(self) -> None:
        """
        Test base case for `VehicleMake` initialization.
        """
        data = {
            "id": "00000000-0000-0000-0000-000000000000",
            "attributes": {"name": "Alfa Romeo", "number_of_models": 69},
        }
        subject: VehicleMake = VehicleMake(data)
        self.assertEqual(subject.id, "00000000-0000-0000-0000-000000000000")
        self.assertEqual(subject.name, "Alfa Romeo")
        self.assertEqual(subject.number_of_models, 69)
