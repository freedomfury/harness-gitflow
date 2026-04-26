from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserMetadata")


@_attrs_define
class UserMetadata:
    """This is the view of the UserMetadata entity defined in Harness

    Attributes:
        email (str):
        uuid (str):
        locked (bool):
        disabled (bool):
        externally_managed (bool):
        name (str | Unset):
        two_factor_authentication_enabled (bool | Unset):
    """

    email: str
    uuid: str
    locked: bool
    disabled: bool
    externally_managed: bool
    name: str | Unset = UNSET
    two_factor_authentication_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        uuid = self.uuid

        locked = self.locked

        disabled = self.disabled

        externally_managed = self.externally_managed

        name = self.name

        two_factor_authentication_enabled = self.two_factor_authentication_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "uuid": uuid,
                "locked": locked,
                "disabled": disabled,
                "externallyManaged": externally_managed,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if two_factor_authentication_enabled is not UNSET:
            field_dict["twoFactorAuthenticationEnabled"] = two_factor_authentication_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        uuid = d.pop("uuid")

        locked = d.pop("locked")

        disabled = d.pop("disabled")

        externally_managed = d.pop("externallyManaged")

        name = d.pop("name", UNSET)

        two_factor_authentication_enabled = d.pop("twoFactorAuthenticationEnabled", UNSET)

        user_metadata = cls(
            email=email,
            uuid=uuid,
            locked=locked,
            disabled=disabled,
            externally_managed=externally_managed,
            name=name,
            two_factor_authentication_enabled=two_factor_authentication_enabled,
        )

        user_metadata.additional_properties = d
        return user_metadata

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
