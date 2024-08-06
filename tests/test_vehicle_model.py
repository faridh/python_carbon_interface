"""
Module test_vehicle_make
"""

import unittest

from vehicles import VehicleModel


class TestVehicleModel(unittest.TestCase):
    """
    Defines UTs for vehicle_make module
    """

    def test_should_initialize_successfully(self) -> None:
        """
        Test base case for `VehicleMake` initialization.
        """
        data = {
            "id": "00000000-0000-0000-0000-000000000000",
            "attributes": {"name": "Taurus", "year": 1993, "vehicle_make": "Ford"},
        }
        subject: VehicleModel = VehicleModel(data)
        self.assertEqual(subject.id, "00000000-0000-0000-0000-000000000000")
        self.assertEqual(subject.name, "Taurus")
        self.assertEqual(subject.year, 1993)
        self.assertEqual(subject.vehicle_make, "Ford")
