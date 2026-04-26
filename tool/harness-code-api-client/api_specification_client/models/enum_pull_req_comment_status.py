from enum import Enum


class EnumPullReqCommentStatus(str, Enum):
    ACTIVE = "active"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
