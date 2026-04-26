from typing import Literal, cast

ServiceOverrideMoveConfigResponseType = Literal[
    "CLUSTER_GLOBAL_OVERRIDE",
    "CLUSTER_SERVICE_OVERRIDE",
    "ENV_GLOBAL_OVERRIDE",
    "ENV_SERVICE_OVERRIDE",
    "INFRA_GLOBAL_OVERRIDE",
    "INFRA_SERVICE_OVERRIDE",
]

SERVICE_OVERRIDE_MOVE_CONFIG_RESPONSE_TYPE_VALUES: set[ServiceOverrideMoveConfigResponseType] = {
    "CLUSTER_GLOBAL_OVERRIDE",
    "CLUSTER_SERVICE_OVERRIDE",
    "ENV_GLOBAL_OVERRIDE",
    "ENV_SERVICE_OVERRIDE",
    "INFRA_GLOBAL_OVERRIDE",
    "INFRA_SERVICE_OVERRIDE",
}


def check_service_override_move_config_response_type(value: str) -> ServiceOverrideMoveConfigResponseType:
    if value in SERVICE_OVERRIDE_MOVE_CONFIG_RESPONSE_TYPE_VALUES:
        return cast(ServiceOverrideMoveConfigResponseType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SERVICE_OVERRIDE_MOVE_CONFIG_RESPONSE_TYPE_VALUES!r}"
    )
