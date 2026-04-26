from typing import Literal, cast

DeleteClusterScope = Literal["ACCOUNT", "ORGANIZATION", "PROJECT"]

DELETE_CLUSTER_SCOPE_VALUES: set[DeleteClusterScope] = {
    "ACCOUNT",
    "ORGANIZATION",
    "PROJECT",
}


def check_delete_cluster_scope(value: str) -> DeleteClusterScope:
    if value in DELETE_CLUSTER_SCOPE_VALUES:
        return cast(DeleteClusterScope, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DELETE_CLUSTER_SCOPE_VALUES!r}")
