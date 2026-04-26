from typing import Literal, cast

ResponseDTOServiceUsageDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_SERVICE_USAGE_DTO_STATUS_VALUES: set[ResponseDTOServiceUsageDTOStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_service_usage_dto_status(value: str) -> ResponseDTOServiceUsageDTOStatus:
    if value in RESPONSE_DTO_SERVICE_USAGE_DTO_STATUS_VALUES:
        return cast(ResponseDTOServiceUsageDTOStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_SERVICE_USAGE_DTO_STATUS_VALUES!r}")
