from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EntityReferredByOverridesSetupUsageDetail")


@_attrs_define
class EntityReferredByOverridesSetupUsageDetail:
    """
    Attributes:
        type_ (str):
        identifier (str | Unset):
        override_type (str | Unset):
    """

    type_: str
    identifier: str | Unset = UNSET
    override_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        identifier = self.identifier

        override_type = self.override_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if override_type is not UNSET:
            field_dict["overrideType"] = override_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        identifier = d.pop("identifier", UNSET)

        override_type = d.pop("overrideType", UNSET)

        entity_referred_by_overrides_setup_usage_detail = cls(
            type_=type_,
            identifier=identifier,
            override_type=override_type,
        )

        entity_referred_by_overrides_setup_usage_detail.additional_properties = d
        return entity_referred_by_overrides_setup_usage_detail

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
