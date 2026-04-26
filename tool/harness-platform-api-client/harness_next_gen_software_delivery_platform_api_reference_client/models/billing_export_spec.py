from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billing_export_spec_billing_type import (
    BillingExportSpecBillingType,
    check_billing_export_spec_billing_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingExportSpec")


@_attrs_define
class BillingExportSpec:
    """Returns Billing details like StorageAccount's Name, container's Name, directory's Name, report Name and subscription
    Id

        Attributes:
            storage_account_name (str):
            container_name (str):
            directory_name (str):
            report_name (str):
            subscription_id (str):
            billing_type (BillingExportSpecBillingType | Unset):
    """

    storage_account_name: str
    container_name: str
    directory_name: str
    report_name: str
    subscription_id: str
    billing_type: BillingExportSpecBillingType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        storage_account_name = self.storage_account_name

        container_name = self.container_name

        directory_name = self.directory_name

        report_name = self.report_name

        subscription_id = self.subscription_id

        billing_type: str | Unset = UNSET
        if not isinstance(self.billing_type, Unset):
            billing_type = self.billing_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "storageAccountName": storage_account_name,
                "containerName": container_name,
                "directoryName": directory_name,
                "reportName": report_name,
                "subscriptionId": subscription_id,
            }
        )
        if billing_type is not UNSET:
            field_dict["billingType"] = billing_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        storage_account_name = d.pop("storageAccountName")

        container_name = d.pop("containerName")

        directory_name = d.pop("directoryName")

        report_name = d.pop("reportName")

        subscription_id = d.pop("subscriptionId")

        _billing_type = d.pop("billingType", UNSET)
        billing_type: BillingExportSpecBillingType | Unset
        if isinstance(_billing_type, Unset):
            billing_type = UNSET
        else:
            billing_type = check_billing_export_spec_billing_type(_billing_type)

        billing_export_spec = cls(
            storage_account_name=storage_account_name,
            container_name=container_name,
            directory_name=directory_name,
            report_name=report_name,
            subscription_id=subscription_id,
            billing_type=billing_type,
        )

        billing_export_spec.additional_properties = d
        return billing_export_spec

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
