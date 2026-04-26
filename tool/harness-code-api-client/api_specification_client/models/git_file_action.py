from enum import Enum


class GitFileAction(str, Enum):
    CREATE = "CREATE"
    DELETE = "DELETE"
    MOVE = "MOVE"
    PATCH_TEXT = "PATCH_TEXT"
    UPDATE = "UPDATE"

    def __str__(self) -> str:
        return str(self.value)
