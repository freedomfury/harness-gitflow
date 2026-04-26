from typing import Literal, cast

DeleteApiKeyApiKeyType = Literal["PGP_KEY", "SERVICE_ACCOUNT", "SSH_KEY", "USER"]

DELETE_API_KEY_API_KEY_TYPE_VALUES: set[DeleteApiKeyApiKeyType] = {
    "PGP_KEY",
    "SERVICE_ACCOUNT",
    "SSH_KEY",
    "USER",
}


def check_delete_api_key_api_key_type(value: str) -> DeleteApiKeyApiKeyType:
    if value in DELETE_API_KEY_API_KEY_TYPE_VALUES:
        return cast(DeleteApiKeyApiKeyType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DELETE_API_KEY_API_KEY_TYPE_VALUES!r}")
