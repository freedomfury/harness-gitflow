from typing import Literal, cast

ResponseDTOPageResponseServiceAccountAggregateStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_SERVICE_ACCOUNT_AGGREGATE_STATUS_VALUES: set[
    ResponseDTOPageResponseServiceAccountAggregateStatus
] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_service_account_aggregate_status(
    value: str,
) -> ResponseDTOPageResponseServiceAccountAggregateStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_SERVICE_ACCOUNT_AGGREGATE_STATUS_VALUES:
        return cast(ResponseDTOPageResponseServiceAccountAggregateStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_SERVICE_ACCOUNT_AGGREGATE_STATUS_VALUES!r}"
    )
