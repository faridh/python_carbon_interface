"""
Module test_client
"""

import os
from unittest import TestCase, mock

from requests import RequestException

from client import BaseRequest, Client


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
    @mock.patch("client.client.requests.Session.get")
    def test_should_execute_get_successfully(self, mock_session) -> None:
        """
        Tests that client invokes `get` successfully.
        """

        mock_session.return_value.text = '{"k": "v"}'
        mock_session.return_value.status_code = 200
        subject: Client = Client()
        result: str = subject.get("/endpoint")
        self.assertEqual(result, '{"k": "v"}')

    @mock.patch.dict(os.environ, {"CARBON_INTERFACE_API_KEY": "someApiKey"})
    @mock.patch("client.client.requests.Session.get")
    def test_get_should_raise_error_when_not_200(self, mock_session) -> None:
        """
        Tests that client raises a RuntimeError when the HTTP status != 200.
        """

        mock_session.return_value.text = '{"k": "v"}'
        mock_session.return_value.status_code = 400

        def helper_function() -> None:
            subject: Client = Client()
            subject.get("/endpoint")

        self.assertRaises(RuntimeError, helper_function)

    @mock.patch.dict(os.environ, {"CARBON_INTERFACE_API_KEY": "someApiKey"})
    @mock.patch("client.client.requests.Session.get")
    def test_get_should_raise_error_when_retry_not_successful(
        self, mock_session
    ) -> None:
        """
        Tests that client raises a RuntimeError when the retry mechanism is not successful.
        """

        mock_session.return_value.text = '{"k": "v"}'
        mock_session.return_value.status_code = 429
        mock_session.side_effect = RequestException(mock.Mock())

        def helper_function() -> None:
            subject: Client = Client()
            subject.get("/endpoint")

        self.assertRaises(RuntimeError, helper_function)

    @mock.patch.dict(os.environ, {"CARBON_INTERFACE_API_KEY": "someApiKey"})
    @mock.patch("client.client.requests.Session.post")
    def test_should_execute_post_successfully(self, mock_session) -> None:
        """
        Tests that client invokes `post` successfully.
        """

        mock_session.return_value.text = '{"k": "v"}'
        mock_session.return_value.status_code = 201
        subject: Client = Client()
        result: str = subject.post("/endpoint", BaseRequest())
        self.assertEqual(result, '{"k": "v"}')

    @mock.patch.dict(os.environ, {"CARBON_INTERFACE_API_KEY": "someApiKey"})
    @mock.patch("client.client.requests.Session.post")
    def test_post_should_raise_error_when_not_200(self, mock_session) -> None:
        """
        Tests that client raises a RuntimeError when the HTTP status != {200, 201}.
        """

        mock_session.return_value.text = '{"k": "v"}'
        mock_session.return_value.status_code = 400

        def helper_function() -> None:
            subject: Client = Client()
            subject.post("/endpoint", BaseRequest())

        self.assertRaises(RuntimeError, helper_function)

    @mock.patch.dict(os.environ, {"CARBON_INTERFACE_API_KEY": "someApiKey"})
    @mock.patch("client.client.requests.Session.post")
    def test_post_should_raise_error_when_retry_not_successful(
        self, mock_session
    ) -> None:
        """
        Tests that client raises a RuntimeError when the retry mechanism is not successful.
        """

        mock_session.return_value.text = '{"k": "v"}'
        mock_session.return_value.status_code = 429
        mock_session.side_effect = RequestException(mock.Mock())

        def helper_function() -> None:
            subject: Client = Client()
            subject.post("/endpoint", BaseRequest())

        self.assertRaises(RuntimeError, helper_function)
