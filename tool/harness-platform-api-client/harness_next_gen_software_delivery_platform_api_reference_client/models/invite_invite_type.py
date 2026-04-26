from typing import Literal, cast

InviteInviteType = Literal["ADMIN_INITIATED_INVITE", "SCIM_INITIATED_INVITE", "USER_INITIATED_INVITE"]

INVITE_INVITE_TYPE_VALUES: set[InviteInviteType] = {
    "ADMIN_INITIATED_INVITE",
    "SCIM_INITIATED_INVITE",
    "USER_INITIATED_INVITE",
}


def check_invite_invite_type(value: str) -> InviteInviteType:
    if value in INVITE_INVITE_TYPE_VALUES:
        return cast(InviteInviteType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVITE_INVITE_TYPE_VALUES!r}")
