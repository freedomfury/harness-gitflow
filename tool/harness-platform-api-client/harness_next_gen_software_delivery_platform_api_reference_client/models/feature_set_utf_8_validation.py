from typing import Literal, cast

FeatureSetUtf8Validation = Literal["NONE", "UTF8_VALIDATION_UNKNOWN", "VERIFY"]

FEATURE_SET_UTF_8_VALIDATION_VALUES: set[FeatureSetUtf8Validation] = {
    "NONE",
    "UTF8_VALIDATION_UNKNOWN",
    "VERIFY",
}


def check_feature_set_utf_8_validation(value: str) -> FeatureSetUtf8Validation:
    if value in FEATURE_SET_UTF_8_VALIDATION_VALUES:
        return cast(FeatureSetUtf8Validation, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FEATURE_SET_UTF_8_VALIDATION_VALUES!r}")
