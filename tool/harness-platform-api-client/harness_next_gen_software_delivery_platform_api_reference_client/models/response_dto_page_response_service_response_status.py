from typing import Literal, cast

ResponseDTOPageResponseServiceResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_SERVICE_RESPONSE_STATUS_VALUES: set[ResponseDTOPageResponseServiceResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_service_response_status(
    value: str,
) -> ResponseDTOPageResponseServiceResponseStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_SERVICE_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOPageResponseServiceResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_SERVICE_RESPONSE_STATUS_VALUES!r}"
    )
