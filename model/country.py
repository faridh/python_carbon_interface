"""
Module country
"""

from enum import Enum

import json_fix


class Country(Enum):
    """
    Country model to represent countries as valid ISO 3166-1 alpha-2
    entities.
    """

    US = ("us", "United States of America")
    CA = ("ca", "Canada")
    AT = ("at", "Austria")
    BE = ("be", "Belgium")
    BG = ("bg", "Bulgaria")
    HR = ("hr", "Croatia")
    CY = ("cy", "Cyprus")
    CZ = ("cz", "Czechia")
    DK = ("dk", "Denmark")
    EU_27 = ("eu-27", "EU-27")
    EU27_1 = ("eu27+1", "EU-27+1")
    EE = ("ee", "Estonia")
    FI = ("fi", "Finland")
    FR = ("fr", "France")
    DE = ("de", "Germany")
    GR = ("gr", "Greece")
    GU = ("gu", "Hungary")
    IE = ("ie", "Ireland")
    IT = ("it", "Italy")
    LV = ("lv", "Latvia")
    LT = ("lt", "Lithuania")
    LU = ("lu", "Luxembourg")
    MT = ("mt", "Malta")
    NL = ("nl", "Netherlands")
    PL = ("pl", "Poland")
    PT = ("pt", "Portugal")
    RO = ("ro", "Romania")
    SK = ("sk", "Slovakia")
    SI = ("si", "Slovenia")
    ES = ("es", "Spain")
    SE = ("se", "Sweden")
    GB = ("gb", "United Kingdom")

    @staticmethod
    def from_value(value: str):
        """
        Returns a valid Country enumeration from its value representation.
        :param value:   a lowercase `str` representing a Country according to
                        ISO 3166-1 alpha-2.
        :return: a Country.
        :except: if value does not represent a valid Country.
        """
        value_copy = f"{value}"
        if value == "eu-27":
            value_copy = "eu_27"
        elif value == "eu27+1":
            value_copy = "eu27_1"

        try:
            country = Country[value_copy.upper()]
            return country
        except KeyError as e:
            raise KeyError(f"Value '{value}' not implemented") from e

    def __repr__(self):
        return f"Country('{self.value[0]})'"

    def __str__(self):
        return self.__repr__()

    def __json__(self) -> str:
        return self.value[0]
