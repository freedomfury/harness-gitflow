from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_merge_method import EnumMergeMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_default_reviewer_approvals_response import TypesDefaultReviewerApprovalsResponse
    from ..models.types_rule_violations import TypesRuleViolations


T = TypeVar("T", bound="TypesMergeResponse")


@_attrs_define
class TypesMergeResponse:
    """
    Attributes:
        allowed_methods (list[EnumMergeMethod] | Unset):
        branch_deleted (bool | Unset):
        conflict_files (list[str] | Unset):
        default_reviewer_aprovals (list[TypesDefaultReviewerApprovalsResponse] | Unset):
        dry_run (bool | Unset):
        dry_run_rules (bool | Unset):
        mergeable (bool | Unset):
        minimum_required_approvals_count (int | Unset):
        minimum_required_approvals_count_latest (int | Unset):
        requires_bypass_message (bool | Unset):
        requires_code_owners_approval (bool | Unset):
        requires_code_owners_approval_latest (bool | Unset):
        requires_comment_resolution (bool | Unset):
        requires_no_change_requests (bool | Unset):
        rule_violations (list[TypesRuleViolations] | Unset):
        sha (str | Unset):
    """

    allowed_methods: list[EnumMergeMethod] | Unset = UNSET
    branch_deleted: bool | Unset = UNSET
    conflict_files: list[str] | Unset = UNSET
    default_reviewer_aprovals: list[TypesDefaultReviewerApprovalsResponse] | Unset = UNSET
    dry_run: bool | Unset = UNSET
    dry_run_rules: bool | Unset = UNSET
    mergeable: bool | Unset = UNSET
    minimum_required_approvals_count: int | Unset = UNSET
    minimum_required_approvals_count_latest: int | Unset = UNSET
    requires_bypass_message: bool | Unset = UNSET
    requires_code_owners_approval: bool | Unset = UNSET
    requires_code_owners_approval_latest: bool | Unset = UNSET
    requires_comment_resolution: bool | Unset = UNSET
    requires_no_change_requests: bool | Unset = UNSET
    rule_violations: list[TypesRuleViolations] | Unset = UNSET
    sha: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_methods: list[str] | Unset = UNSET
        if not isinstance(self.allowed_methods, Unset):
            allowed_methods = []
            for allowed_methods_item_data in self.allowed_methods:
                allowed_methods_item = allowed_methods_item_data.value
                allowed_methods.append(allowed_methods_item)

        branch_deleted = self.branch_deleted

        conflict_files: list[str] | Unset = UNSET
        if not isinstance(self.conflict_files, Unset):
            conflict_files = self.conflict_files

        default_reviewer_aprovals: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.default_reviewer_aprovals, Unset):
            default_reviewer_aprovals = []
            for default_reviewer_aprovals_item_data in self.default_reviewer_aprovals:
                default_reviewer_aprovals_item = default_reviewer_aprovals_item_data.to_dict()
                default_reviewer_aprovals.append(default_reviewer_aprovals_item)

        dry_run = self.dry_run

        dry_run_rules = self.dry_run_rules

        mergeable = self.mergeable

        minimum_required_approvals_count = self.minimum_required_approvals_count

        minimum_required_approvals_count_latest = self.minimum_required_approvals_count_latest

        requires_bypass_message = self.requires_bypass_message

        requires_code_owners_approval = self.requires_code_owners_approval

        requires_code_owners_approval_latest = self.requires_code_owners_approval_latest

        requires_comment_resolution = self.requires_comment_resolution

        requires_no_change_requests = self.requires_no_change_requests

        rule_violations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rule_violations, Unset):
            rule_violations = []
            for rule_violations_item_data in self.rule_violations:
                rule_violations_item = rule_violations_item_data.to_dict()
                rule_violations.append(rule_violations_item)

        sha = self.sha

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowed_methods is not UNSET:
            field_dict["allowed_methods"] = allowed_methods
        if branch_deleted is not UNSET:
            field_dict["branch_deleted"] = branch_deleted
        if conflict_files is not UNSET:
            field_dict["conflict_files"] = conflict_files
        if default_reviewer_aprovals is not UNSET:
            field_dict["default_reviewer_aprovals"] = default_reviewer_aprovals
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if dry_run_rules is not UNSET:
            field_dict["dry_run_rules"] = dry_run_rules
        if mergeable is not UNSET:
            field_dict["mergeable"] = mergeable
        if minimum_required_approvals_count is not UNSET:
            field_dict["minimum_required_approvals_count"] = minimum_required_approvals_count
        if minimum_required_approvals_count_latest is not UNSET:
            field_dict["minimum_required_approvals_count_latest"] = minimum_required_approvals_count_latest
        if requires_bypass_message is not UNSET:
            field_dict["requires_bypass_message"] = requires_bypass_message
        if requires_code_owners_approval is not UNSET:
            field_dict["requires_code_owners_approval"] = requires_code_owners_approval
        if requires_code_owners_approval_latest is not UNSET:
            field_dict["requires_code_owners_approval_latest"] = requires_code_owners_approval_latest
        if requires_comment_resolution is not UNSET:
            field_dict["requires_comment_resolution"] = requires_comment_resolution
        if requires_no_change_requests is not UNSET:
            field_dict["requires_no_change_requests"] = requires_no_change_requests
        if rule_violations is not UNSET:
            field_dict["rule_violations"] = rule_violations
        if sha is not UNSET:
            field_dict["sha"] = sha

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_default_reviewer_approvals_response import TypesDefaultReviewerApprovalsResponse
        from ..models.types_rule_violations import TypesRuleViolations

        d = dict(src_dict)
        _allowed_methods = d.pop("allowed_methods", UNSET)
        allowed_methods: list[EnumMergeMethod] | Unset = UNSET
        if _allowed_methods is not UNSET:
            allowed_methods = []
            for allowed_methods_item_data in _allowed_methods:
                allowed_methods_item = EnumMergeMethod(allowed_methods_item_data)

                allowed_methods.append(allowed_methods_item)

        branch_deleted = d.pop("branch_deleted", UNSET)

        conflict_files = cast(list[str], d.pop("conflict_files", UNSET))

        _default_reviewer_aprovals = d.pop("default_reviewer_aprovals", UNSET)
        default_reviewer_aprovals: list[TypesDefaultReviewerApprovalsResponse] | Unset = UNSET
        if _default_reviewer_aprovals is not UNSET:
            default_reviewer_aprovals = []
            for default_reviewer_aprovals_item_data in _default_reviewer_aprovals:
                default_reviewer_aprovals_item = TypesDefaultReviewerApprovalsResponse.from_dict(
                    default_reviewer_aprovals_item_data
                )

                default_reviewer_aprovals.append(default_reviewer_aprovals_item)

        dry_run = d.pop("dry_run", UNSET)

        dry_run_rules = d.pop("dry_run_rules", UNSET)

        mergeable = d.pop("mergeable", UNSET)

        minimum_required_approvals_count = d.pop("minimum_required_approvals_count", UNSET)

        minimum_required_approvals_count_latest = d.pop("minimum_required_approvals_count_latest", UNSET)

        requires_bypass_message = d.pop("requires_bypass_message", UNSET)

        requires_code_owners_approval = d.pop("requires_code_owners_approval", UNSET)

        requires_code_owners_approval_latest = d.pop("requires_code_owners_approval_latest", UNSET)

        requires_comment_resolution = d.pop("requires_comment_resolution", UNSET)

        requires_no_change_requests = d.pop("requires_no_change_requests", UNSET)

        _rule_violations = d.pop("rule_violations", UNSET)
        rule_violations: list[TypesRuleViolations] | Unset = UNSET
        if _rule_violations is not UNSET:
            rule_violations = []
            for rule_violations_item_data in _rule_violations:
                rule_violations_item = TypesRuleViolations.from_dict(rule_violations_item_data)

                rule_violations.append(rule_violations_item)

        sha = d.pop("sha", UNSET)

        types_merge_response = cls(
            allowed_methods=allowed_methods,
            branch_deleted=branch_deleted,
            conflict_files=conflict_files,
            default_reviewer_aprovals=default_reviewer_aprovals,
            dry_run=dry_run,
            dry_run_rules=dry_run_rules,
            mergeable=mergeable,
            minimum_required_approvals_count=minimum_required_approvals_count,
            minimum_required_approvals_count_latest=minimum_required_approvals_count_latest,
            requires_bypass_message=requires_bypass_message,
            requires_code_owners_approval=requires_code_owners_approval,
            requires_code_owners_approval_latest=requires_code_owners_approval_latest,
            requires_comment_resolution=requires_comment_resolution,
            requires_no_change_requests=requires_no_change_requests,
            rule_violations=rule_violations,
            sha=sha,
        )

        types_merge_response.additional_properties = d
        return types_merge_response

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
