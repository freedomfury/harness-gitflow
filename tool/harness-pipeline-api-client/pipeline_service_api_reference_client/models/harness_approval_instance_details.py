from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_service_account import ApprovalServiceAccount
    from ..models.approval_user_group import ApprovalUserGroup
    from ..models.approver_input_info import ApproverInputInfo
    from ..models.approvers import Approvers
    from ..models.auto_approval import AutoApproval
    from ..models.harness_approval_activity import HarnessApprovalActivity


T = TypeVar("T", bound="HarnessApprovalInstanceDetails")


@_attrs_define
class HarnessApprovalInstanceDetails:
    """This contains details of Harness Approval Instance

    Attributes:
        approvers (Approvers): This contains details of the Approvers
        approval_message (str | Unset):
        include_pipeline_execution_history (bool | Unset):
        approval_activities (list[HarnessApprovalActivity] | Unset):
        auto_approval_params (AutoApproval | Unset): This contains details of the Auto Approval
        approver_inputs (list[ApproverInputInfo] | Unset):
        validated_approval_user_groups (list[ApprovalUserGroup] | Unset):
        validated_approval_service_accounts (list[ApprovalServiceAccount] | Unset):
        is_auto_reject_enabled (bool | Unset):
        auto_reject_enabled (bool | Unset):
    """

    approvers: Approvers
    approval_message: str | Unset = UNSET
    include_pipeline_execution_history: bool | Unset = UNSET
    approval_activities: list[HarnessApprovalActivity] | Unset = UNSET
    auto_approval_params: AutoApproval | Unset = UNSET
    approver_inputs: list[ApproverInputInfo] | Unset = UNSET
    validated_approval_user_groups: list[ApprovalUserGroup] | Unset = UNSET
    validated_approval_service_accounts: list[ApprovalServiceAccount] | Unset = UNSET
    is_auto_reject_enabled: bool | Unset = UNSET
    auto_reject_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approvers = self.approvers.to_dict()

        approval_message = self.approval_message

        include_pipeline_execution_history = self.include_pipeline_execution_history

        approval_activities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.approval_activities, Unset):
            approval_activities = []
            for approval_activities_item_data in self.approval_activities:
                approval_activities_item = approval_activities_item_data.to_dict()
                approval_activities.append(approval_activities_item)

        auto_approval_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auto_approval_params, Unset):
            auto_approval_params = self.auto_approval_params.to_dict()

        approver_inputs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.approver_inputs, Unset):
            approver_inputs = []
            for approver_inputs_item_data in self.approver_inputs:
                approver_inputs_item = approver_inputs_item_data.to_dict()
                approver_inputs.append(approver_inputs_item)

        validated_approval_user_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.validated_approval_user_groups, Unset):
            validated_approval_user_groups = []
            for validated_approval_user_groups_item_data in self.validated_approval_user_groups:
                validated_approval_user_groups_item = validated_approval_user_groups_item_data.to_dict()
                validated_approval_user_groups.append(validated_approval_user_groups_item)

        validated_approval_service_accounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.validated_approval_service_accounts, Unset):
            validated_approval_service_accounts = []
            for validated_approval_service_accounts_item_data in self.validated_approval_service_accounts:
                validated_approval_service_accounts_item = validated_approval_service_accounts_item_data.to_dict()
                validated_approval_service_accounts.append(validated_approval_service_accounts_item)

        is_auto_reject_enabled = self.is_auto_reject_enabled

        auto_reject_enabled = self.auto_reject_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "approvers": approvers,
            }
        )
        if approval_message is not UNSET:
            field_dict["approvalMessage"] = approval_message
        if include_pipeline_execution_history is not UNSET:
            field_dict["includePipelineExecutionHistory"] = include_pipeline_execution_history
        if approval_activities is not UNSET:
            field_dict["approvalActivities"] = approval_activities
        if auto_approval_params is not UNSET:
            field_dict["autoApprovalParams"] = auto_approval_params
        if approver_inputs is not UNSET:
            field_dict["approverInputs"] = approver_inputs
        if validated_approval_user_groups is not UNSET:
            field_dict["validatedApprovalUserGroups"] = validated_approval_user_groups
        if validated_approval_service_accounts is not UNSET:
            field_dict["validatedApprovalServiceAccounts"] = validated_approval_service_accounts
        if is_auto_reject_enabled is not UNSET:
            field_dict["isAutoRejectEnabled"] = is_auto_reject_enabled
        if auto_reject_enabled is not UNSET:
            field_dict["autoRejectEnabled"] = auto_reject_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.approval_service_account import ApprovalServiceAccount
        from ..models.approval_user_group import ApprovalUserGroup
        from ..models.approver_input_info import ApproverInputInfo
        from ..models.approvers import Approvers
        from ..models.auto_approval import AutoApproval
        from ..models.harness_approval_activity import HarnessApprovalActivity

        d = dict(src_dict)
        approvers = Approvers.from_dict(d.pop("approvers"))

        approval_message = d.pop("approvalMessage", UNSET)

        include_pipeline_execution_history = d.pop("includePipelineExecutionHistory", UNSET)

        _approval_activities = d.pop("approvalActivities", UNSET)
        approval_activities: list[HarnessApprovalActivity] | Unset = UNSET
        if _approval_activities is not UNSET:
            approval_activities = []
            for approval_activities_item_data in _approval_activities:
                approval_activities_item = HarnessApprovalActivity.from_dict(approval_activities_item_data)

                approval_activities.append(approval_activities_item)

        _auto_approval_params = d.pop("autoApprovalParams", UNSET)
        auto_approval_params: AutoApproval | Unset
        if isinstance(_auto_approval_params, Unset):
            auto_approval_params = UNSET
        else:
            auto_approval_params = AutoApproval.from_dict(_auto_approval_params)

        _approver_inputs = d.pop("approverInputs", UNSET)
        approver_inputs: list[ApproverInputInfo] | Unset = UNSET
        if _approver_inputs is not UNSET:
            approver_inputs = []
            for approver_inputs_item_data in _approver_inputs:
                approver_inputs_item = ApproverInputInfo.from_dict(approver_inputs_item_data)

                approver_inputs.append(approver_inputs_item)

        _validated_approval_user_groups = d.pop("validatedApprovalUserGroups", UNSET)
        validated_approval_user_groups: list[ApprovalUserGroup] | Unset = UNSET
        if _validated_approval_user_groups is not UNSET:
            validated_approval_user_groups = []
            for validated_approval_user_groups_item_data in _validated_approval_user_groups:
                validated_approval_user_groups_item = ApprovalUserGroup.from_dict(
                    validated_approval_user_groups_item_data
                )

                validated_approval_user_groups.append(validated_approval_user_groups_item)

        _validated_approval_service_accounts = d.pop("validatedApprovalServiceAccounts", UNSET)
        validated_approval_service_accounts: list[ApprovalServiceAccount] | Unset = UNSET
        if _validated_approval_service_accounts is not UNSET:
            validated_approval_service_accounts = []
            for validated_approval_service_accounts_item_data in _validated_approval_service_accounts:
                validated_approval_service_accounts_item = ApprovalServiceAccount.from_dict(
                    validated_approval_service_accounts_item_data
                )

                validated_approval_service_accounts.append(validated_approval_service_accounts_item)

        is_auto_reject_enabled = d.pop("isAutoRejectEnabled", UNSET)

        auto_reject_enabled = d.pop("autoRejectEnabled", UNSET)

        harness_approval_instance_details = cls(
            approvers=approvers,
            approval_message=approval_message,
            include_pipeline_execution_history=include_pipeline_execution_history,
            approval_activities=approval_activities,
            auto_approval_params=auto_approval_params,
            approver_inputs=approver_inputs,
            validated_approval_user_groups=validated_approval_user_groups,
            validated_approval_service_accounts=validated_approval_service_accounts,
            is_auto_reject_enabled=is_auto_reject_enabled,
            auto_reject_enabled=auto_reject_enabled,
        )

        harness_approval_instance_details.additional_properties = d
        return harness_approval_instance_details

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
