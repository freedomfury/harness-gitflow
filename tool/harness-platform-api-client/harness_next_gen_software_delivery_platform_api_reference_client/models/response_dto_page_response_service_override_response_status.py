from typing import Literal, cast

ResponseDTOPageResponseServiceOverrideResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_SERVICE_OVERRIDE_RESPONSE_STATUS_VALUES: set[
    ResponseDTOPageResponseServiceOverrideResponseStatus
] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_service_override_response_status(
    value: str,
) -> ResponseDTOPageResponseServiceOverrideResponseStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_SERVICE_OVERRIDE_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOPageResponseServiceOverrideResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_SERVICE_OVERRIDE_RESPONSE_STATUS_VALUES!r}"
    )
