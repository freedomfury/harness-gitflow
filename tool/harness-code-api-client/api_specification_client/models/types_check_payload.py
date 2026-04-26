from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_check_payload_kind import EnumCheckPayloadKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesCheckPayload")


@_attrs_define
class TypesCheckPayload:
    """
    Attributes:
        data (Any | Unset):
        kind (EnumCheckPayloadKind | Unset):
        version (str | Unset):
    """

    data: Any | Unset = UNSET
    kind: EnumCheckPayloadKind | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if kind is not UNSET:
            field_dict["kind"] = kind
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data = d.pop("data", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: EnumCheckPayloadKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = EnumCheckPayloadKind(_kind)

        version = d.pop("version", UNSET)

        types_check_payload = cls(
            data=data,
            kind=kind,
            version=version,
        )

        types_check_payload.additional_properties = d
        return types_check_payload

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
