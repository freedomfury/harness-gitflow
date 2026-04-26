from typing import Literal, cast

AccountEdition = Literal["COMMUNITY", "DEVOPS_ESSENTIALS", "ENTERPRISE", "ESSENTIALS", "FREE", "STARTUP", "TEAM"]

ACCOUNT_EDITION_VALUES: set[AccountEdition] = {
    "COMMUNITY",
    "DEVOPS_ESSENTIALS",
    "ENTERPRISE",
    "ESSENTIALS",
    "FREE",
    "STARTUP",
    "TEAM",
}


def check_account_edition(value: str) -> AccountEdition:
    if value in ACCOUNT_EDITION_VALUES:
        return cast(AccountEdition, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACCOUNT_EDITION_VALUES!r}")
