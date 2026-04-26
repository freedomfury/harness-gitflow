from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenapiCreateBranchRequest")


@_attrs_define
class OpenapiCreateBranchRequest:
    """
    Attributes:
        bypass_rules (bool | Unset):
        dry_run_rules (bool | Unset):
        name (str | Unset):
        target (str | Unset):
    """

    bypass_rules: bool | Unset = UNSET
    dry_run_rules: bool | Unset = UNSET
    name: str | Unset = UNSET
    target: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bypass_rules = self.bypass_rules

        dry_run_rules = self.dry_run_rules

        name = self.name

        target = self.target

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bypass_rules is not UNSET:
            field_dict["bypass_rules"] = bypass_rules
        if dry_run_rules is not UNSET:
            field_dict["dry_run_rules"] = dry_run_rules
        if name is not UNSET:
            field_dict["name"] = name
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bypass_rules = d.pop("bypass_rules", UNSET)

        dry_run_rules = d.pop("dry_run_rules", UNSET)

        name = d.pop("name", UNSET)

        target = d.pop("target", UNSET)

        openapi_create_branch_request = cls(
            bypass_rules=bypass_rules,
            dry_run_rules=dry_run_rules,
            name=name,
            target=target,
        )

        openapi_create_branch_request.additional_properties = d
        return openapi_create_branch_request

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
