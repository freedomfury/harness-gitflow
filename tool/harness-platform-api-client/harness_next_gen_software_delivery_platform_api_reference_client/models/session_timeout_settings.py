from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SessionTimeoutSettings")


@_attrs_define
class SessionTimeoutSettings:
    """This contains the information about the session timeout for this account in Harness.

    Attributes:
        session_time_out_in_minutes (int): Any user of this account will be logged out if there is no activity for this
            number of minutes
        absolute_session_time_out_in_minutes (int | Unset): Any user of this account will be logged out after this
            number of minutes
    """

    session_time_out_in_minutes: int
    absolute_session_time_out_in_minutes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session_time_out_in_minutes = self.session_time_out_in_minutes

        absolute_session_time_out_in_minutes = self.absolute_session_time_out_in_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sessionTimeOutInMinutes": session_time_out_in_minutes,
            }
        )
        if absolute_session_time_out_in_minutes is not UNSET:
            field_dict["absoluteSessionTimeOutInMinutes"] = absolute_session_time_out_in_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_time_out_in_minutes = d.pop("sessionTimeOutInMinutes")

        absolute_session_time_out_in_minutes = d.pop("absoluteSessionTimeOutInMinutes", UNSET)

        session_timeout_settings = cls(
            session_time_out_in_minutes=session_time_out_in_minutes,
            absolute_session_time_out_in_minutes=absolute_session_time_out_in_minutes,
        )

        session_timeout_settings.additional_properties = d
        return session_timeout_settings

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
