from typing import Literal, cast

ResponseDTOExecutionGraphStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_EXECUTION_GRAPH_STATUS_VALUES: set[ResponseDTOExecutionGraphStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_execution_graph_status(value: str) -> ResponseDTOExecutionGraphStatus:
    if value in RESPONSE_DTO_EXECUTION_GRAPH_STATUS_VALUES:
        return cast(ResponseDTOExecutionGraphStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_EXECUTION_GRAPH_STATUS_VALUES!r}")
