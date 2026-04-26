from typing import Literal, cast

OverrideMoveConfigsServiceOverridesType = Literal[
    "CLUSTER_GLOBAL_OVERRIDE",
    "CLUSTER_SERVICE_OVERRIDE",
    "ENV_GLOBAL_OVERRIDE",
    "ENV_SERVICE_OVERRIDE",
    "INFRA_GLOBAL_OVERRIDE",
    "INFRA_SERVICE_OVERRIDE",
]

OVERRIDE_MOVE_CONFIGS_SERVICE_OVERRIDES_TYPE_VALUES: set[OverrideMoveConfigsServiceOverridesType] = {
    "CLUSTER_GLOBAL_OVERRIDE",
    "CLUSTER_SERVICE_OVERRIDE",
    "ENV_GLOBAL_OVERRIDE",
    "ENV_SERVICE_OVERRIDE",
    "INFRA_GLOBAL_OVERRIDE",
    "INFRA_SERVICE_OVERRIDE",
}


def check_override_move_configs_service_overrides_type(value: str) -> OverrideMoveConfigsServiceOverridesType:
    if value in OVERRIDE_MOVE_CONFIGS_SERVICE_OVERRIDES_TYPE_VALUES:
        return cast(OverrideMoveConfigsServiceOverridesType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {OVERRIDE_MOVE_CONFIGS_SERVICE_OVERRIDES_TYPE_VALUES!r}"
    )
