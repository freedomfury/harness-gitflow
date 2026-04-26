from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Approvers")


@_attrs_define
class Approvers:
    """This contains details of the Approvers

    Attributes:
        user_groups (list[str] | Unset):
        service_accounts (list[str] | Unset):
        disallowed_user_emails (list[str] | Unset):
        minimum_count (int | Unset):
        disallow_pipeline_executor (bool | Unset):
    """

    user_groups: list[str] | Unset = UNSET
    service_accounts: list[str] | Unset = UNSET
    disallowed_user_emails: list[str] | Unset = UNSET
    minimum_count: int | Unset = UNSET
    disallow_pipeline_executor: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_groups: list[str] | Unset = UNSET
        if not isinstance(self.user_groups, Unset):
            user_groups = self.user_groups

        service_accounts: list[str] | Unset = UNSET
        if not isinstance(self.service_accounts, Unset):
            service_accounts = self.service_accounts

        disallowed_user_emails: list[str] | Unset = UNSET
        if not isinstance(self.disallowed_user_emails, Unset):
            disallowed_user_emails = self.disallowed_user_emails

        minimum_count = self.minimum_count

        disallow_pipeline_executor = self.disallow_pipeline_executor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_groups is not UNSET:
            field_dict["userGroups"] = user_groups
        if service_accounts is not UNSET:
            field_dict["serviceAccounts"] = service_accounts
        if disallowed_user_emails is not UNSET:
            field_dict["disallowedUserEmails"] = disallowed_user_emails
        if minimum_count is not UNSET:
            field_dict["minimumCount"] = minimum_count
        if disallow_pipeline_executor is not UNSET:
            field_dict["disallowPipelineExecutor"] = disallow_pipeline_executor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_groups = cast(list[str], d.pop("userGroups", UNSET))

        service_accounts = cast(list[str], d.pop("serviceAccounts", UNSET))

        disallowed_user_emails = cast(list[str], d.pop("disallowedUserEmails", UNSET))

        minimum_count = d.pop("minimumCount", UNSET)

        disallow_pipeline_executor = d.pop("disallowPipelineExecutor", UNSET)

        approvers = cls(
            user_groups=user_groups,
            service_accounts=service_accounts,
            disallowed_user_emails=disallowed_user_emails,
            minimum_count=minimum_count,
            disallow_pipeline_executor=disallow_pipeline_executor,
        )

        approvers.additional_properties = d
        return approvers

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
