from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TriggerGitFullSyncResponse")


@_attrs_define
class TriggerGitFullSyncResponse:
    """This has details to trigger Git Full Sync.

    Attributes:
        is_full_sync_triggered (bool | Unset): Determines if Full Sync is triggered.
    """

    is_full_sync_triggered: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_full_sync_triggered = self.is_full_sync_triggered

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_full_sync_triggered is not UNSET:
            field_dict["isFullSyncTriggered"] = is_full_sync_triggered

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_full_sync_triggered = d.pop("isFullSyncTriggered", UNSET)

        trigger_git_full_sync_response = cls(
            is_full_sync_triggered=is_full_sync_triggered,
        )

        trigger_git_full_sync_response.additional_properties = d
        return trigger_git_full_sync_response

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
