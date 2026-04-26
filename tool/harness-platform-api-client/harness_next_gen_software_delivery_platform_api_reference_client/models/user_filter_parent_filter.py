from typing import Literal, cast

UserFilterParentFilter = Literal["INCLUDE_PARENT_SCOPES", "NO_PARENT_SCOPES", "STRICTLY_PARENT_SCOPES"]

USER_FILTER_PARENT_FILTER_VALUES: set[UserFilterParentFilter] = {
    "INCLUDE_PARENT_SCOPES",
    "NO_PARENT_SCOPES",
    "STRICTLY_PARENT_SCOPES",
}


def check_user_filter_parent_filter(value: str) -> UserFilterParentFilter:
    if value in USER_FILTER_PARENT_FILTER_VALUES:
        return cast(UserFilterParentFilter, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_FILTER_PARENT_FILTER_VALUES!r}")
