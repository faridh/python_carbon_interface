"""
Module main
"""
import json

from estimates import ElectricityEstimateRequest, Estimates
from model.country import Country
from model.electricity_unit import ElectricityUnit

if __name__ == "__main__":

    electric_request = ElectricityEstimateRequest(
        ElectricityUnit.MWH, 42, Country.EU_27, "fl"
    )
    print(json.dumps(electric_request))

    # response = Estimates.create_estimate_request(electric_request)
    # print(response)

