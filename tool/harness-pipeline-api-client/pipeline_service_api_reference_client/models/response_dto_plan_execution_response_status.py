from typing import Literal, cast

ResponseDTOPlanExecutionResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PLAN_EXECUTION_RESPONSE_STATUS_VALUES: set[ResponseDTOPlanExecutionResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_plan_execution_response_status(value: str) -> ResponseDTOPlanExecutionResponseStatus:
    if value in RESPONSE_DTO_PLAN_EXECUTION_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOPlanExecutionResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PLAN_EXECUTION_RESPONSE_STATUS_VALUES!r}"
    )
