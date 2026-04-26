from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ce_azure_connector_autostopping_features_item import (
    CEAzureConnectorAutostoppingFeaturesItem,
    check_ce_azure_connector_autostopping_features_item,
)
from ..models.ce_azure_connector_features_enabled_item import (
    CEAzureConnectorFeaturesEnabledItem,
    check_ce_azure_connector_features_enabled_item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billing_export_spec import BillingExportSpec


T = TypeVar("T", bound="CEAzureConnector")


@_attrs_define
class CEAzureConnector:
    """This contains the cost explorer of Azure connector

    Attributes:
        connector_type (str):
        features_enabled (list[CEAzureConnectorFeaturesEnabledItem]):
        tenant_id (str):
        subscription_id (str):
        autostopping_features (list[CEAzureConnectorAutostoppingFeaturesItem] | Unset):
        billing_export_spec (BillingExportSpec | Unset): Returns Billing details like StorageAccount's Name, container's
            Name, directory's Name, report Name and subscription Id
        billing_export_spec_2 (BillingExportSpec | Unset): Returns Billing details like StorageAccount's Name,
            container's Name, directory's Name, report Name and subscription Id
        ignore_test_connection (bool | Unset):
    """

    connector_type: str
    features_enabled: list[CEAzureConnectorFeaturesEnabledItem]
    tenant_id: str
    subscription_id: str
    autostopping_features: list[CEAzureConnectorAutostoppingFeaturesItem] | Unset = UNSET
    billing_export_spec: BillingExportSpec | Unset = UNSET
    billing_export_spec_2: BillingExportSpec | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        features_enabled = []
        for features_enabled_item_data in self.features_enabled:
            features_enabled_item: str = features_enabled_item_data
            features_enabled.append(features_enabled_item)

        tenant_id = self.tenant_id

        subscription_id = self.subscription_id

        autostopping_features: list[str] | Unset = UNSET
        if not isinstance(self.autostopping_features, Unset):
            autostopping_features = []
            for autostopping_features_item_data in self.autostopping_features:
                autostopping_features_item: str = autostopping_features_item_data
                autostopping_features.append(autostopping_features_item)

        billing_export_spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.billing_export_spec, Unset):
            billing_export_spec = self.billing_export_spec.to_dict()

        billing_export_spec_2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.billing_export_spec_2, Unset):
            billing_export_spec_2 = self.billing_export_spec_2.to_dict()

        ignore_test_connection = self.ignore_test_connection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
                "featuresEnabled": features_enabled,
                "tenantId": tenant_id,
                "subscriptionId": subscription_id,
            }
        )
        if autostopping_features is not UNSET:
            field_dict["autostoppingFeatures"] = autostopping_features
        if billing_export_spec is not UNSET:
            field_dict["billingExportSpec"] = billing_export_spec
        if billing_export_spec_2 is not UNSET:
            field_dict["billingExportSpec2"] = billing_export_spec_2
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_export_spec import BillingExportSpec

        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        features_enabled = []
        _features_enabled = d.pop("featuresEnabled")
        for features_enabled_item_data in _features_enabled:
            features_enabled_item = check_ce_azure_connector_features_enabled_item(features_enabled_item_data)

            features_enabled.append(features_enabled_item)

        tenant_id = d.pop("tenantId")

        subscription_id = d.pop("subscriptionId")

        _autostopping_features = d.pop("autostoppingFeatures", UNSET)
        autostopping_features: list[CEAzureConnectorAutostoppingFeaturesItem] | Unset = UNSET
        if _autostopping_features is not UNSET:
            autostopping_features = []
            for autostopping_features_item_data in _autostopping_features:
                autostopping_features_item = check_ce_azure_connector_autostopping_features_item(
                    autostopping_features_item_data
                )

                autostopping_features.append(autostopping_features_item)

        _billing_export_spec = d.pop("billingExportSpec", UNSET)
        billing_export_spec: BillingExportSpec | Unset
        if isinstance(_billing_export_spec, Unset):
            billing_export_spec = UNSET
        else:
            billing_export_spec = BillingExportSpec.from_dict(_billing_export_spec)

        _billing_export_spec_2 = d.pop("billingExportSpec2", UNSET)
        billing_export_spec_2: BillingExportSpec | Unset
        if isinstance(_billing_export_spec_2, Unset):
            billing_export_spec_2 = UNSET
        else:
            billing_export_spec_2 = BillingExportSpec.from_dict(_billing_export_spec_2)

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        ce_azure_connector = cls(
            connector_type=connector_type,
            features_enabled=features_enabled,
            tenant_id=tenant_id,
            subscription_id=subscription_id,
            autostopping_features=autostopping_features,
            billing_export_spec=billing_export_spec,
            billing_export_spec_2=billing_export_spec_2,
            ignore_test_connection=ignore_test_connection,
        )

        ce_azure_connector.additional_properties = d
        return ce_azure_connector

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
