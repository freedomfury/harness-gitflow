from typing import Literal, cast

ResponseDTOConnectorResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_CONNECTOR_RESPONSE_STATUS_VALUES: set[ResponseDTOConnectorResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_connector_response_status(value: str) -> ResponseDTOConnectorResponseStatus:
    if value in RESPONSE_DTO_CONNECTOR_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOConnectorResponseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_CONNECTOR_RESPONSE_STATUS_VALUES!r}")
