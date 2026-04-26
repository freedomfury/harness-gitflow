from enum import Enum


class EnumWebhookTrigger(str, Enum):
    ARTIFACT_CREATED = "artifact_created"
    ARTIFACT_DELETED = "artifact_deleted"
    BRANCH_CREATED = "branch_created"
    BRANCH_DELETED = "branch_deleted"
    BRANCH_UPDATED = "branch_updated"
    PULLREQ_BRANCH_UPDATED = "pullreq_branch_updated"
    PULLREQ_CLOSED = "pullreq_closed"
    PULLREQ_COMMENT_CREATED = "pullreq_comment_created"
    PULLREQ_COMMENT_STATUS_UPDATED = "pullreq_comment_status_updated"
    PULLREQ_COMMENT_UPDATED = "pullreq_comment_updated"
    PULLREQ_CREATED = "pullreq_created"
    PULLREQ_LABEL_ASSIGNED = "pullreq_label_assigned"
    PULLREQ_MERGED = "pullreq_merged"
    PULLREQ_REOPENED = "pullreq_reopened"
    PULLREQ_REVIEW_SUBMITTED = "pullreq_review_submitted"
    PULLREQ_TARGET_BRANCH_CHANGED = "pullreq_target_branch_changed"
    PULLREQ_UPDATED = "pullreq_updated"
    TAG_CREATED = "tag_created"
    TAG_DELETED = "tag_deleted"
    TAG_UPDATED = "tag_updated"

    def __str__(self) -> str:
        return str(self.value)
