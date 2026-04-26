from enum import Enum


class SpaceRuleListSort(str, Enum):
    CREATED_AT = "created_at"
    IDENTIFIER = "identifier"
    UID = "uid"
    UPDATED_AT = "updated_at"

    def __str__(self) -> str:
        return str(self.value)
