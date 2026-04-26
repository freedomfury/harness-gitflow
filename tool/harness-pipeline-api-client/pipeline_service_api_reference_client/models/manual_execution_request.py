from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.manual_execution_request_action import ManualExecutionRequestAction, check_manual_execution_request_action

T = TypeVar("T", bound="ManualExecutionRequest")


@_attrs_define
class ManualExecutionRequest:
    """Request for marking manual execution as fail or resume

    Attributes:
        action (ManualExecutionRequestAction): The action that user wants to do on manual execution i.e. mark it as fail
            or resume
    """

    action: ManualExecutionRequestAction
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: str = self.action

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = check_manual_execution_request_action(d.pop("action"))

        manual_execution_request = cls(
            action=action,
        )

        manual_execution_request.additional_properties = d
        return manual_execution_request

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
