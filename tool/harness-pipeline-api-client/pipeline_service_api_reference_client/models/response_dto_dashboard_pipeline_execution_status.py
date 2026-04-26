from typing import Literal, cast

ResponseDTODashboardPipelineExecutionStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_DASHBOARD_PIPELINE_EXECUTION_STATUS_VALUES: set[ResponseDTODashboardPipelineExecutionStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_dashboard_pipeline_execution_status(value: str) -> ResponseDTODashboardPipelineExecutionStatus:
    if value in RESPONSE_DTO_DASHBOARD_PIPELINE_EXECUTION_STATUS_VALUES:
        return cast(ResponseDTODashboardPipelineExecutionStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_DASHBOARD_PIPELINE_EXECUTION_STATUS_VALUES!r}"
    )
