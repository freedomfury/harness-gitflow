from typing import Literal, cast

ResponseDTOExecutionDataResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_EXECUTION_DATA_RESPONSE_STATUS_VALUES: set[ResponseDTOExecutionDataResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_execution_data_response_status(value: str) -> ResponseDTOExecutionDataResponseStatus:
    if value in RESPONSE_DTO_EXECUTION_DATA_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOExecutionDataResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_EXECUTION_DATA_RESPONSE_STATUS_VALUES!r}"
    )
