from enum import Enum


class EnumPullReqActivityKind(str, Enum):
    CHANGE_COMMENT = "change-comment"
    COMMENT = "comment"
    SYSTEM = "system"

    def __str__(self) -> str:
        return str(self.value)
