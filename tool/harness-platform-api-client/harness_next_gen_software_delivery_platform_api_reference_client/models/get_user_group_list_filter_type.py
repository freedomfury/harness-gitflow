from typing import Literal, cast

GetUserGroupListFilterType = Literal[
    "EXCLUDE_INHERITED_GROUPS", "INCLUDE_CHILD_SCOPE_GROUPS", "INCLUDE_INHERITED_GROUPS", "INCLUDE_PARENT_SCOPE_GROUPS"
]

GET_USER_GROUP_LIST_FILTER_TYPE_VALUES: set[GetUserGroupListFilterType] = {
    "EXCLUDE_INHERITED_GROUPS",
    "INCLUDE_CHILD_SCOPE_GROUPS",
    "INCLUDE_INHERITED_GROUPS",
    "INCLUDE_PARENT_SCOPE_GROUPS",
}


def check_get_user_group_list_filter_type(value: str) -> GetUserGroupListFilterType:
    if value in GET_USER_GROUP_LIST_FILTER_TYPE_VALUES:
        return cast(GetUserGroupListFilterType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_USER_GROUP_LIST_FILTER_TYPE_VALUES!r}")
