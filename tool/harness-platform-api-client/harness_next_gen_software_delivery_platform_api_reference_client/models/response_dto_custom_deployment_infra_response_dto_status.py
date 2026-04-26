from typing import Literal, cast

ResponseDTOCustomDeploymentInfraResponseDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_CUSTOM_DEPLOYMENT_INFRA_RESPONSE_DTO_STATUS_VALUES: set[
    ResponseDTOCustomDeploymentInfraResponseDTOStatus
] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_custom_deployment_infra_response_dto_status(
    value: str,
) -> ResponseDTOCustomDeploymentInfraResponseDTOStatus:
    if value in RESPONSE_DTO_CUSTOM_DEPLOYMENT_INFRA_RESPONSE_DTO_STATUS_VALUES:
        return cast(ResponseDTOCustomDeploymentInfraResponseDTOStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_CUSTOM_DEPLOYMENT_INFRA_RESPONSE_DTO_STATUS_VALUES!r}"
    )
