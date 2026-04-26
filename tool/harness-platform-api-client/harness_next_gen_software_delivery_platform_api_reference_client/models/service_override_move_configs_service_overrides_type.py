from typing import Literal, cast

ServiceOverrideMoveConfigsServiceOverridesType = Literal[
    "CLUSTER_GLOBAL_OVERRIDE",
    "CLUSTER_SERVICE_OVERRIDE",
    "ENV_GLOBAL_OVERRIDE",
    "ENV_SERVICE_OVERRIDE",
    "INFRA_GLOBAL_OVERRIDE",
    "INFRA_SERVICE_OVERRIDE",
]

SERVICE_OVERRIDE_MOVE_CONFIGS_SERVICE_OVERRIDES_TYPE_VALUES: set[ServiceOverrideMoveConfigsServiceOverridesType] = {
    "CLUSTER_GLOBAL_OVERRIDE",
    "CLUSTER_SERVICE_OVERRIDE",
    "ENV_GLOBAL_OVERRIDE",
    "ENV_SERVICE_OVERRIDE",
    "INFRA_GLOBAL_OVERRIDE",
    "INFRA_SERVICE_OVERRIDE",
}


def check_service_override_move_configs_service_overrides_type(
    value: str,
) -> ServiceOverrideMoveConfigsServiceOverridesType:
    if value in SERVICE_OVERRIDE_MOVE_CONFIGS_SERVICE_OVERRIDES_TYPE_VALUES:
        return cast(ServiceOverrideMoveConfigsServiceOverridesType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SERVICE_OVERRIDE_MOVE_CONFIGS_SERVICE_OVERRIDES_TYPE_VALUES!r}"
    )
