from typing import Literal, cast

ListApiKeysApiKeyType = Literal["PGP_KEY", "SERVICE_ACCOUNT", "SSH_KEY", "USER"]

LIST_API_KEYS_API_KEY_TYPE_VALUES: set[ListApiKeysApiKeyType] = {
    "PGP_KEY",
    "SERVICE_ACCOUNT",
    "SSH_KEY",
    "USER",
}


def check_list_api_keys_api_key_type(value: str) -> ListApiKeysApiKeyType:
    if value in LIST_API_KEYS_API_KEY_TYPE_VALUES:
        return cast(ListApiKeysApiKeyType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_API_KEYS_API_KEY_TYPE_VALUES!r}")
