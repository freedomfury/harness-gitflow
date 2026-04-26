from typing import Literal, cast

FeatureSupportOrBuilderEditionRemoved = Literal[
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

FEATURE_SUPPORT_OR_BUILDER_EDITION_REMOVED_VALUES: set[FeatureSupportOrBuilderEditionRemoved] = {
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


def check_feature_support_or_builder_edition_removed(value: str) -> FeatureSupportOrBuilderEditionRemoved:
    if value in FEATURE_SUPPORT_OR_BUILDER_EDITION_REMOVED_VALUES:
        return cast(FeatureSupportOrBuilderEditionRemoved, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FEATURE_SUPPORT_OR_BUILDER_EDITION_REMOVED_VALUES!r}"
    )
