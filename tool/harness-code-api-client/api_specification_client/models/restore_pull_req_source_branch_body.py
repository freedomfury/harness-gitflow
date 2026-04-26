from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestorePullReqSourceBranchBody")


@_attrs_define
class RestorePullReqSourceBranchBody:
    """
    Attributes:
        bypass_rules (bool | Unset):
        dry_run_rules (bool | Unset):
    """

    bypass_rules: bool | Unset = UNSET
    dry_run_rules: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bypass_rules = self.bypass_rules

        dry_run_rules = self.dry_run_rules

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bypass_rules is not UNSET:
            field_dict["bypass_rules"] = bypass_rules
        if dry_run_rules is not UNSET:
            field_dict["dry_run_rules"] = dry_run_rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bypass_rules = d.pop("bypass_rules", UNSET)

        dry_run_rules = d.pop("dry_run_rules", UNSET)

        restore_pull_req_source_branch_body = cls(
            bypass_rules=bypass_rules,
            dry_run_rules=dry_run_rules,
        )

        restore_pull_req_source_branch_body.additional_properties = d
        return restore_pull_req_source_branch_body

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
