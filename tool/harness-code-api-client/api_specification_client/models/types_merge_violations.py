from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_rule_violations import TypesRuleViolations


T = TypeVar("T", bound="TypesMergeViolations")


@_attrs_define
class TypesMergeViolations:
    """
    Attributes:
        conflict_files (list[str] | Unset):
        message (str | Unset):
        rule_violations (list[TypesRuleViolations] | Unset):
    """

    conflict_files: list[str] | Unset = UNSET
    message: str | Unset = UNSET
    rule_violations: list[TypesRuleViolations] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conflict_files: list[str] | Unset = UNSET
        if not isinstance(self.conflict_files, Unset):
            conflict_files = self.conflict_files

        message = self.message

        rule_violations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rule_violations, Unset):
            rule_violations = []
            for rule_violations_item_data in self.rule_violations:
                rule_violations_item = rule_violations_item_data.to_dict()
                rule_violations.append(rule_violations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conflict_files is not UNSET:
            field_dict["conflict_files"] = conflict_files
        if message is not UNSET:
            field_dict["message"] = message
        if rule_violations is not UNSET:
            field_dict["rule_violations"] = rule_violations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_rule_violations import TypesRuleViolations

        d = dict(src_dict)
        conflict_files = cast(list[str], d.pop("conflict_files", UNSET))

        message = d.pop("message", UNSET)

        _rule_violations = d.pop("rule_violations", UNSET)
        rule_violations: list[TypesRuleViolations] | Unset = UNSET
        if _rule_violations is not UNSET:
            rule_violations = []
            for rule_violations_item_data in _rule_violations:
                rule_violations_item = TypesRuleViolations.from_dict(rule_violations_item_data)

                rule_violations.append(rule_violations_item)

        types_merge_violations = cls(
            conflict_files=conflict_files,
            message=message,
            rule_violations=rule_violations,
        )

        types_merge_violations.additional_properties = d
        return types_merge_violations

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
