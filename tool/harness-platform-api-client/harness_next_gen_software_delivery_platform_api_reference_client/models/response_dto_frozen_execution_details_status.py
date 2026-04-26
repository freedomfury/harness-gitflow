from typing import Literal, cast

ResponseDTOFrozenExecutionDetailsStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_FROZEN_EXECUTION_DETAILS_STATUS_VALUES: set[ResponseDTOFrozenExecutionDetailsStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_frozen_execution_details_status(value: str) -> ResponseDTOFrozenExecutionDetailsStatus:
    if value in RESPONSE_DTO_FROZEN_EXECUTION_DETAILS_STATUS_VALUES:
        return cast(ResponseDTOFrozenExecutionDetailsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_FROZEN_EXECUTION_DETAILS_STATUS_VALUES!r}"
    )
