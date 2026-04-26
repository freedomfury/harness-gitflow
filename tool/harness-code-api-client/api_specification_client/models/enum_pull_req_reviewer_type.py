from enum import Enum


class EnumPullReqReviewerType(str, Enum):
    ASSIGNED = "assigned"
    CODE_OWNERS = "code_owners"
    DEFAULT = "default"
    REQUESTED = "requested"
    SELF_ASSIGNED = "self_assigned"

    def __str__(self) -> str:
        return str(self.value)
