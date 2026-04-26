from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.criteria_spec_wrapper import CriteriaSpecWrapper
    from ..models.service_now_change_window_spec import ServiceNowChangeWindowSpec
    from ..models.service_now_ticket_key_ng import ServiceNowTicketKeyNG


T = TypeVar("T", bound="ServiceNowApprovalInstanceDetails")


@_attrs_define
class ServiceNowApprovalInstanceDetails:
    """This contains details of ServiceNow Approval Instance

    Attributes:
        connector_ref (str):
        ticket (ServiceNowTicketKeyNG):
        approval_criteria (CriteriaSpecWrapper): This contains details of Criteria Specifications such as Criteria Type
        rejection_criteria (CriteriaSpecWrapper | Unset): This contains details of Criteria Specifications such as
            Criteria Type
        change_window_spec (ServiceNowChangeWindowSpec | Unset): This contains details of the ServiceNow ChangeWindow
        retry_interval (str | Unset):
        latest_delegate_task_id (str | Unset):
        delegate_task_name (str | Unset):
    """

    connector_ref: str
    ticket: ServiceNowTicketKeyNG
    approval_criteria: CriteriaSpecWrapper
    rejection_criteria: CriteriaSpecWrapper | Unset = UNSET
    change_window_spec: ServiceNowChangeWindowSpec | Unset = UNSET
    retry_interval: str | Unset = UNSET
    latest_delegate_task_id: str | Unset = UNSET
    delegate_task_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_ref = self.connector_ref

        ticket = self.ticket.to_dict()

        approval_criteria = self.approval_criteria.to_dict()

        rejection_criteria: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rejection_criteria, Unset):
            rejection_criteria = self.rejection_criteria.to_dict()

        change_window_spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.change_window_spec, Unset):
            change_window_spec = self.change_window_spec.to_dict()

        retry_interval = self.retry_interval

        latest_delegate_task_id = self.latest_delegate_task_id

        delegate_task_name = self.delegate_task_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorRef": connector_ref,
                "ticket": ticket,
                "approvalCriteria": approval_criteria,
            }
        )
        if rejection_criteria is not UNSET:
            field_dict["rejectionCriteria"] = rejection_criteria
        if change_window_spec is not UNSET:
            field_dict["changeWindowSpec"] = change_window_spec
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
        from ..models.service_now_change_window_spec import ServiceNowChangeWindowSpec
        from ..models.service_now_ticket_key_ng import ServiceNowTicketKeyNG

        d = dict(src_dict)
        connector_ref = d.pop("connectorRef")

        ticket = ServiceNowTicketKeyNG.from_dict(d.pop("ticket"))

        approval_criteria = CriteriaSpecWrapper.from_dict(d.pop("approvalCriteria"))

        _rejection_criteria = d.pop("rejectionCriteria", UNSET)
        rejection_criteria: CriteriaSpecWrapper | Unset
        if isinstance(_rejection_criteria, Unset):
            rejection_criteria = UNSET
        else:
            rejection_criteria = CriteriaSpecWrapper.from_dict(_rejection_criteria)

        _change_window_spec = d.pop("changeWindowSpec", UNSET)
        change_window_spec: ServiceNowChangeWindowSpec | Unset
        if isinstance(_change_window_spec, Unset):
            change_window_spec = UNSET
        else:
            change_window_spec = ServiceNowChangeWindowSpec.from_dict(_change_window_spec)

        retry_interval = d.pop("retryInterval", UNSET)

        latest_delegate_task_id = d.pop("latestDelegateTaskId", UNSET)

        delegate_task_name = d.pop("delegateTaskName", UNSET)

        service_now_approval_instance_details = cls(
            connector_ref=connector_ref,
            ticket=ticket,
            approval_criteria=approval_criteria,
            rejection_criteria=rejection_criteria,
            change_window_spec=change_window_spec,
            retry_interval=retry_interval,
            latest_delegate_task_id=latest_delegate_task_id,
            delegate_task_name=delegate_task_name,
        )

        service_now_approval_instance_details.additional_properties = d
        return service_now_approval_instance_details

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
