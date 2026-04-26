from typing import Literal, cast

WinRmAuthType = Literal["Kerberos", "NTLM"]

WIN_RM_AUTH_TYPE_VALUES: set[WinRmAuthType] = {
    "Kerberos",
    "NTLM",
}


def check_win_rm_auth_type(value: str) -> WinRmAuthType:
    if value in WIN_RM_AUTH_TYPE_VALUES:
        return cast(WinRmAuthType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WIN_RM_AUTH_TYPE_VALUES!r}")
