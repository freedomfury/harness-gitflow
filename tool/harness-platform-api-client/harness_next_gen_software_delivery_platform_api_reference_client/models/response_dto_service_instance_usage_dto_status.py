from typing import Literal, cast

ResponseDTOServiceInstanceUsageDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_SERVICE_INSTANCE_USAGE_DTO_STATUS_VALUES: set[ResponseDTOServiceInstanceUsageDTOStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_service_instance_usage_dto_status(value: str) -> ResponseDTOServiceInstanceUsageDTOStatus:
    if value in RESPONSE_DTO_SERVICE_INSTANCE_USAGE_DTO_STATUS_VALUES:
        return cast(ResponseDTOServiceInstanceUsageDTOStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_SERVICE_INSTANCE_USAGE_DTO_STATUS_VALUES!r}"
    )
