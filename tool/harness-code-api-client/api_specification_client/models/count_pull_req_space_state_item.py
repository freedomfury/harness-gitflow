from enum import Enum


class CountPullReqSpaceStateItem(str, Enum):
    CLOSED = "closed"
    MERGED = "merged"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
