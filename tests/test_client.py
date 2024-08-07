"""
Module test_client
"""

import os
from unittest import TestCase, mock

from requests import Response

from client import Client


class TestClient(TestCase):
    """
    UTs for client module
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

    @mock.patch.dict(os.environ, {"CARBON_INTERFACE_API_KEY": "someApiKey"})
    @mock.patch("client.client.requests.get")
    def test_should_execute_get_successfully(self, mock_requests) -> None:
        """
        Tests that client invokes `get` successfully.
        """

        mock_requests.return_value.text = '{"k": "v"}'
        subject: Client = Client()
        result: str = subject.get("/endpoint")
        self.assertEqual(result, '{"k": "v"}')

    @mock.patch.dict(os.environ, {"CARBON_INTERFACE_API_KEY": "someApiKey"})
    @mock.patch("client.client.requests.post")
    def test_should_execute_post_successfully(self, mock_requests) -> None:
        """
        Tests that client invokes `post` successfully.
        """

        mock_requests.return_value.text = '{"k": "v"}'
        subject: Client = Client()
        result: str = subject.post("/endpoint", {})
        self.assertEqual(result, '{"k": "v"}')
