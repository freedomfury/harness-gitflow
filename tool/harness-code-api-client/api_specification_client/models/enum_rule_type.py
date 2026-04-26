from enum import Enum


class EnumRuleType(str, Enum):
    BRANCH = "branch"
    PUSH = "push"
    TAG = "tag"

    def __str__(self) -> str:
        return str(self.value)
