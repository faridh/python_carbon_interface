"""
Module estimate_response
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Any
from uuid import UUID


@dataclass
class EstimateResponse:
    """
    Class that represents a generic response from Carbon Interface API when
    creating an EstimateRequest.
    """

    id: UUID
    type: str
    estimated_at: datetime
    carbon_g: float
    carbon_lb: float
    carbon_kg: float
    carbon_mt: float

    def __init__(self, data: dict[str, Any]):
        self.id: UUID = UUID(data.get("id"))
        self.type: str = data.get("type")
        attributes: dict[str, Any] = data.get("attributes")
        self.estimated_at: datetime = datetime.strptime(
            attributes.get("estimated_at"), "%Y-%m-%dT%H:%M:%S.%fZ"
        )
        self.carbon_g: float = float(attributes.get("carbon_g"))
        self.carbon_lb: float = float(attributes.get("carbon_lb"))
        self.carbon_kg: float = float(attributes.get("carbon_kg"))
        self.carbon_mt: float = float(attributes.get("carbon_mt"))
