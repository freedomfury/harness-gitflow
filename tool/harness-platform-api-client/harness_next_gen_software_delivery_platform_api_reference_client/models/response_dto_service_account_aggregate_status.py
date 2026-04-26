from typing import Literal, cast

ResponseDTOServiceAccountAggregateStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_SERVICE_ACCOUNT_AGGREGATE_STATUS_VALUES: set[ResponseDTOServiceAccountAggregateStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_service_account_aggregate_status(value: str) -> ResponseDTOServiceAccountAggregateStatus:
    if value in RESPONSE_DTO_SERVICE_ACCOUNT_AGGREGATE_STATUS_VALUES:
        return cast(ResponseDTOServiceAccountAggregateStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_SERVICE_ACCOUNT_AGGREGATE_STATUS_VALUES!r}"
    )
