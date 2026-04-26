from typing import Literal, cast

FileOptionsOptimizeFor = Literal["CODE_SIZE", "LITE_RUNTIME", "SPEED"]

FILE_OPTIONS_OPTIMIZE_FOR_VALUES: set[FileOptionsOptimizeFor] = {
    "CODE_SIZE",
    "LITE_RUNTIME",
    "SPEED",
}


def check_file_options_optimize_for(value: str) -> FileOptionsOptimizeFor:
    if value in FILE_OPTIONS_OPTIMIZE_FOR_VALUES:
        return cast(FileOptionsOptimizeFor, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FILE_OPTIONS_OPTIMIZE_FOR_VALUES!r}")
