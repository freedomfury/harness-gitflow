from typing import Literal, cast

ResponseDTOUserAggregateStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_USER_AGGREGATE_STATUS_VALUES: set[ResponseDTOUserAggregateStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_user_aggregate_status(value: str) -> ResponseDTOUserAggregateStatus:
    if value in RESPONSE_DTO_USER_AGGREGATE_STATUS_VALUES:
        return cast(ResponseDTOUserAggregateStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_USER_AGGREGATE_STATUS_VALUES!r}")
