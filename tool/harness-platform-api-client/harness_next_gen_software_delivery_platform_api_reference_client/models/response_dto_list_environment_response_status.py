from typing import Literal, cast

ResponseDTOListEnvironmentResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_LIST_ENVIRONMENT_RESPONSE_STATUS_VALUES: set[ResponseDTOListEnvironmentResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_list_environment_response_status(value: str) -> ResponseDTOListEnvironmentResponseStatus:
    if value in RESPONSE_DTO_LIST_ENVIRONMENT_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOListEnvironmentResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_LIST_ENVIRONMENT_RESPONSE_STATUS_VALUES!r}"
    )
