from enum import Enum


class ListPullReqActivitiesTypeItem(str, Enum):
    AUTO_MERGE_UNSUPPORTED_MERGE_METHOD = "auto-merge-unsupported-merge-method"
    BRANCH_DELETE = "branch-delete"
    BRANCH_RESTORE = "branch-restore"
    BRANCH_UPDATE = "branch-update"
    CODE_COMMENT = "code-comment"
    COMMENT = "comment"
    LABEL_MODIFY = "label-modify"
    MERGE = "merge"
    NON_UNIQUE_MERGE_BASE = "non-unique-merge-base"
    REVIEWER_ADD = "reviewer-add"
    REVIEWER_DELETE = "reviewer-delete"
    REVIEW_SUBMIT = "review-submit"
    STATE_CHANGE = "state-change"
    TARGET_BRANCH_CHANGE = "target-branch-change"
    TITLE_CHANGE = "title-change"
    USER_GROUP_REVIEWER_ADD = "user-group-reviewer-add"
    USER_GROUP_REVIEWER_DELETE = "user-group-reviewer-delete"

    def __str__(self) -> str:
        return str(self.value)
