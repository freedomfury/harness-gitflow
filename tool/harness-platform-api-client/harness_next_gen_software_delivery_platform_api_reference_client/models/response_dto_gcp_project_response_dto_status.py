from typing import Literal, cast

ResponseDTOGcpProjectResponseDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_GCP_PROJECT_RESPONSE_DTO_STATUS_VALUES: set[ResponseDTOGcpProjectResponseDTOStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_gcp_project_response_dto_status(value: str) -> ResponseDTOGcpProjectResponseDTOStatus:
    if value in RESPONSE_DTO_GCP_PROJECT_RESPONSE_DTO_STATUS_VALUES:
        return cast(ResponseDTOGcpProjectResponseDTOStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_GCP_PROJECT_RESPONSE_DTO_STATUS_VALUES!r}"
    )
