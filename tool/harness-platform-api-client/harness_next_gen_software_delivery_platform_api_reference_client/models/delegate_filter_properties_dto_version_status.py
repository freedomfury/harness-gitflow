from typing import Literal, cast

DelegateFilterPropertiesDTOVersionStatus = Literal["ACTIVE", "EXPIRED", "EXPIRING", "UNSUPPORTED"]

DELEGATE_FILTER_PROPERTIES_DTO_VERSION_STATUS_VALUES: set[DelegateFilterPropertiesDTOVersionStatus] = {
    "ACTIVE",
    "EXPIRED",
    "EXPIRING",
    "UNSUPPORTED",
}


def check_delegate_filter_properties_dto_version_status(value: str) -> DelegateFilterPropertiesDTOVersionStatus:
    if value in DELEGATE_FILTER_PROPERTIES_DTO_VERSION_STATUS_VALUES:
        return cast(DelegateFilterPropertiesDTOVersionStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DELEGATE_FILTER_PROPERTIES_DTO_VERSION_STATUS_VALUES!r}"
    )
