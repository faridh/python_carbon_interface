"""
Module client
"""

import os
from typing import Any

import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from .base_request import BaseRequest


class Client:
    """
    Client singleton class provides single access to low-level method calls to
    Carbon Interface API over standard HTTP methods such as GET, POST.
    """

    DEFAULT_TIMEOUT: int = 10
    instance = None

    def __init__(self):
        api_key: str | None = os.getenv("CARBON_INTERFACE_API_KEY")
        if not api_key:
            raise RuntimeError("CARBON_INTERFACE_API_KEY is not defined")
        self.__api_key = os.getenv("CARBON_INTERFACE_API_KEY")
        self.__api_base_url = "https://www.carboninterface.com/api/v1"
        self.__default_headers = {
            "Authorization": f"Bearer {self.__api_key}",
            "Content-Type": "application/json",
        }

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance") or not cls.instance:
            cls.instance = super(Client, cls).__new__(cls)
        return cls.instance

    def get(self, endpoint: str) -> str:
        """
        Executes a GET call to Carbon Interface API.
        :param endpoint: the final endpoint for the request, i.e.: 'estimates'
        :raises: RuntimeError: when the request can't be completed.
        """
        full_api_url: str = f"{self.__api_base_url}/{endpoint}"
        try:
            response = self.__get_with_retries(full_api_url)
            if response.status_code == 200:
                return response.text

            raise IOError(
                f"Could not execute the GET request. Status code: {response.status_code}."
            )
        except IOError as exc:
            raise RuntimeError("Could not execute the GET request.") from exc

    def post(self, endpoint: str, data: BaseRequest) -> str:
        """
        Executes a POST call to Carbon Interface API.
        :param endpoint: the final endpoint for the request, i.e.: 'estimates'
        :param data: the data to be sent as the Request body.
        :raises: RuntimeError: when the request can't be completed.
        """
        full_api_url: str = f"{self.__api_base_url}/{endpoint}"
        try:
            response = self.__post_with_retries(full_api_url, data)
            if response.status_code in {200, 201}:
                return response.text

            raise IOError(
                f"Could not execute the POST request. Status code: {response.status_code}."
            )
        except IOError as exc:
            raise RuntimeError("Could not execute the POST request.") from exc

    def __get_with_retries(self, url: str) -> requests.Response:
        response: requests.Response | None
        try:
            retry_conf = Retry(
                total=4,
                backoff_factor=2,
                status_forcelist={429, 500, 503},
            )

            adapter: HTTPAdapter = HTTPAdapter(max_retries=retry_conf)
            session: requests.Session = requests.Session()
            session.mount("https://", adapter)
            response = session.get(
                url,
                headers=self.__default_headers,
                timeout=Client.DEFAULT_TIMEOUT,
            )
            return response
        except IOError as e:
            raise RuntimeError("GET failed.") from e

    def __post_with_retries(self, url: str, data: Any) -> requests.Response:
        response: requests.Response | None
        try:
            retry_conf = Retry(
                total=4,
                backoff_factor=2,
                status_forcelist={429, 500, 503},
                allowed_methods={"POST"},
            )

            adapter: HTTPAdapter = HTTPAdapter(max_retries=retry_conf)
            session: requests.Session = requests.Session()
            session.mount("https://", adapter)
            response = session.post(
                url,
                headers=self.__default_headers,
                json=data,
                timeout=Client.DEFAULT_TIMEOUT,
            )
            return response
        except IOError as e:
            raise RuntimeError("POST failed.") from e
