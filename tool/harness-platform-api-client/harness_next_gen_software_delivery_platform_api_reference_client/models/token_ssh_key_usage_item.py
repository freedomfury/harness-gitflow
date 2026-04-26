from typing import Literal, cast

TokenSshKeyUsageItem = Literal["AUTH", "SIGN"]

TOKEN_SSH_KEY_USAGE_ITEM_VALUES: set[TokenSshKeyUsageItem] = {
    "AUTH",
    "SIGN",
}


def check_token_ssh_key_usage_item(value: str) -> TokenSshKeyUsageItem:
    if value in TOKEN_SSH_KEY_USAGE_ITEM_VALUES:
        return cast(TokenSshKeyUsageItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TOKEN_SSH_KEY_USAGE_ITEM_VALUES!r}")
