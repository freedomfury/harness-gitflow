from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PerpetualTaskInfoForTriggers")


@_attrs_define
class PerpetualTaskInfoForTriggers:
    """
    Attributes:
        state (str | Unset):
        unassigned_reason (str | Unset):
        task_description (str | Unset):
        created_at (int | Unset):
        delegate_id (str | Unset):
        delegate_host_name (str | Unset):
    """

    state: str | Unset = UNSET
    unassigned_reason: str | Unset = UNSET
    task_description: str | Unset = UNSET
    created_at: int | Unset = UNSET
    delegate_id: str | Unset = UNSET
    delegate_host_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state

        unassigned_reason = self.unassigned_reason

        task_description = self.task_description

        created_at = self.created_at

        delegate_id = self.delegate_id

        delegate_host_name = self.delegate_host_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if unassigned_reason is not UNSET:
            field_dict["unassignedReason"] = unassigned_reason
        if task_description is not UNSET:
            field_dict["taskDescription"] = task_description
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if delegate_id is not UNSET:
            field_dict["delegateId"] = delegate_id
        if delegate_host_name is not UNSET:
            field_dict["delegateHostName"] = delegate_host_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state = d.pop("state", UNSET)

        unassigned_reason = d.pop("unassignedReason", UNSET)

        task_description = d.pop("taskDescription", UNSET)

        created_at = d.pop("createdAt", UNSET)

        delegate_id = d.pop("delegateId", UNSET)

        delegate_host_name = d.pop("delegateHostName", UNSET)

        perpetual_task_info_for_triggers = cls(
            state=state,
            unassigned_reason=unassigned_reason,
            task_description=task_description,
            created_at=created_at,
            delegate_id=delegate_id,
            delegate_host_name=delegate_host_name,
        )

        perpetual_task_info_for_triggers.additional_properties = d
        return perpetual_task_info_for_triggers

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
