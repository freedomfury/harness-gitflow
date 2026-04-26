from enum import Enum


class ListPullReqSpaceReviewDecisionItem(str, Enum):
    APPROVED = "approved"
    CHANGEREQ = "changereq"
    PENDING = "pending"
    REVIEWED = "reviewed"

    def __str__(self) -> str:
        return str(self.value)
