from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteProviderResponse")


@_attrs_define
class DeleteProviderResponse:
    """
    Attributes:
        successfully_deleted (bool | Unset):
        identifier (str | Unset):
    """

    successfully_deleted: bool | Unset = UNSET
    identifier: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        successfully_deleted = self.successfully_deleted

        identifier = self.identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if successfully_deleted is not UNSET:
            field_dict["successfullyDeleted"] = successfully_deleted
        if identifier is not UNSET:
            field_dict["identifier"] = identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        successfully_deleted = d.pop("successfullyDeleted", UNSET)

        identifier = d.pop("identifier", UNSET)

        delete_provider_response = cls(
            successfully_deleted=successfully_deleted,
            identifier=identifier,
        )

        delete_provider_response.additional_properties = d
        return delete_provider_response

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
