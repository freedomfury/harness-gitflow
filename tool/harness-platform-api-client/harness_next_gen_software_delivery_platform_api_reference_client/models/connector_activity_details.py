from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectorActivityDetails")


@_attrs_define
class ConnectorActivityDetails:
    """This contains details of any kind of activities corresponding to the Connector.

    Attributes:
        last_activity_time (int | Unset): This specifies the time of the most recent activity on the Connector.
    """

    last_activity_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_activity_time = self.last_activity_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_activity_time is not UNSET:
            field_dict["lastActivityTime"] = last_activity_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        last_activity_time = d.pop("lastActivityTime", UNSET)

        connector_activity_details = cls(
            last_activity_time=last_activity_time,
        )

        connector_activity_details.additional_properties = d
        return connector_activity_details

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
