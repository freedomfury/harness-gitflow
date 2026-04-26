from typing import Literal, cast

ResponseDTOListConnectorResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_LIST_CONNECTOR_RESPONSE_STATUS_VALUES: set[ResponseDTOListConnectorResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_list_connector_response_status(value: str) -> ResponseDTOListConnectorResponseStatus:
    if value in RESPONSE_DTO_LIST_CONNECTOR_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOListConnectorResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_LIST_CONNECTOR_RESPONSE_STATUS_VALUES!r}"
    )
