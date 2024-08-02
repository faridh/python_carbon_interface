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
from estimates import ElectricityEstimateRequest, Estimates
from model.country import Country
from model.electricity_unit import ElectricityUnit

if __name__ == "__main__":

    electric_request = ElectricityEstimateRequest(
        ElectricityUnit.MWH, 42, Country.US, "fl"
    )

    response = Estimates.create_estimate_request(electric_request)
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