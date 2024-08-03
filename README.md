# python-carbon-client

This project aims to be an unofficial `python` wrapper client to interact with [CarbonInterface API](http://carboninterface.com).

The _CarbonInterface API_ is an API to calculate carbon (CO₂) emissions estimates for common CO₂ emitting activities.

More functionality is going to be added soon.

## Setup

The inner modules depend on your valid `CARBON_INTERFACE_API_KEY` being setup.

You can get a free api key in the [CarbonInterface Developer Portal](https://www.carboninterface.com/account/api_credentials). 

```
// .env file
export CARBON_INTERFACE_API_KEY="yourApiKey"
// console
$ source .env
```

## Basic usage

```python3
from estimates import (
    ElectricityEstimateRequest, 
    Estimates,
    FlightEstimateRequest,
    FlightLeg
)
from model import (
    CabinClass, 
    Country, 
    DistanceUnit, 
    ElectricityUnit
)

if __name__ == "__main__":

    electric_request = ElectricityEstimateRequest(
        electricity_unit=ElectricityUnit.MWH,
        electricity_value=42,
        country=Country.US,
        state="fl",
    )
    response = Estimates.create_estimate_request(electric_request)
    print(response)

    flight_request = FlightEstimateRequest(
        passengers=2,
        legs=[
            FlightLeg("sfo", "yyz", CabinClass.ECONOMY),
            FlightLeg("yyz", "sfo", CabinClass.ECONOMY),
        ],
        distance_unit=DistanceUnit.KM,
    )
    response = Estimates.create_estimate_request(flight_request)
    print(response)
```

### Sample output

```json
{
  "data":
  {
    "id":"00000000-0000-0000-0000-000000000000",
    "type":"estimate",
    "attributes":
    {
      "country": "us",
      "state": "fl",
      "electricity_unit": "mwh",
      "electricity_value": 42.0,
      "estimated_at": "yyyy-MM-ddThh:mm:ss.nnnZ",
      "carbon_g": 16710476,
      "carbon_lb": 36840.29,
      "carbon_kg": 16710.48,
      "carbon_mt": 16.71
    }
  }
}
```
```jsonc
{
  "data":
  {
    "id":"e6911ca6-ab07-4abe-85fc-ff022274a74e",
    "type":"estimate",
    "attributes":
    {
      "passengers":2,
      "legs":[
        {
          "departure_airport":"SFO",
          "destination_airport":"YYZ",
          "cabin_class":"economy"
        },
        {
          "departure_airport":"YYZ",
          "destination_airport":"SFO",
          "cabin_class":"economy"
        }],
      "distance_value":7454.15,
      "distance_unit":"km",
      "estimated_at":"2024-08-03T11:08:53.284Z",
      "carbon_g":859824,
      "carbon_lb":1895.59,
      "carbon_kg":859.82,
      "carbon_mt":0.86
    }
  }
}
```