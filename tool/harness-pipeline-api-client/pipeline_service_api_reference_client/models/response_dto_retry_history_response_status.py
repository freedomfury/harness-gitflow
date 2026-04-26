from typing import Literal, cast

ResponseDTORetryHistoryResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_RETRY_HISTORY_RESPONSE_STATUS_VALUES: set[ResponseDTORetryHistoryResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_retry_history_response_status(value: str) -> ResponseDTORetryHistoryResponseStatus:
    if value in RESPONSE_DTO_RETRY_HISTORY_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTORetryHistoryResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_RETRY_HISTORY_RESPONSE_STATUS_VALUES!r}"
    )
