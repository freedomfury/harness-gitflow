from enum import Enum


class ListTagsSort(str, Enum):
    DATE = "date"
    NAME = "name"

    def __str__(self) -> str:
        return str(self.value)
