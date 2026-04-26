from typing import Literal, cast

ServiceOverrideGitUpdateResponseType = Literal[
    "CLUSTER_GLOBAL_OVERRIDE",
    "CLUSTER_SERVICE_OVERRIDE",
    "ENV_GLOBAL_OVERRIDE",
    "ENV_SERVICE_OVERRIDE",
    "INFRA_GLOBAL_OVERRIDE",
    "INFRA_SERVICE_OVERRIDE",
]

SERVICE_OVERRIDE_GIT_UPDATE_RESPONSE_TYPE_VALUES: set[ServiceOverrideGitUpdateResponseType] = {
    "CLUSTER_GLOBAL_OVERRIDE",
    "CLUSTER_SERVICE_OVERRIDE",
    "ENV_GLOBAL_OVERRIDE",
    "ENV_SERVICE_OVERRIDE",
    "INFRA_GLOBAL_OVERRIDE",
    "INFRA_SERVICE_OVERRIDE",
}


def check_service_override_git_update_response_type(value: str) -> ServiceOverrideGitUpdateResponseType:
    if value in SERVICE_OVERRIDE_GIT_UPDATE_RESPONSE_TYPE_VALUES:
        return cast(ServiceOverrideGitUpdateResponseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SERVICE_OVERRIDE_GIT_UPDATE_RESPONSE_TYPE_VALUES!r}")
