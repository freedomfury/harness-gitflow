from typing import Literal, cast

GetEnvironmentAccessListType = Literal["PreProduction", "Production"]

GET_ENVIRONMENT_ACCESS_LIST_TYPE_VALUES: set[GetEnvironmentAccessListType] = {
    "PreProduction",
    "Production",
}


def check_get_environment_access_list_type(value: str) -> GetEnvironmentAccessListType:
    if value in GET_ENVIRONMENT_ACCESS_LIST_TYPE_VALUES:
        return cast(GetEnvironmentAccessListType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_ENVIRONMENT_ACCESS_LIST_TYPE_VALUES!r}")
