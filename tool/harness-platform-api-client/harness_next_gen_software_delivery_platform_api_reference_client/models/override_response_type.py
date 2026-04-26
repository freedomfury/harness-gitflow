from typing import Literal, cast

OverrideResponseType = Literal[
    "CLUSTER_GLOBAL_OVERRIDE",
    "CLUSTER_SERVICE_OVERRIDE",
    "ENV_GLOBAL_OVERRIDE",
    "ENV_SERVICE_OVERRIDE",
    "INFRA_GLOBAL_OVERRIDE",
    "INFRA_SERVICE_OVERRIDE",
]

OVERRIDE_RESPONSE_TYPE_VALUES: set[OverrideResponseType] = {
    "CLUSTER_GLOBAL_OVERRIDE",
    "CLUSTER_SERVICE_OVERRIDE",
    "ENV_GLOBAL_OVERRIDE",
    "ENV_SERVICE_OVERRIDE",
    "INFRA_GLOBAL_OVERRIDE",
    "INFRA_SERVICE_OVERRIDE",
}


def check_override_response_type(value: str) -> OverrideResponseType:
    if value in OVERRIDE_RESPONSE_TYPE_VALUES:
        return cast(OverrideResponseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OVERRIDE_RESPONSE_TYPE_VALUES!r}")
