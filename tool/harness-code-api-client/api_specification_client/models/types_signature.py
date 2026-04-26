from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_identity import TypesIdentity


T = TypeVar("T", bound="TypesSignature")


@_attrs_define
class TypesSignature:
    """
    Attributes:
        identity (TypesIdentity | Unset):
        when (datetime.datetime | Unset):
    """

    identity: TypesIdentity | Unset = UNSET
    when: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identity, Unset):
            identity = self.identity.to_dict()

        when: str | Unset = UNSET
        if not isinstance(self.when, Unset):
            when = self.when.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identity is not UNSET:
            field_dict["identity"] = identity
        if when is not UNSET:
            field_dict["when"] = when

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_identity import TypesIdentity

        d = dict(src_dict)
        _identity = d.pop("identity", UNSET)
        identity: TypesIdentity | Unset
        if isinstance(_identity, Unset):
            identity = UNSET
        else:
            identity = TypesIdentity.from_dict(_identity)

        _when = d.pop("when", UNSET)
        when: datetime.datetime | Unset
        if isinstance(_when, Unset):
            when = UNSET
        else:
            when = isoparse(_when)

        types_signature = cls(
            identity=identity,
            when=when,
        )

        types_signature.additional_properties = d
        return types_signature

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
