from enum import Enum


class ListPullReqSpaceStateItem(str, Enum):
    CLOSED = "closed"
    MERGED = "merged"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
