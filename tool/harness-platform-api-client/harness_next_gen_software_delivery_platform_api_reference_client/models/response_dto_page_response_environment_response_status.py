from typing import Literal, cast

ResponseDTOPageResponseEnvironmentResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_ENVIRONMENT_RESPONSE_STATUS_VALUES: set[ResponseDTOPageResponseEnvironmentResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_environment_response_status(
    value: str,
) -> ResponseDTOPageResponseEnvironmentResponseStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_ENVIRONMENT_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOPageResponseEnvironmentResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_ENVIRONMENT_RESPONSE_STATUS_VALUES!r}"
    )
