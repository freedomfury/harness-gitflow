from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ACLAggregateFilter")


@_attrs_define
class ACLAggregateFilter:
    """
    Attributes:
        resource_group_identifiers (list[str] | Unset):
        role_identifiers (list[str] | Unset):
    """

    resource_group_identifiers: list[str] | Unset = UNSET
    role_identifiers: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_group_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.resource_group_identifiers, Unset):
            resource_group_identifiers = self.resource_group_identifiers

        role_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.role_identifiers, Unset):
            role_identifiers = self.role_identifiers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_group_identifiers is not UNSET:
            field_dict["resourceGroupIdentifiers"] = resource_group_identifiers
        if role_identifiers is not UNSET:
            field_dict["roleIdentifiers"] = role_identifiers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_group_identifiers = cast(list[str], d.pop("resourceGroupIdentifiers", UNSET))

        role_identifiers = cast(list[str], d.pop("roleIdentifiers", UNSET))

        acl_aggregate_filter = cls(
            resource_group_identifiers=resource_group_identifiers,
            role_identifiers=role_identifiers,
        )

        acl_aggregate_filter.additional_properties = d
        return acl_aggregate_filter

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
