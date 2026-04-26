from typing import Literal, cast

ServiceOverrideResponseV2Type = Literal[
    "CLUSTER_GLOBAL_OVERRIDE",
    "CLUSTER_SERVICE_OVERRIDE",
    "ENV_GLOBAL_OVERRIDE",
    "ENV_SERVICE_OVERRIDE",
    "INFRA_GLOBAL_OVERRIDE",
    "INFRA_SERVICE_OVERRIDE",
]

SERVICE_OVERRIDE_RESPONSE_V2_TYPE_VALUES: set[ServiceOverrideResponseV2Type] = {
    "CLUSTER_GLOBAL_OVERRIDE",
    "CLUSTER_SERVICE_OVERRIDE",
    "ENV_GLOBAL_OVERRIDE",
    "ENV_SERVICE_OVERRIDE",
    "INFRA_GLOBAL_OVERRIDE",
    "INFRA_SERVICE_OVERRIDE",
}


def check_service_override_response_v2_type(value: str) -> ServiceOverrideResponseV2Type:
    if value in SERVICE_OVERRIDE_RESPONSE_V2_TYPE_VALUES:
        return cast(ServiceOverrideResponseV2Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SERVICE_OVERRIDE_RESPONSE_V2_TYPE_VALUES!r}")
