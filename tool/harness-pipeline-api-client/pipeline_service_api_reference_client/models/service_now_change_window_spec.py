from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServiceNowChangeWindowSpec")


@_attrs_define
class ServiceNowChangeWindowSpec:
    """This contains details of the ServiceNow ChangeWindow

    Attributes:
        start_field (str):
        end_field (str):
    """

    start_field: str
    end_field: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_field = self.start_field

        end_field = self.end_field

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startField": start_field,
                "endField": end_field,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_field = d.pop("startField")

        end_field = d.pop("endField")

        service_now_change_window_spec = cls(
            start_field=start_field,
            end_field=end_field,
        )

        service_now_change_window_spec.additional_properties = d
        return service_now_change_window_spec

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
