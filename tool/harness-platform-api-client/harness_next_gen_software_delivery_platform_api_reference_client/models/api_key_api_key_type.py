from typing import Literal, cast

ApiKeyApiKeyType = Literal["PGP_KEY", "SERVICE_ACCOUNT", "SSH_KEY", "USER"]

API_KEY_API_KEY_TYPE_VALUES: set[ApiKeyApiKeyType] = {
    "PGP_KEY",
    "SERVICE_ACCOUNT",
    "SSH_KEY",
    "USER",
}


def check_api_key_api_key_type(value: str) -> ApiKeyApiKeyType:
    if value in API_KEY_API_KEY_TYPE_VALUES:
        return cast(ApiKeyApiKeyType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_KEY_API_KEY_TYPE_VALUES!r}")
