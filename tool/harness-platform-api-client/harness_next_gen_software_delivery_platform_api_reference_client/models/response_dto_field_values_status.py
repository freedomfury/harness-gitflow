from typing import Literal, cast

ResponseDTOFieldValuesStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_FIELD_VALUES_STATUS_VALUES: set[ResponseDTOFieldValuesStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_field_values_status(value: str) -> ResponseDTOFieldValuesStatus:
    if value in RESPONSE_DTO_FIELD_VALUES_STATUS_VALUES:
        return cast(ResponseDTOFieldValuesStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_FIELD_VALUES_STATUS_VALUES!r}")
