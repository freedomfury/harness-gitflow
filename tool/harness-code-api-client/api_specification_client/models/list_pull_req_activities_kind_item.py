from enum import Enum


class ListPullReqActivitiesKindItem(str, Enum):
    CHANGE_COMMENT = "change-comment"
    COMMENT = "comment"
    SYSTEM = "system"

    def __str__(self) -> str:
        return str(self.value)
