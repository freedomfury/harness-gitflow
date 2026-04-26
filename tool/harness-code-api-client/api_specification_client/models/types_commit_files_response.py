from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_file_reference import TypesFileReference
    from ..models.types_rule_violations import TypesRuleViolations


T = TypeVar("T", bound="TypesCommitFilesResponse")


@_attrs_define
class TypesCommitFilesResponse:
    """
    Attributes:
        changed_files (list[TypesFileReference] | None | Unset):
        commit_id (str | Unset): Git object hash
        dry_run_rules (bool | Unset):
        rule_violations (list[TypesRuleViolations] | Unset):
    """

    changed_files: list[TypesFileReference] | None | Unset = UNSET
    commit_id: str | Unset = UNSET
    dry_run_rules: bool | Unset = UNSET
    rule_violations: list[TypesRuleViolations] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changed_files: list[dict[str, Any]] | None | Unset
        if isinstance(self.changed_files, Unset):
            changed_files = UNSET
        elif isinstance(self.changed_files, list):
            changed_files = []
            for changed_files_type_0_item_data in self.changed_files:
                changed_files_type_0_item = changed_files_type_0_item_data.to_dict()
                changed_files.append(changed_files_type_0_item)

        else:
            changed_files = self.changed_files

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
        if changed_files is not UNSET:
            field_dict["changed_files"] = changed_files
        if commit_id is not UNSET:
            field_dict["commit_id"] = commit_id
        if dry_run_rules is not UNSET:
            field_dict["dry_run_rules"] = dry_run_rules
        if rule_violations is not UNSET:
            field_dict["rule_violations"] = rule_violations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_file_reference import TypesFileReference
        from ..models.types_rule_violations import TypesRuleViolations

        d = dict(src_dict)

        def _parse_changed_files(data: object) -> list[TypesFileReference] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                changed_files_type_0 = []
                _changed_files_type_0 = data
                for changed_files_type_0_item_data in _changed_files_type_0:
                    changed_files_type_0_item = TypesFileReference.from_dict(changed_files_type_0_item_data)

                    changed_files_type_0.append(changed_files_type_0_item)

                return changed_files_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TypesFileReference] | None | Unset, data)

        changed_files = _parse_changed_files(d.pop("changed_files", UNSET))

        commit_id = d.pop("commit_id", UNSET)

        dry_run_rules = d.pop("dry_run_rules", UNSET)

        _rule_violations = d.pop("rule_violations", UNSET)
        rule_violations: list[TypesRuleViolations] | Unset = UNSET
        if _rule_violations is not UNSET:
            rule_violations = []
            for rule_violations_item_data in _rule_violations:
                rule_violations_item = TypesRuleViolations.from_dict(rule_violations_item_data)

                rule_violations.append(rule_violations_item)

        types_commit_files_response = cls(
            changed_files=changed_files,
            commit_id=commit_id,
            dry_run_rules=dry_run_rules,
            rule_violations=rule_violations,
        )

        types_commit_files_response.additional_properties = d
        return types_commit_files_response

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
