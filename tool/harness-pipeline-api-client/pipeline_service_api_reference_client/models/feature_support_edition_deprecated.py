from typing import Literal, cast

FeatureSupportEditionDeprecated = Literal[
    "EDITION_1_TEST_ONLY",
    "EDITION_2023",
    "EDITION_2024",
    "EDITION_2_TEST_ONLY",
    "EDITION_99997_TEST_ONLY",
    "EDITION_99998_TEST_ONLY",
    "EDITION_99999_TEST_ONLY",
    "EDITION_LEGACY",
    "EDITION_MAX",
    "EDITION_PROTO2",
    "EDITION_PROTO3",
    "EDITION_UNKNOWN",
]

FEATURE_SUPPORT_EDITION_DEPRECATED_VALUES: set[FeatureSupportEditionDeprecated] = {
    "EDITION_1_TEST_ONLY",
    "EDITION_2023",
    "EDITION_2024",
    "EDITION_2_TEST_ONLY",
    "EDITION_99997_TEST_ONLY",
    "EDITION_99998_TEST_ONLY",
    "EDITION_99999_TEST_ONLY",
    "EDITION_LEGACY",
    "EDITION_MAX",
    "EDITION_PROTO2",
    "EDITION_PROTO3",
    "EDITION_UNKNOWN",
}


def check_feature_support_edition_deprecated(value: str) -> FeatureSupportEditionDeprecated:
    if value in FEATURE_SUPPORT_EDITION_DEPRECATED_VALUES:
        return cast(FeatureSupportEditionDeprecated, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FEATURE_SUPPORT_EDITION_DEPRECATED_VALUES!r}")
