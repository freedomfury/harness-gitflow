from typing import Literal, cast

RotateTokenApiKeyType = Literal["PGP_KEY", "SERVICE_ACCOUNT", "SSH_KEY", "USER"]

ROTATE_TOKEN_API_KEY_TYPE_VALUES: set[RotateTokenApiKeyType] = {
    "PGP_KEY",
    "SERVICE_ACCOUNT",
    "SSH_KEY",
    "USER",
}


def check_rotate_token_api_key_type(value: str) -> RotateTokenApiKeyType:
    if value in ROTATE_TOKEN_API_KEY_TYPE_VALUES:
        return cast(RotateTokenApiKeyType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROTATE_TOKEN_API_KEY_TYPE_VALUES!r}")
