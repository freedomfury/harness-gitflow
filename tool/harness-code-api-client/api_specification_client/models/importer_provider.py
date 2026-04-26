from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.importer_provider_type import ImporterProviderType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImporterProvider")


@_attrs_define
class ImporterProvider:
    """
    Attributes:
        host (str | Unset):
        password (str | Unset):
        type_ (ImporterProviderType | Unset):
        username (str | Unset):
    """

    host: str | Unset = UNSET
    password: str | Unset = UNSET
    type_: ImporterProviderType | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        password = self.password

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host is not UNSET:
            field_dict["host"] = host
        if password is not UNSET:
            field_dict["password"] = password
        if type_ is not UNSET:
            field_dict["type"] = type_
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host = d.pop("host", UNSET)

        password = d.pop("password", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ImporterProviderType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ImporterProviderType(_type_)

        username = d.pop("username", UNSET)

        importer_provider = cls(
            host=host,
            password=password,
            type_=type_,
            username=username,
        )

        importer_provider.additional_properties = d
        return importer_provider

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
