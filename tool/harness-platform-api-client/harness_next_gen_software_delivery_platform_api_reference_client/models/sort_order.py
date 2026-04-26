from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sort_order_order_type import SortOrderOrderType, check_sort_order_order_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="SortOrder")


@_attrs_define
class SortOrder:
    """
    Attributes:
        field_name (str | Unset):
        order_type (SortOrderOrderType | Unset):
    """

    field_name: str | Unset = UNSET
    order_type: SortOrderOrderType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_name = self.field_name

        order_type: str | Unset = UNSET
        if not isinstance(self.order_type, Unset):
            order_type = self.order_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_name is not UNSET:
            field_dict["fieldName"] = field_name
        if order_type is not UNSET:
            field_dict["orderType"] = order_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_name = d.pop("fieldName", UNSET)

        _order_type = d.pop("orderType", UNSET)
        order_type: SortOrderOrderType | Unset
        if isinstance(_order_type, Unset):
            order_type = UNSET
        else:
            order_type = check_sort_order_order_type(_order_type)

        sort_order = cls(
            field_name=field_name,
            order_type=order_type,
        )

        sort_order.additional_properties = d
        return sort_order

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
