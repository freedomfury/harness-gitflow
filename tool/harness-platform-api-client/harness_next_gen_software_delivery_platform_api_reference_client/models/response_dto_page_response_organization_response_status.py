from typing import Literal, cast

ResponseDTOPageResponseOrganizationResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_ORGANIZATION_RESPONSE_STATUS_VALUES: set[
    ResponseDTOPageResponseOrganizationResponseStatus
] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_organization_response_status(
    value: str,
) -> ResponseDTOPageResponseOrganizationResponseStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_ORGANIZATION_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOPageResponseOrganizationResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_ORGANIZATION_RESPONSE_STATUS_VALUES!r}"
    )
