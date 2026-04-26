from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connector_status_stats import ConnectorStatusStats
    from ..models.connector_type_stats import ConnectorTypeStats


T = TypeVar("T", bound="ConnectorStatistics")


@_attrs_define
class ConnectorStatistics:
    """This has the count for all Connector Types and Status defined in Harness

    Attributes:
        type_stats (list[ConnectorTypeStats] | Unset): Count of Connectors grouped by type.
        status_stats (list[ConnectorStatusStats] | Unset): Count of Connectors grouped by status.
    """

    type_stats: list[ConnectorTypeStats] | Unset = UNSET
    status_stats: list[ConnectorStatusStats] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_stats: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.type_stats, Unset):
            type_stats = []
            for type_stats_item_data in self.type_stats:
                type_stats_item = type_stats_item_data.to_dict()
                type_stats.append(type_stats_item)

        status_stats: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.status_stats, Unset):
            status_stats = []
            for status_stats_item_data in self.status_stats:
                status_stats_item = status_stats_item_data.to_dict()
                status_stats.append(status_stats_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_stats is not UNSET:
            field_dict["typeStats"] = type_stats
        if status_stats is not UNSET:
            field_dict["statusStats"] = status_stats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connector_status_stats import ConnectorStatusStats
        from ..models.connector_type_stats import ConnectorTypeStats

        d = dict(src_dict)
        _type_stats = d.pop("typeStats", UNSET)
        type_stats: list[ConnectorTypeStats] | Unset = UNSET
        if _type_stats is not UNSET:
            type_stats = []
            for type_stats_item_data in _type_stats:
                type_stats_item = ConnectorTypeStats.from_dict(type_stats_item_data)

                type_stats.append(type_stats_item)

        _status_stats = d.pop("statusStats", UNSET)
        status_stats: list[ConnectorStatusStats] | Unset = UNSET
        if _status_stats is not UNSET:
            status_stats = []
            for status_stats_item_data in _status_stats:
                status_stats_item = ConnectorStatusStats.from_dict(status_stats_item_data)

                status_stats.append(status_stats_item)

        connector_statistics = cls(
            type_stats=type_stats,
            status_stats=status_stats,
        )

        connector_statistics.additional_properties = d
        return connector_statistics

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
