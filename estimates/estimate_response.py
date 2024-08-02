"""
Module estimate_response
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from model import Country, ElectricityUnit


@dataclass
class EstimateResponse:
    """
    Class that represents the response from Carbon Interface API when
    creating an EstimateRequest.
    """
    id: str
    type: str
    country: Country
    state: str
    electricity_unit: ElectricityUnit
    electricity_value: float
    estimated_at: datetime
    carbon_g: float
    carbon_lb: float
    carbon_kg: float
    carbon_mt: float

    def __init__(self, data: dict[str, Any]):
        self.id: str = data.get("id")
        self.type: str = data.get("type")
        attributes: dict[str, Any] = data.get("attributes")
        self.country: Country = Country.from_value(attributes.get("country"))
        self.state: str = attributes.get("state")
        self.electricity_unit: ElectricityUnit = ElectricityUnit(
            attributes.get("electricity_unit")
        )
        self.electricity_value: float = float(attributes.get("electricity_value"))
        self.estimated_at: datetime = datetime.strptime(
            attributes.get("estimated_at"), "%Y-%m-%dT%H:%M:%S.%fZ"
        )
        self.carbon_g: float = float(attributes.get("carbon_g"))
        self.carbon_lb: float = float(attributes.get("carbon_lb"))
        self.carbon_kg: float = float(attributes.get("carbon_kg"))
        self.carbon_mt: float = float(attributes.get("carbon_mt"))

    @staticmethod
    def from_json(data: dict[str, Any]):
        """
        Deserializes an EstimateResponse instance based on
        the contents of data
        :param data: the data that represents an EstimateResponse.
        :return: an EstimateResponse instance.
        """
        return EstimateResponse(data)
