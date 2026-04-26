from typing import Literal, cast

ResponseDTOApiKeyAggregateStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_API_KEY_AGGREGATE_STATUS_VALUES: set[ResponseDTOApiKeyAggregateStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_api_key_aggregate_status(value: str) -> ResponseDTOApiKeyAggregateStatus:
    if value in RESPONSE_DTO_API_KEY_AGGREGATE_STATUS_VALUES:
        return cast(ResponseDTOApiKeyAggregateStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_API_KEY_AGGREGATE_STATUS_VALUES!r}")
