from typing import Literal, cast

ResponseDTOWorkflowGraphStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_WORKFLOW_GRAPH_STATUS_VALUES: set[ResponseDTOWorkflowGraphStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_workflow_graph_status(value: str) -> ResponseDTOWorkflowGraphStatus:
    if value in RESPONSE_DTO_WORKFLOW_GRAPH_STATUS_VALUES:
        return cast(ResponseDTOWorkflowGraphStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_WORKFLOW_GRAPH_STATUS_VALUES!r}")
