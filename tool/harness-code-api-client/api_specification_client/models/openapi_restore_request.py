from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenapiRestoreRequest")


@_attrs_define
class OpenapiRestoreRequest:
    """
    Attributes:
        new_identifier (None | str | Unset):
        new_parent_ref (None | str | Unset):
    """

    new_identifier: None | str | Unset = UNSET
    new_parent_ref: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_identifier: None | str | Unset
        if isinstance(self.new_identifier, Unset):
            new_identifier = UNSET
        else:
            new_identifier = self.new_identifier

        new_parent_ref: None | str | Unset
        if isinstance(self.new_parent_ref, Unset):
            new_parent_ref = UNSET
        else:
            new_parent_ref = self.new_parent_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new_identifier is not UNSET:
            field_dict["new_identifier"] = new_identifier
        if new_parent_ref is not UNSET:
            field_dict["new_parent_ref"] = new_parent_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_new_identifier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_identifier = _parse_new_identifier(d.pop("new_identifier", UNSET))

        def _parse_new_parent_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_parent_ref = _parse_new_parent_ref(d.pop("new_parent_ref", UNSET))

        openapi_restore_request = cls(
            new_identifier=new_identifier,
            new_parent_ref=new_parent_ref,
        )

        openapi_restore_request.additional_properties = d
        return openapi_restore_request

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
