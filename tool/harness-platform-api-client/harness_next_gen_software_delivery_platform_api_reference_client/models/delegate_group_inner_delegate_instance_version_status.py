from typing import Literal, cast

DelegateGroupInnerDelegateInstanceVersionStatus = Literal["ACTIVE", "EXPIRED", "EXPIRING", "UNSUPPORTED"]

DELEGATE_GROUP_INNER_DELEGATE_INSTANCE_VERSION_STATUS_VALUES: set[DelegateGroupInnerDelegateInstanceVersionStatus] = {
    "ACTIVE",
    "EXPIRED",
    "EXPIRING",
    "UNSUPPORTED",
}


def check_delegate_group_inner_delegate_instance_version_status(
    value: str,
) -> DelegateGroupInnerDelegateInstanceVersionStatus:
    if value in DELEGATE_GROUP_INNER_DELEGATE_INSTANCE_VERSION_STATUS_VALUES:
        return cast(DelegateGroupInnerDelegateInstanceVersionStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DELEGATE_GROUP_INNER_DELEGATE_INSTANCE_VERSION_STATUS_VALUES!r}"
    )
