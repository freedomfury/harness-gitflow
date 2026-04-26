from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.time_range_time_range_filter_type import (
    TimeRangeTimeRangeFilterType,
    check_time_range_time_range_filter_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeRange")


@_attrs_define
class TimeRange:
    """Filter by queued time window

    Attributes:
        start_time (int | Unset):
        end_time (int | Unset):
        relative_time (str | Unset):
        time_range_filter_type (TimeRangeTimeRangeFilterType | Unset): These are the default filters supported for
            specifying time range
    """

    start_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    relative_time: str | Unset = UNSET
    time_range_filter_type: TimeRangeTimeRangeFilterType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_time = self.start_time

        end_time = self.end_time

        relative_time = self.relative_time

        time_range_filter_type: str | Unset = UNSET
        if not isinstance(self.time_range_filter_type, Unset):
            time_range_filter_type = self.time_range_filter_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if relative_time is not UNSET:
            field_dict["relativeTime"] = relative_time
        if time_range_filter_type is not UNSET:
            field_dict["timeRangeFilterType"] = time_range_filter_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        relative_time = d.pop("relativeTime", UNSET)

        _time_range_filter_type = d.pop("timeRangeFilterType", UNSET)
        time_range_filter_type: TimeRangeTimeRangeFilterType | Unset
        if isinstance(_time_range_filter_type, Unset):
            time_range_filter_type = UNSET
        else:
            time_range_filter_type = check_time_range_time_range_filter_type(_time_range_filter_type)

        time_range = cls(
            start_time=start_time,
            end_time=end_time,
            relative_time=relative_time,
            time_range_filter_type=time_range_filter_type,
        )

        time_range.additional_properties = d
        return time_range

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
