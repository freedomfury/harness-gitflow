from typing import Literal, cast

DeleteTokenApiKeyType = Literal["PGP_KEY", "SERVICE_ACCOUNT", "SSH_KEY", "USER"]

DELETE_TOKEN_API_KEY_TYPE_VALUES: set[DeleteTokenApiKeyType] = {
    "PGP_KEY",
    "SERVICE_ACCOUNT",
    "SSH_KEY",
    "USER",
}


def check_delete_token_api_key_type(value: str) -> DeleteTokenApiKeyType:
    if value in DELETE_TOKEN_API_KEY_TYPE_VALUES:
        return cast(DeleteTokenApiKeyType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DELETE_TOKEN_API_KEY_TYPE_VALUES!r}")
