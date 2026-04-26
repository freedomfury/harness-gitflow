from typing import Literal, cast

ResponseDTOBooleanStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_BOOLEAN_STATUS_VALUES: set[ResponseDTOBooleanStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_boolean_status(value: str) -> ResponseDTOBooleanStatus:
    if value in RESPONSE_DTO_BOOLEAN_STATUS_VALUES:
        return cast(ResponseDTOBooleanStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_BOOLEAN_STATUS_VALUES!r}")
