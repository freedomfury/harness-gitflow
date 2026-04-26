from enum import Enum


class EnumPullReqSubState(str, Enum):
    AUTO_MERGE = "auto_merge"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
