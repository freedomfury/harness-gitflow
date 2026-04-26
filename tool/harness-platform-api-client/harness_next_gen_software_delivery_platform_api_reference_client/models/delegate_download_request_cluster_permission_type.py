from typing import Literal, cast

DelegateDownloadRequestClusterPermissionType = Literal["CLUSTER_ADMIN", "CLUSTER_VIEWER", "NAMESPACE_ADMIN"]

DELEGATE_DOWNLOAD_REQUEST_CLUSTER_PERMISSION_TYPE_VALUES: set[DelegateDownloadRequestClusterPermissionType] = {
    "CLUSTER_ADMIN",
    "CLUSTER_VIEWER",
    "NAMESPACE_ADMIN",
}


def check_delegate_download_request_cluster_permission_type(value: str) -> DelegateDownloadRequestClusterPermissionType:
    if value in DELEGATE_DOWNLOAD_REQUEST_CLUSTER_PERMISSION_TYPE_VALUES:
        return cast(DelegateDownloadRequestClusterPermissionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DELEGATE_DOWNLOAD_REQUEST_CLUSTER_PERMISSION_TYPE_VALUES!r}"
    )
