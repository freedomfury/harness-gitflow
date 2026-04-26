from typing import Literal, cast

UpdateFreezeStatusStatus = Literal["Disabled", "Enabled"]

UPDATE_FREEZE_STATUS_STATUS_VALUES: set[UpdateFreezeStatusStatus] = {
    "Disabled",
    "Enabled",
}


def check_update_freeze_status_status(value: str) -> UpdateFreezeStatusStatus:
    if value in UPDATE_FREEZE_STATUS_STATUS_VALUES:
        return cast(UpdateFreezeStatusStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_FREEZE_STATUS_STATUS_VALUES!r}")
