from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.criteria_spec_wrapper import CriteriaSpecWrapper
    from ..models.jira_issue_key_ng import JiraIssueKeyNG


T = TypeVar("T", bound="JiraApprovalInstanceDetails")


@_attrs_define
class JiraApprovalInstanceDetails:
    """This contains details of Jira Approval Instance

    Attributes:
        connector_ref (str):
        issue (JiraIssueKeyNG):
        approval_criteria (CriteriaSpecWrapper): This contains details of Criteria Specifications such as Criteria Type
        rejection_criteria (CriteriaSpecWrapper): This contains details of Criteria Specifications such as Criteria Type
        retry_interval (str | Unset):
        latest_delegate_task_id (str | Unset):
        delegate_task_name (str | Unset):
    """

    connector_ref: str
    issue: JiraIssueKeyNG
    approval_criteria: CriteriaSpecWrapper
    rejection_criteria: CriteriaSpecWrapper
    retry_interval: str | Unset = UNSET
    latest_delegate_task_id: str | Unset = UNSET
    delegate_task_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_ref = self.connector_ref

        issue = self.issue.to_dict()

        approval_criteria = self.approval_criteria.to_dict()

        rejection_criteria = self.rejection_criteria.to_dict()

        retry_interval = self.retry_interval

        latest_delegate_task_id = self.latest_delegate_task_id

        delegate_task_name = self.delegate_task_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorRef": connector_ref,
                "issue": issue,
                "approvalCriteria": approval_criteria,
                "rejectionCriteria": rejection_criteria,
            }
        )
        if retry_interval is not UNSET:
            field_dict["retryInterval"] = retry_interval
        if latest_delegate_task_id is not UNSET:
            field_dict["latestDelegateTaskId"] = latest_delegate_task_id
        if delegate_task_name is not UNSET:
            field_dict["delegateTaskName"] = delegate_task_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.criteria_spec_wrapper import CriteriaSpecWrapper
        from ..models.jira_issue_key_ng import JiraIssueKeyNG

        d = dict(src_dict)
        connector_ref = d.pop("connectorRef")

        issue = JiraIssueKeyNG.from_dict(d.pop("issue"))

        approval_criteria = CriteriaSpecWrapper.from_dict(d.pop("approvalCriteria"))

        rejection_criteria = CriteriaSpecWrapper.from_dict(d.pop("rejectionCriteria"))

        retry_interval = d.pop("retryInterval", UNSET)

        latest_delegate_task_id = d.pop("latestDelegateTaskId", UNSET)

        delegate_task_name = d.pop("delegateTaskName", UNSET)

        jira_approval_instance_details = cls(
            connector_ref=connector_ref,
            issue=issue,
            approval_criteria=approval_criteria,
            rejection_criteria=rejection_criteria,
            retry_interval=retry_interval,
            latest_delegate_task_id=latest_delegate_task_id,
            delegate_task_name=delegate_task_name,
        )

        jira_approval_instance_details.additional_properties = d
        return jira_approval_instance_details

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
