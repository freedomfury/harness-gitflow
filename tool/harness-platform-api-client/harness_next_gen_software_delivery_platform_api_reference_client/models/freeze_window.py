from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.recurrence import Recurrence


T = TypeVar("T", bound="FreezeWindow")


@_attrs_define
class FreezeWindow:
    """
    Attributes:
        time_zone (str):
        start_time (str):
        duration (str | Unset):
        end_time (str | Unset):
        recurrence (Recurrence | Unset):
    """

    time_zone: str
    start_time: str
    duration: str | Unset = UNSET
    end_time: str | Unset = UNSET
    recurrence: Recurrence | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_zone = self.time_zone

        start_time = self.start_time

        duration = self.duration

        end_time = self.end_time

        recurrence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recurrence, Unset):
            recurrence = self.recurrence.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timeZone": time_zone,
                "startTime": start_time,
            }
        )
        if duration is not UNSET:
            field_dict["duration"] = duration
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if recurrence is not UNSET:
            field_dict["recurrence"] = recurrence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recurrence import Recurrence

        d = dict(src_dict)
        time_zone = d.pop("timeZone")

        start_time = d.pop("startTime")

        duration = d.pop("duration", UNSET)

        end_time = d.pop("endTime", UNSET)

        _recurrence = d.pop("recurrence", UNSET)
        recurrence: Recurrence | Unset
        if isinstance(_recurrence, Unset):
            recurrence = UNSET
        else:
            recurrence = Recurrence.from_dict(_recurrence)

        freeze_window = cls(
            time_zone=time_zone,
            start_time=start_time,
            duration=duration,
            end_time=end_time,
            recurrence=recurrence,
        )

        freeze_window.additional_properties = d
        return freeze_window

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
