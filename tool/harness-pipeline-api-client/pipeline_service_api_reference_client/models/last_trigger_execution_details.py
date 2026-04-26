from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LastTriggerExecutionDetails")


@_attrs_define
class LastTriggerExecutionDetails:
    """
    Attributes:
        last_execution_time (int | Unset):
        last_execution_successful (bool | Unset):
        last_execution_status (str | Unset):
        plan_execution_id (str | Unset):
        message (str | Unset):
    """

    last_execution_time: int | Unset = UNSET
    last_execution_successful: bool | Unset = UNSET
    last_execution_status: str | Unset = UNSET
    plan_execution_id: str | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_execution_time = self.last_execution_time

        last_execution_successful = self.last_execution_successful

        last_execution_status = self.last_execution_status

        plan_execution_id = self.plan_execution_id

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_execution_time is not UNSET:
            field_dict["lastExecutionTime"] = last_execution_time
        if last_execution_successful is not UNSET:
            field_dict["lastExecutionSuccessful"] = last_execution_successful
        if last_execution_status is not UNSET:
            field_dict["lastExecutionStatus"] = last_execution_status
        if plan_execution_id is not UNSET:
            field_dict["planExecutionId"] = plan_execution_id
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        last_execution_time = d.pop("lastExecutionTime", UNSET)

        last_execution_successful = d.pop("lastExecutionSuccessful", UNSET)

        last_execution_status = d.pop("lastExecutionStatus", UNSET)

        plan_execution_id = d.pop("planExecutionId", UNSET)

        message = d.pop("message", UNSET)

        last_trigger_execution_details = cls(
            last_execution_time=last_execution_time,
            last_execution_successful=last_execution_successful,
            last_execution_status=last_execution_status,
            plan_execution_id=plan_execution_id,
            message=message,
        )

        last_trigger_execution_details.additional_properties = d
        return last_trigger_execution_details

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
