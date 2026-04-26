from typing import Literal, cast

ResponseDTOCustomDeploymentRefreshYamlDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_CUSTOM_DEPLOYMENT_REFRESH_YAML_DTO_STATUS_VALUES: set[ResponseDTOCustomDeploymentRefreshYamlDTOStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_custom_deployment_refresh_yaml_dto_status(
    value: str,
) -> ResponseDTOCustomDeploymentRefreshYamlDTOStatus:
    if value in RESPONSE_DTO_CUSTOM_DEPLOYMENT_REFRESH_YAML_DTO_STATUS_VALUES:
        return cast(ResponseDTOCustomDeploymentRefreshYamlDTOStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_CUSTOM_DEPLOYMENT_REFRESH_YAML_DTO_STATUS_VALUES!r}"
    )
