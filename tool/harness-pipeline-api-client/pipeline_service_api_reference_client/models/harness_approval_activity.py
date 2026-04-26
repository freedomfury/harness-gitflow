from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.harness_approval_activity_action import (
    HarnessApprovalActivityAction,
    check_harness_approval_activity_action,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approver_input import ApproverInput
    from ..models.embedded_user import EmbeddedUser


T = TypeVar("T", bound="HarnessApprovalActivity")


@_attrs_define
class HarnessApprovalActivity:
    """
    Attributes:
        user (EmbeddedUser):
        action (HarnessApprovalActivityAction):
        approver_inputs (list[ApproverInput] | Unset):
        comments (str | Unset):
        approved_at (int | Unset):
    """

    user: EmbeddedUser
    action: HarnessApprovalActivityAction
    approver_inputs: list[ApproverInput] | Unset = UNSET
    comments: str | Unset = UNSET
    approved_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user.to_dict()

        action: str = self.action

        approver_inputs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.approver_inputs, Unset):
            approver_inputs = []
            for approver_inputs_item_data in self.approver_inputs:
                approver_inputs_item = approver_inputs_item_data.to_dict()
                approver_inputs.append(approver_inputs_item)

        comments = self.comments

        approved_at = self.approved_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "action": action,
            }
        )
        if approver_inputs is not UNSET:
            field_dict["approverInputs"] = approver_inputs
        if comments is not UNSET:
            field_dict["comments"] = comments
        if approved_at is not UNSET:
            field_dict["approvedAt"] = approved_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.approver_input import ApproverInput
        from ..models.embedded_user import EmbeddedUser

        d = dict(src_dict)
        user = EmbeddedUser.from_dict(d.pop("user"))

        action = check_harness_approval_activity_action(d.pop("action"))

        _approver_inputs = d.pop("approverInputs", UNSET)
        approver_inputs: list[ApproverInput] | Unset = UNSET
        if _approver_inputs is not UNSET:
            approver_inputs = []
            for approver_inputs_item_data in _approver_inputs:
                approver_inputs_item = ApproverInput.from_dict(approver_inputs_item_data)

                approver_inputs.append(approver_inputs_item)

        comments = d.pop("comments", UNSET)

        approved_at = d.pop("approvedAt", UNSET)

        harness_approval_activity = cls(
            user=user,
            action=action,
            approver_inputs=approver_inputs,
            comments=comments,
            approved_at=approved_at,
        )

        harness_approval_activity.additional_properties = d
        return harness_approval_activity

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
