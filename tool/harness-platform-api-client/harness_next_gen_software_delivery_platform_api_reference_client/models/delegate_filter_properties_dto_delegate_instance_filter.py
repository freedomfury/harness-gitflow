from typing import Literal, cast

DelegateFilterPropertiesDTODelegateInstanceFilter = Literal["AVAILABLE", "EXPIRED"]

DELEGATE_FILTER_PROPERTIES_DTO_DELEGATE_INSTANCE_FILTER_VALUES: set[
    DelegateFilterPropertiesDTODelegateInstanceFilter
] = {
    "AVAILABLE",
    "EXPIRED",
}


def check_delegate_filter_properties_dto_delegate_instance_filter(
    value: str,
) -> DelegateFilterPropertiesDTODelegateInstanceFilter:
    if value in DELEGATE_FILTER_PROPERTIES_DTO_DELEGATE_INSTANCE_FILTER_VALUES:
        return cast(DelegateFilterPropertiesDTODelegateInstanceFilter, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DELEGATE_FILTER_PROPERTIES_DTO_DELEGATE_INSTANCE_FILTER_VALUES!r}"
    )
