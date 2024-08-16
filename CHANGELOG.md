# 0.0.1

- Initial release with limited functionality.
    - Adds modules to interact with Request/Responses of `Electricity`, `Flight` and `Shipping` types.
    - Adds models to interact with `/vehicle_makes` and `/*/*/vehicle_models`.
    - Adds `vehicle` modules to interact with Request/Responses of `Vehicle` types.
    - Adds _fuel_ enums to `model` module.
    - Adds retry capabilities to `client` module.
    - Adds capability to handle different HTTP codes in the `client` module.
    - Removes `json_fix`, adds basic serialization logic for classes deriving from `EstimateRequest`.
