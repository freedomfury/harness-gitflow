from typing import Literal, cast

FeatureSetOrBuilderUtf8Validation = Literal["NONE", "UTF8_VALIDATION_UNKNOWN", "VERIFY"]

FEATURE_SET_OR_BUILDER_UTF_8_VALIDATION_VALUES: set[FeatureSetOrBuilderUtf8Validation] = {
    "NONE",
    "UTF8_VALIDATION_UNKNOWN",
    "VERIFY",
}


def check_feature_set_or_builder_utf_8_validation(value: str) -> FeatureSetOrBuilderUtf8Validation:
    if value in FEATURE_SET_OR_BUILDER_UTF_8_VALIDATION_VALUES:
        return cast(FeatureSetOrBuilderUtf8Validation, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FEATURE_SET_OR_BUILDER_UTF_8_VALIDATION_VALUES!r}")
