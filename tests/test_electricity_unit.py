"""
Module test_electricity_unit
"""
import json
import unittest

from model import ElectricityUnit


class TestElectricityUnit(unittest.TestCase):
    """
    Defines UTs for electricity_unit module
    """

    def test_should_serialize_successfully(self) -> None:
        """
        Tests that ElectricityUnit serializes proper to JSON.
        """
        e_unit_1: ElectricityUnit = ElectricityUnit.KWH
        subject: dict[str, ElectricityUnit] = {"electricity_unit": e_unit_1}
        self.assertEqual(json.dumps(subject), '{"electricity_unit": "kwh"}')

        e_unit_2: ElectricityUnit = ElectricityUnit.MWH
        subject: dict[str, ElectricityUnit] = {"electricity_unit": e_unit_2}
        self.assertEqual(json.dumps(subject), '{"electricity_unit": "mwh"}')
