from typing import Literal, cast

ResponseDTOPageResponseConnectorResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_CONNECTOR_RESPONSE_STATUS_VALUES: set[ResponseDTOPageResponseConnectorResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_connector_response_status(
    value: str,
) -> ResponseDTOPageResponseConnectorResponseStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_CONNECTOR_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOPageResponseConnectorResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_CONNECTOR_RESPONSE_STATUS_VALUES!r}"
    )
