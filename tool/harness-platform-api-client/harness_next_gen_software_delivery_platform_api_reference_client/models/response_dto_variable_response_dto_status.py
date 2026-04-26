from typing import Literal, cast

ResponseDTOVariableResponseDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_VARIABLE_RESPONSE_DTO_STATUS_VALUES: set[ResponseDTOVariableResponseDTOStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_variable_response_dto_status(value: str) -> ResponseDTOVariableResponseDTOStatus:
    if value in RESPONSE_DTO_VARIABLE_RESPONSE_DTO_STATUS_VALUES:
        return cast(ResponseDTOVariableResponseDTOStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_VARIABLE_RESPONSE_DTO_STATUS_VALUES!r}")
