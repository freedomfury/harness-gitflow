from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.connector_status_stats_status import ConnectorStatusStatsStatus, check_connector_status_stats_status
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectorStatusStats")


@_attrs_define
class ConnectorStatusStats:
    """Count of Connectors grouped by status.

    Attributes:
        status (ConnectorStatusStatsStatus | Unset):
        count (int | Unset):
    """

    status: ConnectorStatusStatsStatus | Unset = UNSET
    count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: ConnectorStatusStatsStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_connector_status_stats_status(_status)

        count = d.pop("count", UNSET)

        connector_status_stats = cls(
            status=status,
            count=count,
        )

        connector_status_stats.additional_properties = d
        return connector_status_stats

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
