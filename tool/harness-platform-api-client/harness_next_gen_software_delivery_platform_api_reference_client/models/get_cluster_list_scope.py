from typing import Literal, cast

GetClusterListScope = Literal["ACCOUNT", "ORGANIZATION", "PROJECT"]

GET_CLUSTER_LIST_SCOPE_VALUES: set[GetClusterListScope] = {
    "ACCOUNT",
    "ORGANIZATION",
    "PROJECT",
}


def check_get_cluster_list_scope(value: str) -> GetClusterListScope:
    if value in GET_CLUSTER_LIST_SCOPE_VALUES:
        return cast(GetClusterListScope, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_CLUSTER_LIST_SCOPE_VALUES!r}")
