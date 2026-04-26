from typing import Literal, cast

OverrideRequestType = Literal[
    "CLUSTER_GLOBAL_OVERRIDE",
    "CLUSTER_SERVICE_OVERRIDE",
    "ENV_GLOBAL_OVERRIDE",
    "ENV_SERVICE_OVERRIDE",
    "INFRA_GLOBAL_OVERRIDE",
    "INFRA_SERVICE_OVERRIDE",
]

OVERRIDE_REQUEST_TYPE_VALUES: set[OverrideRequestType] = {
    "CLUSTER_GLOBAL_OVERRIDE",
    "CLUSTER_SERVICE_OVERRIDE",
    "ENV_GLOBAL_OVERRIDE",
    "ENV_SERVICE_OVERRIDE",
    "INFRA_GLOBAL_OVERRIDE",
    "INFRA_SERVICE_OVERRIDE",
}


def check_override_request_type(value: str) -> OverrideRequestType:
    if value in OVERRIDE_REQUEST_TYPE_VALUES:
        return cast(OverrideRequestType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OVERRIDE_REQUEST_TYPE_VALUES!r}")
