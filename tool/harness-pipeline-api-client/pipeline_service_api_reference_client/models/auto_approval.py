from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auto_approval_action import AutoApprovalAction, check_auto_approval_action
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scheduled_approval import ScheduledApproval


T = TypeVar("T", bound="AutoApproval")


@_attrs_define
class AutoApproval:
    """This contains details of the Auto Approval

    Attributes:
        scheduled_deadline (ScheduledApproval): This contains details of the Scheduled Approval
        action (AutoApprovalAction):
        comments (str | Unset):
    """

    scheduled_deadline: ScheduledApproval
    action: AutoApprovalAction
    comments: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scheduled_deadline = self.scheduled_deadline.to_dict()

        action: str = self.action

        comments = self.comments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scheduledDeadline": scheduled_deadline,
                "action": action,
            }
        )
        if comments is not UNSET:
            field_dict["comments"] = comments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scheduled_approval import ScheduledApproval

        d = dict(src_dict)
        scheduled_deadline = ScheduledApproval.from_dict(d.pop("scheduledDeadline"))

        action = check_auto_approval_action(d.pop("action"))

        comments = d.pop("comments", UNSET)

        auto_approval = cls(
            scheduled_deadline=scheduled_deadline,
            action=action,
            comments=comments,
        )

        auto_approval.additional_properties = d
        return auto_approval

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
