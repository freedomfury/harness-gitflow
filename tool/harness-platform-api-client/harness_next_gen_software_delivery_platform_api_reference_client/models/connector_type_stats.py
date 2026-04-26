from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.connector_type_stats_type import ConnectorTypeStatsType, check_connector_type_stats_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectorTypeStats")


@_attrs_define
class ConnectorTypeStats:
    """Count of Connectors grouped by type.

    Attributes:
        type_ (ConnectorTypeStatsType | Unset):
        count (int | Unset):
    """

    type_: ConnectorTypeStatsType | Unset = UNSET
    count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: ConnectorTypeStatsType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_connector_type_stats_type(_type_)

        count = d.pop("count", UNSET)

        connector_type_stats = cls(
            type_=type_,
            count=count,
        )

        connector_type_stats.additional_properties = d
        return connector_type_stats

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
