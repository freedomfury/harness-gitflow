from typing import Literal, cast

ResponseDTOPageResponseApiKeyAggregateStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_API_KEY_AGGREGATE_STATUS_VALUES: set[ResponseDTOPageResponseApiKeyAggregateStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_api_key_aggregate_status(
    value: str,
) -> ResponseDTOPageResponseApiKeyAggregateStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_API_KEY_AGGREGATE_STATUS_VALUES:
        return cast(ResponseDTOPageResponseApiKeyAggregateStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_API_KEY_AGGREGATE_STATUS_VALUES!r}"
    )
