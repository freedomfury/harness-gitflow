from typing import Literal, cast

FilesFilterPropertiesDTOFileUsage = Literal["CONFIG", "MANIFEST_FILE", "SCRIPT"]

FILES_FILTER_PROPERTIES_DTO_FILE_USAGE_VALUES: set[FilesFilterPropertiesDTOFileUsage] = {
    "CONFIG",
    "MANIFEST_FILE",
    "SCRIPT",
}


def check_files_filter_properties_dto_file_usage(value: str) -> FilesFilterPropertiesDTOFileUsage:
    if value in FILES_FILTER_PROPERTIES_DTO_FILE_USAGE_VALUES:
        return cast(FilesFilterPropertiesDTOFileUsage, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FILES_FILTER_PROPERTIES_DTO_FILE_USAGE_VALUES!r}")
