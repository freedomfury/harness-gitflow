from enum import Enum


class ListPullReqSort(str, Enum):
    CREATED = "created"
    EDITED = "edited"
    MERGED = "merged"
    NUMBER = "number"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
