from typing import Literal, cast

UpdateOverrideGitDetailsServiceOverridesType = Literal[
    "CLUSTER_GLOBAL_OVERRIDE",
    "CLUSTER_SERVICE_OVERRIDE",
    "ENV_GLOBAL_OVERRIDE",
    "ENV_SERVICE_OVERRIDE",
    "INFRA_GLOBAL_OVERRIDE",
    "INFRA_SERVICE_OVERRIDE",
]

UPDATE_OVERRIDE_GIT_DETAILS_SERVICE_OVERRIDES_TYPE_VALUES: set[UpdateOverrideGitDetailsServiceOverridesType] = {
    "CLUSTER_GLOBAL_OVERRIDE",
    "CLUSTER_SERVICE_OVERRIDE",
    "ENV_GLOBAL_OVERRIDE",
    "ENV_SERVICE_OVERRIDE",
    "INFRA_GLOBAL_OVERRIDE",
    "INFRA_SERVICE_OVERRIDE",
}


def check_update_override_git_details_service_overrides_type(
    value: str,
) -> UpdateOverrideGitDetailsServiceOverridesType:
    if value in UPDATE_OVERRIDE_GIT_DETAILS_SERVICE_OVERRIDES_TYPE_VALUES:
        return cast(UpdateOverrideGitDetailsServiceOverridesType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_OVERRIDE_GIT_DETAILS_SERVICE_OVERRIDES_TYPE_VALUES!r}"
    )
