from typing import Literal, cast

ExtensionRangeOptionsVerification = Literal["DECLARATION", "UNVERIFIED"]

EXTENSION_RANGE_OPTIONS_VERIFICATION_VALUES: set[ExtensionRangeOptionsVerification] = {
    "DECLARATION",
    "UNVERIFIED",
}


def check_extension_range_options_verification(value: str) -> ExtensionRangeOptionsVerification:
    if value in EXTENSION_RANGE_OPTIONS_VERIFICATION_VALUES:
        return cast(ExtensionRangeOptionsVerification, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EXTENSION_RANGE_OPTIONS_VERIFICATION_VALUES!r}")
