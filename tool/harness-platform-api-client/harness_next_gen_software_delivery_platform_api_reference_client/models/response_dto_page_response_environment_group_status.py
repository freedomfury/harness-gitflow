from typing import Literal, cast

ResponseDTOPageResponseEnvironmentGroupStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_ENVIRONMENT_GROUP_STATUS_VALUES: set[ResponseDTOPageResponseEnvironmentGroupStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_environment_group_status(
    value: str,
) -> ResponseDTOPageResponseEnvironmentGroupStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_ENVIRONMENT_GROUP_STATUS_VALUES:
        return cast(ResponseDTOPageResponseEnvironmentGroupStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_ENVIRONMENT_GROUP_STATUS_VALUES!r}"
    )
