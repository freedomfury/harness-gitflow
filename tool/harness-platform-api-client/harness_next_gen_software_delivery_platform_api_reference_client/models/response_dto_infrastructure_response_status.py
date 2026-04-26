from typing import Literal, cast

ResponseDTOInfrastructureResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_INFRASTRUCTURE_RESPONSE_STATUS_VALUES: set[ResponseDTOInfrastructureResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_infrastructure_response_status(value: str) -> ResponseDTOInfrastructureResponseStatus:
    if value in RESPONSE_DTO_INFRASTRUCTURE_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOInfrastructureResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_INFRASTRUCTURE_RESPONSE_STATUS_VALUES!r}"
    )
