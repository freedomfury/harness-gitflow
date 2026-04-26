from typing import Literal, cast

DelegateGroupDetailsDelegateGroupVersionStatus = Literal["ACTIVE", "EXPIRED", "EXPIRING", "UNSUPPORTED"]

DELEGATE_GROUP_DETAILS_DELEGATE_GROUP_VERSION_STATUS_VALUES: set[DelegateGroupDetailsDelegateGroupVersionStatus] = {
    "ACTIVE",
    "EXPIRED",
    "EXPIRING",
    "UNSUPPORTED",
}


def check_delegate_group_details_delegate_group_version_status(
    value: str,
) -> DelegateGroupDetailsDelegateGroupVersionStatus:
    if value in DELEGATE_GROUP_DETAILS_DELEGATE_GROUP_VERSION_STATUS_VALUES:
        return cast(DelegateGroupDetailsDelegateGroupVersionStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DELEGATE_GROUP_DETAILS_DELEGATE_GROUP_VERSION_STATUS_VALUES!r}"
    )
