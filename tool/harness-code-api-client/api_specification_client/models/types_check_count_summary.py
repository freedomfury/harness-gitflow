from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesCheckCountSummary")


@_attrs_define
class TypesCheckCountSummary:
    """
    Attributes:
        error (int | Unset):
        failure (int | Unset):
        pending (int | Unset):
        running (int | Unset):
        success (int | Unset):
    """

    error: int | Unset = UNSET
    failure: int | Unset = UNSET
    pending: int | Unset = UNSET
    running: int | Unset = UNSET
    success: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        failure = self.failure

        pending = self.pending

        running = self.running

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if failure is not UNSET:
            field_dict["failure"] = failure
        if pending is not UNSET:
            field_dict["pending"] = pending
        if running is not UNSET:
            field_dict["running"] = running
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = d.pop("error", UNSET)

        failure = d.pop("failure", UNSET)

        pending = d.pop("pending", UNSET)

        running = d.pop("running", UNSET)

        success = d.pop("success", UNSET)

        types_check_count_summary = cls(
            error=error,
            failure=failure,
            pending=pending,
            running=running,
            success=success,
        )

        types_check_count_summary.additional_properties = d
        return types_check_count_summary

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
