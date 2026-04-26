from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connector_response import ConnectorResponse


T = TypeVar("T", bound="CcmK8SConnectorResponse")


@_attrs_define
class CcmK8SConnectorResponse:
    """This has the CCM K8s Connector details along with its metadata.

    Attributes:
        k_8_s_connector (ConnectorResponse | Unset): This has the Connector details along with its metadata.
        ccmk_8_s_connector (list[ConnectorResponse] | Unset):
    """

    k_8_s_connector: ConnectorResponse | Unset = UNSET
    ccmk_8_s_connector: list[ConnectorResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        k_8_s_connector: dict[str, Any] | Unset = UNSET
        if not isinstance(self.k_8_s_connector, Unset):
            k_8_s_connector = self.k_8_s_connector.to_dict()

        ccmk_8_s_connector: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ccmk_8_s_connector, Unset):
            ccmk_8_s_connector = []
            for ccmk_8_s_connector_item_data in self.ccmk_8_s_connector:
                ccmk_8_s_connector_item = ccmk_8_s_connector_item_data.to_dict()
                ccmk_8_s_connector.append(ccmk_8_s_connector_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if k_8_s_connector is not UNSET:
            field_dict["k8sConnector"] = k_8_s_connector
        if ccmk_8_s_connector is not UNSET:
            field_dict["ccmk8sConnector"] = ccmk_8_s_connector

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connector_response import ConnectorResponse

        d = dict(src_dict)
        _k_8_s_connector = d.pop("k8sConnector", UNSET)
        k_8_s_connector: ConnectorResponse | Unset
        if isinstance(_k_8_s_connector, Unset):
            k_8_s_connector = UNSET
        else:
            k_8_s_connector = ConnectorResponse.from_dict(_k_8_s_connector)

        _ccmk_8_s_connector = d.pop("ccmk8sConnector", UNSET)
        ccmk_8_s_connector: list[ConnectorResponse] | Unset = UNSET
        if _ccmk_8_s_connector is not UNSET:
            ccmk_8_s_connector = []
            for ccmk_8_s_connector_item_data in _ccmk_8_s_connector:
                ccmk_8_s_connector_item = ConnectorResponse.from_dict(ccmk_8_s_connector_item_data)

                ccmk_8_s_connector.append(ccmk_8_s_connector_item)

        ccm_k8s_connector_response = cls(
            k_8_s_connector=k_8_s_connector,
            ccmk_8_s_connector=ccmk_8_s_connector,
        )

        ccm_k8s_connector_response.additional_properties = d
        return ccm_k8s_connector_response

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
