from typing import Literal, cast

TokenApiKeyType = Literal["PGP_KEY", "SERVICE_ACCOUNT", "SSH_KEY", "USER"]

TOKEN_API_KEY_TYPE_VALUES: set[TokenApiKeyType] = {
    "PGP_KEY",
    "SERVICE_ACCOUNT",
    "SSH_KEY",
    "USER",
}


def check_token_api_key_type(value: str) -> TokenApiKeyType:
    if value in TOKEN_API_KEY_TYPE_VALUES:
        return cast(TokenApiKeyType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TOKEN_API_KEY_TYPE_VALUES!r}")
