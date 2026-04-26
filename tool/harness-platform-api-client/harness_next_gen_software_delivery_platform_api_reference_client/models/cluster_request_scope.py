from typing import Literal, cast

ClusterRequestScope = Literal["ACCOUNT", "ORGANIZATION", "PROJECT"]

CLUSTER_REQUEST_SCOPE_VALUES: set[ClusterRequestScope] = {
    "ACCOUNT",
    "ORGANIZATION",
    "PROJECT",
}


def check_cluster_request_scope(value: str) -> ClusterRequestScope:
    if value in CLUSTER_REQUEST_SCOPE_VALUES:
        return cast(ClusterRequestScope, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CLUSTER_REQUEST_SCOPE_VALUES!r}")
