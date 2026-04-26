from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesRepositoryCore")


@_attrs_define
class TypesRepositoryCore:
    """
    Attributes:
        default_branch (str | Unset):
        fork_id (int | Unset):
        id (int | Unset):
        identifier (str | Unset):
        parent_id (int | Unset):
        path (str | Unset):
        type_ (str | Unset):
    """

    default_branch: str | Unset = UNSET
    fork_id: int | Unset = UNSET
    id: int | Unset = UNSET
    identifier: str | Unset = UNSET
    parent_id: int | Unset = UNSET
    path: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_branch = self.default_branch

        fork_id = self.fork_id

        id = self.id

        identifier = self.identifier

        parent_id = self.parent_id

        path = self.path

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_branch is not UNSET:
            field_dict["default_branch"] = default_branch
        if fork_id is not UNSET:
            field_dict["fork_id"] = fork_id
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if path is not UNSET:
            field_dict["path"] = path
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default_branch = d.pop("default_branch", UNSET)

        fork_id = d.pop("fork_id", UNSET)

        id = d.pop("id", UNSET)

        identifier = d.pop("identifier", UNSET)

        parent_id = d.pop("parent_id", UNSET)

        path = d.pop("path", UNSET)

        type_ = d.pop("type", UNSET)

        types_repository_core = cls(
            default_branch=default_branch,
            fork_id=fork_id,
            id=id,
            identifier=identifier,
            parent_id=parent_id,
            path=path,
            type_=type_,
        )

        types_repository_core.additional_properties = d
        return types_repository_core

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
