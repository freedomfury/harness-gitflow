from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ce_kubernetes_cluster_config_dto_features_enabled_item import (
    CEKubernetesClusterConfigDTOFeaturesEnabledItem,
    check_ce_kubernetes_cluster_config_dto_features_enabled_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CEKubernetesClusterConfigDTO")


@_attrs_define
class CEKubernetesClusterConfigDTO:
    """
    Attributes:
        connector_type (str):
        connector_ref (str):
        features_enabled (list[CEKubernetesClusterConfigDTOFeaturesEnabledItem]):
        ignore_test_connection (bool | Unset):
    """

    connector_type: str
    connector_ref: str
    features_enabled: list[CEKubernetesClusterConfigDTOFeaturesEnabledItem]
    ignore_test_connection: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        connector_ref = self.connector_ref

        features_enabled = []
        for features_enabled_item_data in self.features_enabled:
            features_enabled_item: str = features_enabled_item_data
            features_enabled.append(features_enabled_item)

        ignore_test_connection = self.ignore_test_connection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
                "connectorRef": connector_ref,
                "featuresEnabled": features_enabled,
            }
        )
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        connector_ref = d.pop("connectorRef")

        features_enabled = []
        _features_enabled = d.pop("featuresEnabled")
        for features_enabled_item_data in _features_enabled:
            features_enabled_item = check_ce_kubernetes_cluster_config_dto_features_enabled_item(
                features_enabled_item_data
            )

            features_enabled.append(features_enabled_item)

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        ce_kubernetes_cluster_config_dto = cls(
            connector_type=connector_type,
            connector_ref=connector_ref,
            features_enabled=features_enabled,
            ignore_test_connection=ignore_test_connection,
        )

        ce_kubernetes_cluster_config_dto.additional_properties = d
        return ce_kubernetes_cluster_config_dto

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
