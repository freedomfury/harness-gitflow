from typing import Literal, cast

FileDescriptorProtoEdition = Literal[
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

FILE_DESCRIPTOR_PROTO_EDITION_VALUES: set[FileDescriptorProtoEdition] = {
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


def check_file_descriptor_proto_edition(value: str) -> FileDescriptorProtoEdition:
    if value in FILE_DESCRIPTOR_PROTO_EDITION_VALUES:
        return cast(FileDescriptorProtoEdition, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FILE_DESCRIPTOR_PROTO_EDITION_VALUES!r}")
