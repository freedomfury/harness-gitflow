from typing import Literal, cast

ListApiKeys1ApiKeyType = Literal["PGP_KEY", "SERVICE_ACCOUNT", "SSH_KEY", "USER"]

LIST_API_KEYS_1_API_KEY_TYPE_VALUES: set[ListApiKeys1ApiKeyType] = {
    "PGP_KEY",
    "SERVICE_ACCOUNT",
    "SSH_KEY",
    "USER",
}


def check_list_api_keys_1_api_key_type(value: str) -> ListApiKeys1ApiKeyType:
    if value in LIST_API_KEYS_1_API_KEY_TYPE_VALUES:
        return cast(ListApiKeys1ApiKeyType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_API_KEYS_1_API_KEY_TYPE_VALUES!r}")
