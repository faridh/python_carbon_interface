"""
Module test_country
"""

import unittest

from model import Country


class TestCountry(unittest.TestCase):
    """
    Defines UTs for country module
    """

    def test_should_initialize_successfully(self) -> None:
        """
        Test base case for Country creation from @staticmethod.
        """
        subject: Country = Country.from_value("fr")
        self.assertEqual(subject, Country.FR)

    def test_should_initialize_edge_cases(self) -> None:
        """
        Test edge-cases for EU regions.
        """
        subject_1: Country = Country.from_value("eu-27")
        self.assertEqual(subject_1, Country.EU_27)

        subject_2: Country = Country.from_value("eu27+1")
        self.assertEqual(subject_2, Country.EU27_1)

    def test_should_throw_exception(self) -> None:
        """
        Tests that Country throws an exception when trying to initialize from
        an unsupported value.
        """

        def test_function():
            return Country.from_value("mx")

        self.assertRaises(KeyError, test_function)
