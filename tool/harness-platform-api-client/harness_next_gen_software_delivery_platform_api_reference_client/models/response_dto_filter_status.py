from typing import Literal, cast

ResponseDTOFilterStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_FILTER_STATUS_VALUES: set[ResponseDTOFilterStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_filter_status(value: str) -> ResponseDTOFilterStatus:
    if value in RESPONSE_DTO_FILTER_STATUS_VALUES:
        return cast(ResponseDTOFilterStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_FILTER_STATUS_VALUES!r}")
