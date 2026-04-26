from typing import Literal, cast

FileType = Literal["FILE", "FOLDER"]

FILE_TYPE_VALUES: set[FileType] = {
    "FILE",
    "FOLDER",
}


def check_file_type(value: str) -> FileType:
    if value in FILE_TYPE_VALUES:
        return cast(FileType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FILE_TYPE_VALUES!r}")
