from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_rule_violations import TypesRuleViolations


T = TypeVar("T", bound="PullreqCommentApplySuggestionsOutput")


@_attrs_define
class PullreqCommentApplySuggestionsOutput:
    """
    Attributes:
        commit_id (str | Unset):
        dry_run_rules (bool | Unset):
        rule_violations (list[TypesRuleViolations] | Unset):
    """

    commit_id: str | Unset = UNSET
    dry_run_rules: bool | Unset = UNSET
    rule_violations: list[TypesRuleViolations] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commit_id = self.commit_id

        dry_run_rules = self.dry_run_rules

        rule_violations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rule_violations, Unset):
            rule_violations = []
            for rule_violations_item_data in self.rule_violations:
                rule_violations_item = rule_violations_item_data.to_dict()
                rule_violations.append(rule_violations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commit_id is not UNSET:
            field_dict["commit_id"] = commit_id
        if dry_run_rules is not UNSET:
            field_dict["dry_run_rules"] = dry_run_rules
        if rule_violations is not UNSET:
            field_dict["rule_violations"] = rule_violations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_rule_violations import TypesRuleViolations

        d = dict(src_dict)
        commit_id = d.pop("commit_id", UNSET)

        dry_run_rules = d.pop("dry_run_rules", UNSET)

        _rule_violations = d.pop("rule_violations", UNSET)
        rule_violations: list[TypesRuleViolations] | Unset = UNSET
        if _rule_violations is not UNSET:
            rule_violations = []
            for rule_violations_item_data in _rule_violations:
                rule_violations_item = TypesRuleViolations.from_dict(rule_violations_item_data)

                rule_violations.append(rule_violations_item)

        pullreq_comment_apply_suggestions_output = cls(
            commit_id=commit_id,
            dry_run_rules=dry_run_rules,
            rule_violations=rule_violations,
        )

        pullreq_comment_apply_suggestions_output.additional_properties = d
        return pullreq_comment_apply_suggestions_output

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
