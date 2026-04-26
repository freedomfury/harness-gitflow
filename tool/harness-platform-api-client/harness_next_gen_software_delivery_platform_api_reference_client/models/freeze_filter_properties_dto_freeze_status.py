from typing import Literal, cast

FreezeFilterPropertiesDTOFreezeStatus = Literal["Disabled", "Enabled"]

FREEZE_FILTER_PROPERTIES_DTO_FREEZE_STATUS_VALUES: set[FreezeFilterPropertiesDTOFreezeStatus] = {
    "Disabled",
    "Enabled",
}


def check_freeze_filter_properties_dto_freeze_status(value: str) -> FreezeFilterPropertiesDTOFreezeStatus:
    if value in FREEZE_FILTER_PROPERTIES_DTO_FREEZE_STATUS_VALUES:
        return cast(FreezeFilterPropertiesDTOFreezeStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FREEZE_FILTER_PROPERTIES_DTO_FREEZE_STATUS_VALUES!r}"
    )
