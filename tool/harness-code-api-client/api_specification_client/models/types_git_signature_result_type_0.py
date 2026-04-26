from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_git_signature_result import EnumGitSignatureResult
from ..models.enum_public_key_scheme import EnumPublicKeyScheme
from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesGitSignatureResultType0")


@_attrs_define
class TypesGitSignatureResultType0:
    """
    Attributes:
        created (int | Unset):
        key_fingerprint (str | Unset):
        key_id (str | Unset):
        key_scheme (EnumPublicKeyScheme | Unset):
        result (EnumGitSignatureResult | Unset):
        updated (int | Unset):
    """

    created: int | Unset = UNSET
    key_fingerprint: str | Unset = UNSET
    key_id: str | Unset = UNSET
    key_scheme: EnumPublicKeyScheme | Unset = UNSET
    result: EnumGitSignatureResult | Unset = UNSET
    updated: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        key_fingerprint = self.key_fingerprint

        key_id = self.key_id

        key_scheme: str | Unset = UNSET
        if not isinstance(self.key_scheme, Unset):
            key_scheme = self.key_scheme.value

        result: str | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.value

        updated = self.updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if key_fingerprint is not UNSET:
            field_dict["key_fingerprint"] = key_fingerprint
        if key_id is not UNSET:
            field_dict["key_id"] = key_id
        if key_scheme is not UNSET:
            field_dict["key_scheme"] = key_scheme
        if result is not UNSET:
            field_dict["result"] = result
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = d.pop("created", UNSET)

        key_fingerprint = d.pop("key_fingerprint", UNSET)

        key_id = d.pop("key_id", UNSET)

        _key_scheme = d.pop("key_scheme", UNSET)
        key_scheme: EnumPublicKeyScheme | Unset
        if isinstance(_key_scheme, Unset):
            key_scheme = UNSET
        else:
            key_scheme = EnumPublicKeyScheme(_key_scheme)

        _result = d.pop("result", UNSET)
        result: EnumGitSignatureResult | Unset
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = EnumGitSignatureResult(_result)

        updated = d.pop("updated", UNSET)

        types_git_signature_result_type_0 = cls(
            created=created,
            key_fingerprint=key_fingerprint,
            key_id=key_id,
            key_scheme=key_scheme,
            result=result,
            updated=updated,
        )

        types_git_signature_result_type_0.additional_properties = d
        return types_git_signature_result_type_0

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
