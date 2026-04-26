from typing import Literal, cast

K8SConfigDetailsK8SPermissionType = Literal["CLUSTER_ADMIN", "CLUSTER_VIEWER", "NAMESPACE_ADMIN"]

K8S_CONFIG_DETAILS_K8S_PERMISSION_TYPE_VALUES: set[K8SConfigDetailsK8SPermissionType] = {
    "CLUSTER_ADMIN",
    "CLUSTER_VIEWER",
    "NAMESPACE_ADMIN",
}


def check_k8s_config_details_k8s_permission_type(value: str) -> K8SConfigDetailsK8SPermissionType:
    if value in K8S_CONFIG_DETAILS_K8S_PERMISSION_TYPE_VALUES:
        return cast(K8SConfigDetailsK8SPermissionType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_CONFIG_DETAILS_K8S_PERMISSION_TYPE_VALUES!r}")
