from typing import Literal, cast

KeyKeyUsageItem = Literal["AUTH", "CERTIFY", "ENCRYPT", "SIGN"]

KEY_KEY_USAGE_ITEM_VALUES: set[KeyKeyUsageItem] = {
    "AUTH",
    "CERTIFY",
    "ENCRYPT",
    "SIGN",
}


def check_key_key_usage_item(value: str) -> KeyKeyUsageItem:
    if value in KEY_KEY_USAGE_ITEM_VALUES:
        return cast(KeyKeyUsageItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {KEY_KEY_USAGE_ITEM_VALUES!r}")
