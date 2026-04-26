from typing import Literal, cast

UserGroupFilterFilterType = Literal[
    "EXCLUDE_INHERITED_GROUPS", "INCLUDE_CHILD_SCOPE_GROUPS", "INCLUDE_INHERITED_GROUPS", "INCLUDE_PARENT_SCOPE_GROUPS"
]

USER_GROUP_FILTER_FILTER_TYPE_VALUES: set[UserGroupFilterFilterType] = {
    "EXCLUDE_INHERITED_GROUPS",
    "INCLUDE_CHILD_SCOPE_GROUPS",
    "INCLUDE_INHERITED_GROUPS",
    "INCLUDE_PARENT_SCOPE_GROUPS",
}


def check_user_group_filter_filter_type(value: str) -> UserGroupFilterFilterType:
    if value in USER_GROUP_FILTER_FILTER_TYPE_VALUES:
        return cast(UserGroupFilterFilterType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_GROUP_FILTER_FILTER_TYPE_VALUES!r}")
