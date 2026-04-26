from typing import Literal, cast

GetCgDelegateTokensStatus = Literal["ACTIVE", "REVOKED"]

GET_CG_DELEGATE_TOKENS_STATUS_VALUES: set[GetCgDelegateTokensStatus] = {
    "ACTIVE",
    "REVOKED",
}


def check_get_cg_delegate_tokens_status(value: str) -> GetCgDelegateTokensStatus:
    if value in GET_CG_DELEGATE_TOKENS_STATUS_VALUES:
        return cast(GetCgDelegateTokensStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_CG_DELEGATE_TOKENS_STATUS_VALUES!r}")
