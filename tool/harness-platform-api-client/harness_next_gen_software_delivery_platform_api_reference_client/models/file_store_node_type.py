from typing import Literal, cast

FileStoreNodeType = Literal["FILE", "FOLDER"]

FILE_STORE_NODE_TYPE_VALUES: set[FileStoreNodeType] = {
    "FILE",
    "FOLDER",
}


def check_file_store_node_type(value: str) -> FileStoreNodeType:
    if value in FILE_STORE_NODE_TYPE_VALUES:
        return cast(FileStoreNodeType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FILE_STORE_NODE_TYPE_VALUES!r}")
