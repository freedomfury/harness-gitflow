from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EdgeLayoutList")


@_attrs_define
class EdgeLayoutList:
    """This contains info about the Layout of the Graph

    Attributes:
        current_node_children (list[str] | Unset):
        next_ids (list[str] | Unset):
    """

    current_node_children: list[str] | Unset = UNSET
    next_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_node_children: list[str] | Unset = UNSET
        if not isinstance(self.current_node_children, Unset):
            current_node_children = self.current_node_children

        next_ids: list[str] | Unset = UNSET
        if not isinstance(self.next_ids, Unset):
            next_ids = self.next_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_node_children is not UNSET:
            field_dict["currentNodeChildren"] = current_node_children
        if next_ids is not UNSET:
            field_dict["nextIds"] = next_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_node_children = cast(list[str], d.pop("currentNodeChildren", UNSET))

        next_ids = cast(list[str], d.pop("nextIds", UNSET))

        edge_layout_list = cls(
            current_node_children=current_node_children,
            next_ids=next_ids,
        )

        edge_layout_list.additional_properties = d
        return edge_layout_list

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
