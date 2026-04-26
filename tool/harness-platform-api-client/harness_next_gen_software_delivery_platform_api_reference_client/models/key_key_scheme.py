from typing import Literal, cast

KeyKeyScheme = Literal["PGP", "SSH"]

KEY_KEY_SCHEME_VALUES: set[KeyKeyScheme] = {
    "PGP",
    "SSH",
}


def check_key_key_scheme(value: str) -> KeyKeyScheme:
    if value in KEY_KEY_SCHEME_VALUES:
        return cast(KeyKeyScheme, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {KEY_KEY_SCHEME_VALUES!r}")
