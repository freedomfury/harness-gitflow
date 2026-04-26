from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RebaseBranchBody")


@_attrs_define
class RebaseBranchBody:
    """
    Attributes:
        base_branch (str | Unset):
        base_commit_sha (str | Unset): Git object hash
        bypass_rules (bool | Unset):
        dry_run (bool | Unset):
        dry_run_rules (bool | Unset):
        head_branch (str | Unset):
        head_commit_sha (str | Unset): Git object hash
    """

    base_branch: str | Unset = UNSET
    base_commit_sha: str | Unset = UNSET
    bypass_rules: bool | Unset = UNSET
    dry_run: bool | Unset = UNSET
    dry_run_rules: bool | Unset = UNSET
    head_branch: str | Unset = UNSET
    head_commit_sha: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_branch = self.base_branch

        base_commit_sha = self.base_commit_sha

        bypass_rules = self.bypass_rules

        dry_run = self.dry_run

        dry_run_rules = self.dry_run_rules

        head_branch = self.head_branch

        head_commit_sha = self.head_commit_sha

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_branch is not UNSET:
            field_dict["base_branch"] = base_branch
        if base_commit_sha is not UNSET:
            field_dict["base_commit_sha"] = base_commit_sha
        if bypass_rules is not UNSET:
            field_dict["bypass_rules"] = bypass_rules
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if dry_run_rules is not UNSET:
            field_dict["dry_run_rules"] = dry_run_rules
        if head_branch is not UNSET:
            field_dict["head_branch"] = head_branch
        if head_commit_sha is not UNSET:
            field_dict["head_commit_sha"] = head_commit_sha

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_branch = d.pop("base_branch", UNSET)

        base_commit_sha = d.pop("base_commit_sha", UNSET)

        bypass_rules = d.pop("bypass_rules", UNSET)

        dry_run = d.pop("dry_run", UNSET)

        dry_run_rules = d.pop("dry_run_rules", UNSET)

        head_branch = d.pop("head_branch", UNSET)

        head_commit_sha = d.pop("head_commit_sha", UNSET)

        rebase_branch_body = cls(
            base_branch=base_branch,
            base_commit_sha=base_commit_sha,
            bypass_rules=bypass_rules,
            dry_run=dry_run,
            dry_run_rules=dry_run_rules,
            head_branch=head_branch,
            head_commit_sha=head_commit_sha,
        )

        rebase_branch_body.additional_properties = d
        return rebase_branch_body

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
