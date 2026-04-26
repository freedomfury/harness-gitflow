from typing import Literal, cast

FolderNodeType = Literal["FILE", "FOLDER"]

FOLDER_NODE_TYPE_VALUES: set[FolderNodeType] = {
    "FILE",
    "FOLDER",
}


def check_folder_node_type(value: str) -> FolderNodeType:
    if value in FOLDER_NODE_TYPE_VALUES:
        return cast(FolderNodeType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FOLDER_NODE_TYPE_VALUES!r}")
