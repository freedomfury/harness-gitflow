from typing import Literal, cast

ResponseDTOPageResponseTokenAggregateStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_TOKEN_AGGREGATE_STATUS_VALUES: set[ResponseDTOPageResponseTokenAggregateStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_token_aggregate_status(value: str) -> ResponseDTOPageResponseTokenAggregateStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_TOKEN_AGGREGATE_STATUS_VALUES:
        return cast(ResponseDTOPageResponseTokenAggregateStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_TOKEN_AGGREGATE_STATUS_VALUES!r}"
    )
