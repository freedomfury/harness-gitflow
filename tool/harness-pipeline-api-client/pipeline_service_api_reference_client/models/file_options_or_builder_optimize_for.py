from typing import Literal, cast

FileOptionsOrBuilderOptimizeFor = Literal["CODE_SIZE", "LITE_RUNTIME", "SPEED"]

FILE_OPTIONS_OR_BUILDER_OPTIMIZE_FOR_VALUES: set[FileOptionsOrBuilderOptimizeFor] = {
    "CODE_SIZE",
    "LITE_RUNTIME",
    "SPEED",
}


def check_file_options_or_builder_optimize_for(value: str) -> FileOptionsOrBuilderOptimizeFor:
    if value in FILE_OPTIONS_OR_BUILDER_OPTIMIZE_FOR_VALUES:
        return cast(FileOptionsOrBuilderOptimizeFor, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FILE_OPTIONS_OR_BUILDER_OPTIMIZE_FOR_VALUES!r}")
