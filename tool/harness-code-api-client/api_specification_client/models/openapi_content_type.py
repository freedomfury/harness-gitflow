from enum import Enum


class OpenapiContentType(str, Enum):
    DIR = "dir"
    FILE = "file"
    SUBMODULE = "submodule"
    SYMLINK = "symlink"

    def __str__(self) -> str:
        return str(self.value)
