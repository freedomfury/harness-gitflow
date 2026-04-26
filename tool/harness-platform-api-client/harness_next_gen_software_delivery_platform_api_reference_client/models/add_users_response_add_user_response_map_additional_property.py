from typing import Literal, cast

AddUsersResponseAddUserResponseMapAdditionalProperty = Literal[
    "FAIL",
    "USER_ADDED_SUCCESSFULLY",
    "USER_ALREADY_ADDED",
    "USER_ALREADY_INVITED",
    "USER_INVITE_NOT_REQUIRED",
    "USER_INVITED_SUCCESSFULLY",
]

ADD_USERS_RESPONSE_ADD_USER_RESPONSE_MAP_ADDITIONAL_PROPERTY_VALUES: set[
    AddUsersResponseAddUserResponseMapAdditionalProperty
] = {
    "FAIL",
    "USER_ADDED_SUCCESSFULLY",
    "USER_ALREADY_ADDED",
    "USER_ALREADY_INVITED",
    "USER_INVITE_NOT_REQUIRED",
    "USER_INVITED_SUCCESSFULLY",
}


def check_add_users_response_add_user_response_map_additional_property(
    value: str,
) -> AddUsersResponseAddUserResponseMapAdditionalProperty:
    if value in ADD_USERS_RESPONSE_ADD_USER_RESPONSE_MAP_ADDITIONAL_PROPERTY_VALUES:
        return cast(AddUsersResponseAddUserResponseMapAdditionalProperty, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_USERS_RESPONSE_ADD_USER_RESPONSE_MAP_ADDITIONAL_PROPERTY_VALUES!r}"
    )
