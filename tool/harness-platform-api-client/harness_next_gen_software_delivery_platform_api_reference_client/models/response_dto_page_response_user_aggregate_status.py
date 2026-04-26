from typing import Literal, cast

ResponseDTOPageResponseUserAggregateStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_USER_AGGREGATE_STATUS_VALUES: set[ResponseDTOPageResponseUserAggregateStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_user_aggregate_status(value: str) -> ResponseDTOPageResponseUserAggregateStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_USER_AGGREGATE_STATUS_VALUES:
        return cast(ResponseDTOPageResponseUserAggregateStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_USER_AGGREGATE_STATUS_VALUES!r}"
    )
