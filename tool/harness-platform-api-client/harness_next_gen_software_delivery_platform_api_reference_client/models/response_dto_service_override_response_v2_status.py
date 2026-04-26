from typing import Literal, cast

ResponseDTOServiceOverrideResponseV2Status = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_SERVICE_OVERRIDE_RESPONSE_V2_STATUS_VALUES: set[ResponseDTOServiceOverrideResponseV2Status] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_service_override_response_v2_status(value: str) -> ResponseDTOServiceOverrideResponseV2Status:
    if value in RESPONSE_DTO_SERVICE_OVERRIDE_RESPONSE_V2_STATUS_VALUES:
        return cast(ResponseDTOServiceOverrideResponseV2Status, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_SERVICE_OVERRIDE_RESPONSE_V2_STATUS_VALUES!r}"
    )
