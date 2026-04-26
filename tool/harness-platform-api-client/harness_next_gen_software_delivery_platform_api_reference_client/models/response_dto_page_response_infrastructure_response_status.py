from typing import Literal, cast

ResponseDTOPageResponseInfrastructureResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_INFRASTRUCTURE_RESPONSE_STATUS_VALUES: set[
    ResponseDTOPageResponseInfrastructureResponseStatus
] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_infrastructure_response_status(
    value: str,
) -> ResponseDTOPageResponseInfrastructureResponseStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_INFRASTRUCTURE_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOPageResponseInfrastructureResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_INFRASTRUCTURE_RESPONSE_STATUS_VALUES!r}"
    )
