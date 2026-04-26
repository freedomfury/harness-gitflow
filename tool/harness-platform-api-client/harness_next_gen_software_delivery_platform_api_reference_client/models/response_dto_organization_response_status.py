from typing import Literal, cast

ResponseDTOOrganizationResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_ORGANIZATION_RESPONSE_STATUS_VALUES: set[ResponseDTOOrganizationResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_organization_response_status(value: str) -> ResponseDTOOrganizationResponseStatus:
    if value in RESPONSE_DTO_ORGANIZATION_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOOrganizationResponseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_ORGANIZATION_RESPONSE_STATUS_VALUES!r}")
