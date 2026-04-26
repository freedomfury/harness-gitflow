from typing import Literal, cast

DelegateListResponseAutoUpgrade = Literal["DETECTING", "OFF", "ON"]

DELEGATE_LIST_RESPONSE_AUTO_UPGRADE_VALUES: set[DelegateListResponseAutoUpgrade] = {
    "DETECTING",
    "OFF",
    "ON",
}


def check_delegate_list_response_auto_upgrade(value: str) -> DelegateListResponseAutoUpgrade:
    if value in DELEGATE_LIST_RESPONSE_AUTO_UPGRADE_VALUES:
        return cast(DelegateListResponseAutoUpgrade, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DELEGATE_LIST_RESPONSE_AUTO_UPGRADE_VALUES!r}")
