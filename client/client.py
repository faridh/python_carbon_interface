"""
Module client
"""

import os

import requests

from .base_request import BaseRequest


class Client:
    """
    Client singleton class provides single access to low-level method calls to
    Carbon Interface API over standard HTTP methods such as GET, POST.
    """

    DEFAULT_TIMEOUT: int = 10
    instance = None

    def __init__(self):
        if os.getenv("CARBON_INTERFACE_API_KEY") is None:
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
        :return:
        """
        full_api_url: str = f"{self.__api_base_url}/{endpoint}"
        response = requests.get(
            full_api_url,
            headers=self.__default_headers,
            timeout=Client.DEFAULT_TIMEOUT,
        )
        return response.text

    def post(self, endpoint: str, data: BaseRequest) -> str:
        """
        Executes a POST call to Carbon Interface API.
        :param endpoint: the final endpoint for the request, i.e.: 'estimates'
        :param data: the data to be sent as the Request body.
        :return:
        """
        full_api_url: str = f"{self.__api_base_url}/{endpoint}"
        response = requests.post(
            full_api_url,
            json=data,
            headers=self.__default_headers,
            timeout=Client.DEFAULT_TIMEOUT,
        )
        return response.text
