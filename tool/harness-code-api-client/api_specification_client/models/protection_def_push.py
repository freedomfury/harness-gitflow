from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectionDefPush")


@_attrs_define
class ProtectionDefPush:
    """
    Attributes:
        file_size_limit (int | Unset):
        principal_committer_match (bool | Unset):
        secret_scanning_enabled (bool | Unset):
    """

    file_size_limit: int | Unset = UNSET
    principal_committer_match: bool | Unset = UNSET
    secret_scanning_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_size_limit = self.file_size_limit

        principal_committer_match = self.principal_committer_match

        secret_scanning_enabled = self.secret_scanning_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_size_limit is not UNSET:
            field_dict["file_size_limit"] = file_size_limit
        if principal_committer_match is not UNSET:
            field_dict["principal_committer_match"] = principal_committer_match
        if secret_scanning_enabled is not UNSET:
            field_dict["secret_scanning_enabled"] = secret_scanning_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_size_limit = d.pop("file_size_limit", UNSET)

        principal_committer_match = d.pop("principal_committer_match", UNSET)

        secret_scanning_enabled = d.pop("secret_scanning_enabled", UNSET)

        protection_def_push = cls(
            file_size_limit=file_size_limit,
            principal_committer_match=principal_committer_match,
            secret_scanning_enabled=secret_scanning_enabled,
        )

        protection_def_push.additional_properties = d
        return protection_def_push

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
