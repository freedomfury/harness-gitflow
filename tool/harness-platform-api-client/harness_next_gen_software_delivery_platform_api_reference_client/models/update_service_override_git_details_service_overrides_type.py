from typing import Literal, cast

UpdateServiceOverrideGitDetailsServiceOverridesType = Literal[
    "CLUSTER_GLOBAL_OVERRIDE",
    "CLUSTER_SERVICE_OVERRIDE",
    "ENV_GLOBAL_OVERRIDE",
    "ENV_SERVICE_OVERRIDE",
    "INFRA_GLOBAL_OVERRIDE",
    "INFRA_SERVICE_OVERRIDE",
]

UPDATE_SERVICE_OVERRIDE_GIT_DETAILS_SERVICE_OVERRIDES_TYPE_VALUES: set[
    UpdateServiceOverrideGitDetailsServiceOverridesType
] = {
    "CLUSTER_GLOBAL_OVERRIDE",
    "CLUSTER_SERVICE_OVERRIDE",
    "ENV_GLOBAL_OVERRIDE",
    "ENV_SERVICE_OVERRIDE",
    "INFRA_GLOBAL_OVERRIDE",
    "INFRA_SERVICE_OVERRIDE",
}


def check_update_service_override_git_details_service_overrides_type(
    value: str,
) -> UpdateServiceOverrideGitDetailsServiceOverridesType:
    if value in UPDATE_SERVICE_OVERRIDE_GIT_DETAILS_SERVICE_OVERRIDES_TYPE_VALUES:
        return cast(UpdateServiceOverrideGitDetailsServiceOverridesType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_SERVICE_OVERRIDE_GIT_DETAILS_SERVICE_OVERRIDES_TYPE_VALUES!r}"
    )
