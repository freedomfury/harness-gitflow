from enum import Enum


class SpaceRuleListTypeItem(str, Enum):
    BRANCH = "branch"
    PUSH = "push"
    TAG = "tag"

    def __str__(self) -> str:
        return str(self.value)
