from typing import Literal, cast

ResponseDTOManualExecutionResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_MANUAL_EXECUTION_RESPONSE_STATUS_VALUES: set[ResponseDTOManualExecutionResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_manual_execution_response_status(value: str) -> ResponseDTOManualExecutionResponseStatus:
    if value in RESPONSE_DTO_MANUAL_EXECUTION_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOManualExecutionResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_MANUAL_EXECUTION_RESPONSE_STATUS_VALUES!r}"
    )
