from typing import Literal, cast

EditionDefaultOrBuilderEdition = Literal[
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

EDITION_DEFAULT_OR_BUILDER_EDITION_VALUES: set[EditionDefaultOrBuilderEdition] = {
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


def check_edition_default_or_builder_edition(value: str) -> EditionDefaultOrBuilderEdition:
    if value in EDITION_DEFAULT_OR_BUILDER_EDITION_VALUES:
        return cast(EditionDefaultOrBuilderEdition, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EDITION_DEFAULT_OR_BUILDER_EDITION_VALUES!r}")
