from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicAccessResponse")


@_attrs_define
class PublicAccessResponse:
    """
    Attributes:
        is_public (bool | Unset):
        error_message (str | Unset):
        public (bool | Unset):
    """

    is_public: bool | Unset = UNSET
    error_message: str | Unset = UNSET
    public: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_public = self.is_public

        error_message = self.error_message

        public = self.public

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_public is not UNSET:
            field_dict["isPublic"] = is_public
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if public is not UNSET:
            field_dict["public"] = public

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_public = d.pop("isPublic", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        public = d.pop("public", UNSET)

        public_access_response = cls(
            is_public=is_public,
            error_message=error_message,
            public=public,
        )

        public_access_response.additional_properties = d
        return public_access_response

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
