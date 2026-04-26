from typing import Literal, cast

ResponseDTONodeExecutionDetailsStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_NODE_EXECUTION_DETAILS_STATUS_VALUES: set[ResponseDTONodeExecutionDetailsStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_node_execution_details_status(value: str) -> ResponseDTONodeExecutionDetailsStatus:
    if value in RESPONSE_DTO_NODE_EXECUTION_DETAILS_STATUS_VALUES:
        return cast(ResponseDTONodeExecutionDetailsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_NODE_EXECUTION_DETAILS_STATUS_VALUES!r}"
    )
