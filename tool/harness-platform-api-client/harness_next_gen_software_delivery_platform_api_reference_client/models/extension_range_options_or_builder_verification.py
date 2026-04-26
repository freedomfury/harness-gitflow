from typing import Literal, cast

ExtensionRangeOptionsOrBuilderVerification = Literal["DECLARATION", "UNVERIFIED"]

EXTENSION_RANGE_OPTIONS_OR_BUILDER_VERIFICATION_VALUES: set[ExtensionRangeOptionsOrBuilderVerification] = {
    "DECLARATION",
    "UNVERIFIED",
}


def check_extension_range_options_or_builder_verification(value: str) -> ExtensionRangeOptionsOrBuilderVerification:
    if value in EXTENSION_RANGE_OPTIONS_OR_BUILDER_VERIFICATION_VALUES:
        return cast(ExtensionRangeOptionsOrBuilderVerification, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EXTENSION_RANGE_OPTIONS_OR_BUILDER_VERIFICATION_VALUES!r}"
    )
