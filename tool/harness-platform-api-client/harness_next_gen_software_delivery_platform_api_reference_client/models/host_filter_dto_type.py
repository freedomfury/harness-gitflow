from typing import Literal, cast

HostFilterDTOType = Literal["All", "HostAttributes", "HostNames"]

HOST_FILTER_DTO_TYPE_VALUES: set[HostFilterDTOType] = {
    "All",
    "HostAttributes",
    "HostNames",
}


def check_host_filter_dto_type(value: str) -> HostFilterDTOType:
    if value in HOST_FILTER_DTO_TYPE_VALUES:
        return cast(HostFilterDTOType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HOST_FILTER_DTO_TYPE_VALUES!r}")
