from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delegate_group_details_group_implicit_selectors_additional_property import (
    DelegateGroupDetailsGroupImplicitSelectorsAdditionalProperty,
    check_delegate_group_details_group_implicit_selectors_additional_property,
)

T = TypeVar("T", bound="DelegateGroupDetailsGroupImplicitSelectors")


@_attrs_define
class DelegateGroupDetailsGroupImplicitSelectors:
    """ """

    additional_properties: dict[str, DelegateGroupDetailsGroupImplicitSelectorsAdditionalProperty] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delegate_group_details_group_implicit_selectors = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = check_delegate_group_details_group_implicit_selectors_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        delegate_group_details_group_implicit_selectors.additional_properties = additional_properties
        return delegate_group_details_group_implicit_selectors

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> DelegateGroupDetailsGroupImplicitSelectorsAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: DelegateGroupDetailsGroupImplicitSelectorsAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
