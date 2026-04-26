from typing import Literal, cast

FileNodeFileUsage = Literal["CONFIG", "MANIFEST_FILE", "SCRIPT"]

FILE_NODE_FILE_USAGE_VALUES: set[FileNodeFileUsage] = {
    "CONFIG",
    "MANIFEST_FILE",
    "SCRIPT",
}


def check_file_node_file_usage(value: str) -> FileNodeFileUsage:
    if value in FILE_NODE_FILE_USAGE_VALUES:
        return cast(FileNodeFileUsage, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FILE_NODE_FILE_USAGE_VALUES!r}")
