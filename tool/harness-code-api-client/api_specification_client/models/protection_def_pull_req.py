from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.protection_def_approvals import ProtectionDefApprovals
    from ..models.protection_def_comments import ProtectionDefComments
    from ..models.protection_def_merge import ProtectionDefMerge
    from ..models.protection_def_reviewers import ProtectionDefReviewers
    from ..models.protection_def_status_checks import ProtectionDefStatusChecks


T = TypeVar("T", bound="ProtectionDefPullReq")


@_attrs_define
class ProtectionDefPullReq:
    """
    Attributes:
        approvals (ProtectionDefApprovals | Unset):
        comments (ProtectionDefComments | Unset):
        merge (ProtectionDefMerge | Unset):
        reviewers (ProtectionDefReviewers | Unset):
        status_checks (ProtectionDefStatusChecks | Unset):
    """

    approvals: ProtectionDefApprovals | Unset = UNSET
    comments: ProtectionDefComments | Unset = UNSET
    merge: ProtectionDefMerge | Unset = UNSET
    reviewers: ProtectionDefReviewers | Unset = UNSET
    status_checks: ProtectionDefStatusChecks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approvals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.approvals, Unset):
            approvals = self.approvals.to_dict()

        comments: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comments, Unset):
            comments = self.comments.to_dict()

        merge: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merge, Unset):
            merge = self.merge.to_dict()

        reviewers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reviewers, Unset):
            reviewers = self.reviewers.to_dict()

        status_checks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status_checks, Unset):
            status_checks = self.status_checks.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if approvals is not UNSET:
            field_dict["approvals"] = approvals
        if comments is not UNSET:
            field_dict["comments"] = comments
        if merge is not UNSET:
            field_dict["merge"] = merge
        if reviewers is not UNSET:
            field_dict["reviewers"] = reviewers
        if status_checks is not UNSET:
            field_dict["status_checks"] = status_checks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.protection_def_approvals import ProtectionDefApprovals
        from ..models.protection_def_comments import ProtectionDefComments
        from ..models.protection_def_merge import ProtectionDefMerge
        from ..models.protection_def_reviewers import ProtectionDefReviewers
        from ..models.protection_def_status_checks import ProtectionDefStatusChecks

        d = dict(src_dict)
        _approvals = d.pop("approvals", UNSET)
        approvals: ProtectionDefApprovals | Unset
        if isinstance(_approvals, Unset):
            approvals = UNSET
        else:
            approvals = ProtectionDefApprovals.from_dict(_approvals)

        _comments = d.pop("comments", UNSET)
        comments: ProtectionDefComments | Unset
        if isinstance(_comments, Unset):
            comments = UNSET
        else:
            comments = ProtectionDefComments.from_dict(_comments)

        _merge = d.pop("merge", UNSET)
        merge: ProtectionDefMerge | Unset
        if isinstance(_merge, Unset):
            merge = UNSET
        else:
            merge = ProtectionDefMerge.from_dict(_merge)

        _reviewers = d.pop("reviewers", UNSET)
        reviewers: ProtectionDefReviewers | Unset
        if isinstance(_reviewers, Unset):
            reviewers = UNSET
        else:
            reviewers = ProtectionDefReviewers.from_dict(_reviewers)

        _status_checks = d.pop("status_checks", UNSET)
        status_checks: ProtectionDefStatusChecks | Unset
        if isinstance(_status_checks, Unset):
            status_checks = UNSET
        else:
            status_checks = ProtectionDefStatusChecks.from_dict(_status_checks)

        protection_def_pull_req = cls(
            approvals=approvals,
            comments=comments,
            merge=merge,
            reviewers=reviewers,
            status_checks=status_checks,
        )

        protection_def_pull_req.additional_properties = d
        return protection_def_pull_req

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
