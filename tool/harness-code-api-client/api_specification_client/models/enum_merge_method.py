from enum import Enum


class EnumMergeMethod(str, Enum):
    FAST_FORWARD = "fast-forward"
    MERGE = "merge"
    REBASE = "rebase"
    SQUASH = "squash"

    def __str__(self) -> str:
        return str(self.value)
