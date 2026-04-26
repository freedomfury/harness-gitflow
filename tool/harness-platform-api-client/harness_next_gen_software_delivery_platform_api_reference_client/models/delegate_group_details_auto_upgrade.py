from typing import Literal, cast

DelegateGroupDetailsAutoUpgrade = Literal["DETECTING", "OFF", "ON"]

DELEGATE_GROUP_DETAILS_AUTO_UPGRADE_VALUES: set[DelegateGroupDetailsAutoUpgrade] = {
    "DETECTING",
    "OFF",
    "ON",
}


def check_delegate_group_details_auto_upgrade(value: str) -> DelegateGroupDetailsAutoUpgrade:
    if value in DELEGATE_GROUP_DETAILS_AUTO_UPGRADE_VALUES:
        return cast(DelegateGroupDetailsAutoUpgrade, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DELEGATE_GROUP_DETAILS_AUTO_UPGRADE_VALUES!r}")
