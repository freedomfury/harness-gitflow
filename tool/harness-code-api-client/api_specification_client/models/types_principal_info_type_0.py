from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_principal_type import EnumPrincipalType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesPrincipalInfoType0")


@_attrs_define
class TypesPrincipalInfoType0:
    """
    Attributes:
        created (int | Unset):
        display_name (str | Unset):
        email (str | Unset):
        id (int | Unset):
        type_ (EnumPrincipalType | Unset):
        uid (str | Unset):
        updated (int | Unset):
    """

    created: int | Unset = UNSET
    display_name: str | Unset = UNSET
    email: str | Unset = UNSET
    id: int | Unset = UNSET
    type_: EnumPrincipalType | Unset = UNSET
    uid: str | Unset = UNSET
    updated: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        display_name = self.display_name

        email = self.email

        id = self.id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        uid = self.uid

        updated = self.updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if email is not UNSET:
            field_dict["email"] = email
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if uid is not UNSET:
            field_dict["uid"] = uid
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = d.pop("created", UNSET)

        display_name = d.pop("display_name", UNSET)

        email = d.pop("email", UNSET)

        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: EnumPrincipalType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = EnumPrincipalType(_type_)

        uid = d.pop("uid", UNSET)

        updated = d.pop("updated", UNSET)

        types_principal_info_type_0 = cls(
            created=created,
            display_name=display_name,
            email=email,
            id=id,
            type_=type_,
            uid=uid,
            updated=updated,
        )

        types_principal_info_type_0.additional_properties = d
        return types_principal_info_type_0

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
