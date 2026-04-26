from typing import Literal, cast

CustomHealthConnectorDTOMethod = Literal["GET", "POST"]

CUSTOM_HEALTH_CONNECTOR_DTO_METHOD_VALUES: set[CustomHealthConnectorDTOMethod] = {
    "GET",
    "POST",
}


def check_custom_health_connector_dto_method(value: str) -> CustomHealthConnectorDTOMethod:
    if value in CUSTOM_HEALTH_CONNECTOR_DTO_METHOD_VALUES:
        return cast(CustomHealthConnectorDTOMethod, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CUSTOM_HEALTH_CONNECTOR_DTO_METHOD_VALUES!r}")
