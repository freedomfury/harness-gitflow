from typing import Literal, cast

DelegateFilterPropertiesDTOStatus = Literal[
    "CONNECTED", "DELETED", "DISABLED", "DISCONNECTED", "ENABLED", "WAITING_FOR_APPROVAL"
]

DELEGATE_FILTER_PROPERTIES_DTO_STATUS_VALUES: set[DelegateFilterPropertiesDTOStatus] = {
    "CONNECTED",
    "DELETED",
    "DISABLED",
    "DISCONNECTED",
    "ENABLED",
    "WAITING_FOR_APPROVAL",
}


def check_delegate_filter_properties_dto_status(value: str) -> DelegateFilterPropertiesDTOStatus:
    if value in DELEGATE_FILTER_PROPERTIES_DTO_STATUS_VALUES:
        return cast(DelegateFilterPropertiesDTOStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DELEGATE_FILTER_PROPERTIES_DTO_STATUS_VALUES!r}")
