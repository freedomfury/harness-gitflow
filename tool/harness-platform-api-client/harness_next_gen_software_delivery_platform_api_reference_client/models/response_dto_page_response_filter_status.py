from typing import Literal, cast

ResponseDTOPageResponseFilterStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_FILTER_STATUS_VALUES: set[ResponseDTOPageResponseFilterStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_filter_status(value: str) -> ResponseDTOPageResponseFilterStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_FILTER_STATUS_VALUES:
        return cast(ResponseDTOPageResponseFilterStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_FILTER_STATUS_VALUES!r}")
