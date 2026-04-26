from typing import Literal, cast

ResponseDTOPageResponseEntitySetupUsageStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_ENTITY_SETUP_USAGE_STATUS_VALUES: set[ResponseDTOPageResponseEntitySetupUsageStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_entity_setup_usage_status(
    value: str,
) -> ResponseDTOPageResponseEntitySetupUsageStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_ENTITY_SETUP_USAGE_STATUS_VALUES:
        return cast(ResponseDTOPageResponseEntitySetupUsageStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_ENTITY_SETUP_USAGE_STATUS_VALUES!r}"
    )
