from typing import Literal, cast

ClusterResponseScope = Literal["ACCOUNT", "ORGANIZATION", "PROJECT"]

CLUSTER_RESPONSE_SCOPE_VALUES: set[ClusterResponseScope] = {
    "ACCOUNT",
    "ORGANIZATION",
    "PROJECT",
}


def check_cluster_response_scope(value: str) -> ClusterResponseScope:
    if value in CLUSTER_RESPONSE_SCOPE_VALUES:
        return cast(ClusterResponseScope, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CLUSTER_RESPONSE_SCOPE_VALUES!r}")
