"""
Module test_client
"""

import os
from unittest import TestCase, mock

from client import Client


class TestClient(TestCase):
    """
    Defines UTs for client module
    """

    @mock.patch.dict(os.environ, {"CARBON_INTERFACE_API_KEY": "someApiKey"})
    def test_should_initialize_successfully(self):
        """
        Tests that a client instance is initialized successfully.
        """
        subject: Client = Client()
        self.assertIsInstance(subject, Client)

    @mock.patch.dict(os.environ, {"CARBON_INTERFACE_API_KEY": ""})
    def test_should_raise_error_when_no_api_key(self):
        """
        Tests that a client raises a `RuntimeError` when `CARBON_INTERFACE_API_KEY`
        is not present.
        """
        self.assertRaises(RuntimeError, Client)
