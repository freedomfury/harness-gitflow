from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ForkCreateBody")


@_attrs_define
class ForkCreateBody:
    """
    Attributes:
        fork_branch (str | Unset):
        identifier (str | Unset):
        parent_ref (str | Unset):
    """

    fork_branch: str | Unset = UNSET
    identifier: str | Unset = UNSET
    parent_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fork_branch = self.fork_branch

        identifier = self.identifier

        parent_ref = self.parent_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fork_branch is not UNSET:
            field_dict["fork_branch"] = fork_branch
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if parent_ref is not UNSET:
            field_dict["parent_ref"] = parent_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fork_branch = d.pop("fork_branch", UNSET)

        identifier = d.pop("identifier", UNSET)

        parent_ref = d.pop("parent_ref", UNSET)

        fork_create_body = cls(
            fork_branch=fork_branch,
            identifier=identifier,
            parent_ref=parent_ref,
        )

        fork_create_body.additional_properties = d
        return fork_create_body

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
