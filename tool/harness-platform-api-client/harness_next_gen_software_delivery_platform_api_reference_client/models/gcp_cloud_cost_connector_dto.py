from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gcp_cloud_cost_connector_dto_autostopping_features_item import (
    GcpCloudCostConnectorDTOAutostoppingFeaturesItem,
    check_gcp_cloud_cost_connector_dto_autostopping_features_item,
)
from ..models.gcp_cloud_cost_connector_dto_features_enabled_item import (
    GcpCloudCostConnectorDTOFeaturesEnabledItem,
    check_gcp_cloud_cost_connector_dto_features_enabled_item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gcp_billing_export_spec_dto import GcpBillingExportSpecDTO
    from ..models.gcp_ccm_connector_credential import GcpCcmConnectorCredential


T = TypeVar("T", bound="GcpCloudCostConnectorDTO")


@_attrs_define
class GcpCloudCostConnectorDTO:
    """
    Attributes:
        connector_type (str):
        features_enabled (list[GcpCloudCostConnectorDTOFeaturesEnabledItem]):
        project_id (str):
        service_account_email (str):
        billing_export_spec (GcpBillingExportSpecDTO | Unset):
        autostopping_features (list[GcpCloudCostConnectorDTOAutostoppingFeaturesItem] | Unset):
        ignore_test_connection (bool | Unset):
        credential (GcpCcmConnectorCredential | Unset): This contains CCM GCP connector credentials
    """

    connector_type: str
    features_enabled: list[GcpCloudCostConnectorDTOFeaturesEnabledItem]
    project_id: str
    service_account_email: str
    billing_export_spec: GcpBillingExportSpecDTO | Unset = UNSET
    autostopping_features: list[GcpCloudCostConnectorDTOAutostoppingFeaturesItem] | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    credential: GcpCcmConnectorCredential | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        features_enabled = []
        for features_enabled_item_data in self.features_enabled:
            features_enabled_item: str = features_enabled_item_data
            features_enabled.append(features_enabled_item)

        project_id = self.project_id

        service_account_email = self.service_account_email

        billing_export_spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.billing_export_spec, Unset):
            billing_export_spec = self.billing_export_spec.to_dict()

        autostopping_features: list[str] | Unset = UNSET
        if not isinstance(self.autostopping_features, Unset):
            autostopping_features = []
            for autostopping_features_item_data in self.autostopping_features:
                autostopping_features_item: str = autostopping_features_item_data
                autostopping_features.append(autostopping_features_item)

        ignore_test_connection = self.ignore_test_connection

        credential: dict[str, Any] | Unset = UNSET
        if not isinstance(self.credential, Unset):
            credential = self.credential.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
                "featuresEnabled": features_enabled,
                "projectId": project_id,
                "serviceAccountEmail": service_account_email,
            }
        )
        if billing_export_spec is not UNSET:
            field_dict["billingExportSpec"] = billing_export_spec
        if autostopping_features is not UNSET:
            field_dict["autostoppingFeatures"] = autostopping_features
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection
        if credential is not UNSET:
            field_dict["credential"] = credential

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gcp_billing_export_spec_dto import GcpBillingExportSpecDTO
        from ..models.gcp_ccm_connector_credential import GcpCcmConnectorCredential

        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        features_enabled = []
        _features_enabled = d.pop("featuresEnabled")
        for features_enabled_item_data in _features_enabled:
            features_enabled_item = check_gcp_cloud_cost_connector_dto_features_enabled_item(features_enabled_item_data)

            features_enabled.append(features_enabled_item)

        project_id = d.pop("projectId")

        service_account_email = d.pop("serviceAccountEmail")

        _billing_export_spec = d.pop("billingExportSpec", UNSET)
        billing_export_spec: GcpBillingExportSpecDTO | Unset
        if isinstance(_billing_export_spec, Unset):
            billing_export_spec = UNSET
        else:
            billing_export_spec = GcpBillingExportSpecDTO.from_dict(_billing_export_spec)

        _autostopping_features = d.pop("autostoppingFeatures", UNSET)
        autostopping_features: list[GcpCloudCostConnectorDTOAutostoppingFeaturesItem] | Unset = UNSET
        if _autostopping_features is not UNSET:
            autostopping_features = []
            for autostopping_features_item_data in _autostopping_features:
                autostopping_features_item = check_gcp_cloud_cost_connector_dto_autostopping_features_item(
                    autostopping_features_item_data
                )

                autostopping_features.append(autostopping_features_item)

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        _credential = d.pop("credential", UNSET)
        credential: GcpCcmConnectorCredential | Unset
        if isinstance(_credential, Unset):
            credential = UNSET
        else:
            credential = GcpCcmConnectorCredential.from_dict(_credential)

        gcp_cloud_cost_connector_dto = cls(
            connector_type=connector_type,
            features_enabled=features_enabled,
            project_id=project_id,
            service_account_email=service_account_email,
            billing_export_spec=billing_export_spec,
            autostopping_features=autostopping_features,
            ignore_test_connection=ignore_test_connection,
            credential=credential,
        )

        gcp_cloud_cost_connector_dto.additional_properties = d
        return gcp_cloud_cost_connector_dto

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
