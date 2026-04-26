from typing import Literal, cast

ClusterBasicDTOScope = Literal["ACCOUNT", "ORGANIZATION", "PROJECT"]

CLUSTER_BASIC_DTO_SCOPE_VALUES: set[ClusterBasicDTOScope] = {
    "ACCOUNT",
    "ORGANIZATION",
    "PROJECT",
}


def check_cluster_basic_dto_scope(value: str) -> ClusterBasicDTOScope:
    if value in CLUSTER_BASIC_DTO_SCOPE_VALUES:
        return cast(ClusterBasicDTOScope, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CLUSTER_BASIC_DTO_SCOPE_VALUES!r}")
