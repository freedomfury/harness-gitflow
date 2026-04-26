from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmbeddedUser")


@_attrs_define
class EmbeddedUser:
    """
    Attributes:
        uuid (str | Unset):
        name (str | Unset):
        email (str | Unset):
        external_user_id (str | Unset):
    """

    uuid: str | Unset = UNSET
    name: str | Unset = UNSET
    email: str | Unset = UNSET
    external_user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        name = self.name

        email = self.email

        external_user_id = self.external_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if external_user_id is not UNSET:
            field_dict["externalUserId"] = external_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = d.pop("uuid", UNSET)

        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        external_user_id = d.pop("externalUserId", UNSET)

        embedded_user = cls(
            uuid=uuid,
            name=name,
            email=email,
            external_user_id=external_user_id,
        )

        embedded_user.additional_properties = d
        return embedded_user

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
