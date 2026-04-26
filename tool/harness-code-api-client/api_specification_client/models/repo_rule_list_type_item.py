from enum import Enum


class RepoRuleListTypeItem(str, Enum):
    BRANCH = "branch"
    PUSH = "push"
    TAG = "tag"

    def __str__(self) -> str:
        return str(self.value)
