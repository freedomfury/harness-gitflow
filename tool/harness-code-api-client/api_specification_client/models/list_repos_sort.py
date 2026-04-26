from enum import Enum


class ListReposSort(str, Enum):
    CREATED = "created"
    IDENTIFIER = "identifier"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
