from typing import Literal, cast

ResponseDTOCustomDeploymentVariableResponseDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_CUSTOM_DEPLOYMENT_VARIABLE_RESPONSE_DTO_STATUS_VALUES: set[
    ResponseDTOCustomDeploymentVariableResponseDTOStatus
] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_custom_deployment_variable_response_dto_status(
    value: str,
) -> ResponseDTOCustomDeploymentVariableResponseDTOStatus:
    if value in RESPONSE_DTO_CUSTOM_DEPLOYMENT_VARIABLE_RESPONSE_DTO_STATUS_VALUES:
        return cast(ResponseDTOCustomDeploymentVariableResponseDTOStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_CUSTOM_DEPLOYMENT_VARIABLE_RESPONSE_DTO_STATUS_VALUES!r}"
    )
