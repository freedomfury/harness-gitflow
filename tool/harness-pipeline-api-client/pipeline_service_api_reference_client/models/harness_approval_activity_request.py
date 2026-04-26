from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.harness_approval_activity_request_action import (
    HarnessApprovalActivityRequestAction,
    check_harness_approval_activity_request_action,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approver_input import ApproverInput


T = TypeVar("T", bound="HarnessApprovalActivityRequest")


@_attrs_define
class HarnessApprovalActivityRequest:
    """Details of approval activity requested

    Attributes:
        action (HarnessApprovalActivityRequestAction): Approval activity action
        approver_inputs (list[ApproverInput] | Unset): Custom data to capture at the time of approval
        comments (str | Unset): Approval activity with the comment
        auto_approve (bool | Unset):
    """

    action: HarnessApprovalActivityRequestAction
    approver_inputs: list[ApproverInput] | Unset = UNSET
    comments: str | Unset = UNSET
    auto_approve: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: str = self.action

        approver_inputs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.approver_inputs, Unset):
            approver_inputs = []
            for approver_inputs_item_data in self.approver_inputs:
                approver_inputs_item = approver_inputs_item_data.to_dict()
                approver_inputs.append(approver_inputs_item)

        comments = self.comments

        auto_approve = self.auto_approve

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
            }
        )
        if approver_inputs is not UNSET:
            field_dict["approverInputs"] = approver_inputs
        if comments is not UNSET:
            field_dict["comments"] = comments
        if auto_approve is not UNSET:
            field_dict["autoApprove"] = auto_approve

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.approver_input import ApproverInput

        d = dict(src_dict)
        action = check_harness_approval_activity_request_action(d.pop("action"))

        _approver_inputs = d.pop("approverInputs", UNSET)
        approver_inputs: list[ApproverInput] | Unset = UNSET
        if _approver_inputs is not UNSET:
            approver_inputs = []
            for approver_inputs_item_data in _approver_inputs:
                approver_inputs_item = ApproverInput.from_dict(approver_inputs_item_data)

                approver_inputs.append(approver_inputs_item)

        comments = d.pop("comments", UNSET)

        auto_approve = d.pop("autoApprove", UNSET)

        harness_approval_activity_request = cls(
            action=action,
            approver_inputs=approver_inputs,
            comments=comments,
            auto_approve=auto_approve,
        )

        harness_approval_activity_request.additional_properties = d
        return harness_approval_activity_request

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
