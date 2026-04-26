from typing import Literal, cast

GetFolderNodesFileUsage = Literal["CONFIG", "MANIFEST_FILE", "SCRIPT"]

GET_FOLDER_NODES_FILE_USAGE_VALUES: set[GetFolderNodesFileUsage] = {
    "CONFIG",
    "MANIFEST_FILE",
    "SCRIPT",
}


def check_get_folder_nodes_file_usage(value: str) -> GetFolderNodesFileUsage:
    if value in GET_FOLDER_NODES_FILE_USAGE_VALUES:
        return cast(GetFolderNodesFileUsage, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_FOLDER_NODES_FILE_USAGE_VALUES!r}")
