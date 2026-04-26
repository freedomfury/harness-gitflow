from typing import Literal, cast

DelegateTokenDetailsStatus = Literal["ACTIVE", "REVOKED"]

DELEGATE_TOKEN_DETAILS_STATUS_VALUES: set[DelegateTokenDetailsStatus] = {
    "ACTIVE",
    "REVOKED",
}


def check_delegate_token_details_status(value: str) -> DelegateTokenDetailsStatus:
    if value in DELEGATE_TOKEN_DETAILS_STATUS_VALUES:
        return cast(DelegateTokenDetailsStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DELEGATE_TOKEN_DETAILS_STATUS_VALUES!r}")
