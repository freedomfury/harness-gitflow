from typing import Literal, cast

TokenPgpKeyUsageItem = Literal["AUTH", "CERTIFY", "ENCRYPT", "SIGN"]

TOKEN_PGP_KEY_USAGE_ITEM_VALUES: set[TokenPgpKeyUsageItem] = {
    "AUTH",
    "CERTIFY",
    "ENCRYPT",
    "SIGN",
}


def check_token_pgp_key_usage_item(value: str) -> TokenPgpKeyUsageItem:
    if value in TOKEN_PGP_KEY_USAGE_ITEM_VALUES:
        return cast(TokenPgpKeyUsageItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TOKEN_PGP_KEY_USAGE_ITEM_VALUES!r}")
