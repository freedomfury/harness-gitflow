from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gcp_oidc_details import GcpOidcDetails


T = TypeVar("T", bound="GcpKmsConnector")


@_attrs_define
class GcpKmsConnector:
    """This contains GCP KMS SecretManager configuration.

    Attributes:
        connector_type (str):
        project_id (str): ID of the project on GCP.
        region (str): Region for GCP KMS
        key_ring (str): Name of the Key Ring where Google Cloud Symmetric Key is created.
        key_name (str): Name of the Google Cloud Symmetric Key.
        credentials (str | Unset): File Secret which is Service Account Key.
        delegate_selectors (list[str] | Unset): List of Delegate Selectors that belong to the same Delegate and are used
            to connect to the Secret Manager.
        oidc_details (GcpOidcDetails | Unset): This contains GCP OIDC details
        ignore_test_connection (bool | Unset):
        execute_on_delegate (bool | Unset): Should the secret manager execute operations on the delegate, or via Harness
            platform
        default (bool | Unset):
    """

    connector_type: str
    project_id: str
    region: str
    key_ring: str
    key_name: str
    credentials: str | Unset = UNSET
    delegate_selectors: list[str] | Unset = UNSET
    oidc_details: GcpOidcDetails | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    execute_on_delegate: bool | Unset = UNSET
    default: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        project_id = self.project_id

        region = self.region

        key_ring = self.key_ring

        key_name = self.key_name

        credentials = self.credentials

        delegate_selectors: list[str] | Unset = UNSET
        if not isinstance(self.delegate_selectors, Unset):
            delegate_selectors = self.delegate_selectors

        oidc_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.oidc_details, Unset):
            oidc_details = self.oidc_details.to_dict()

        ignore_test_connection = self.ignore_test_connection

        execute_on_delegate = self.execute_on_delegate

        default = self.default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
                "projectId": project_id,
                "region": region,
                "keyRing": key_ring,
                "keyName": key_name,
            }
        )
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if delegate_selectors is not UNSET:
            field_dict["delegateSelectors"] = delegate_selectors
        if oidc_details is not UNSET:
            field_dict["oidcDetails"] = oidc_details
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection
        if execute_on_delegate is not UNSET:
            field_dict["executeOnDelegate"] = execute_on_delegate
        if default is not UNSET:
            field_dict["default"] = default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gcp_oidc_details import GcpOidcDetails

        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        project_id = d.pop("projectId")

        region = d.pop("region")

        key_ring = d.pop("keyRing")

        key_name = d.pop("keyName")

        credentials = d.pop("credentials", UNSET)

        delegate_selectors = cast(list[str], d.pop("delegateSelectors", UNSET))

        _oidc_details = d.pop("oidcDetails", UNSET)
        oidc_details: GcpOidcDetails | Unset
        if isinstance(_oidc_details, Unset):
            oidc_details = UNSET
        else:
            oidc_details = GcpOidcDetails.from_dict(_oidc_details)

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        execute_on_delegate = d.pop("executeOnDelegate", UNSET)

        default = d.pop("default", UNSET)

        gcp_kms_connector = cls(
            connector_type=connector_type,
            project_id=project_id,
            region=region,
            key_ring=key_ring,
            key_name=key_name,
            credentials=credentials,
            delegate_selectors=delegate_selectors,
            oidc_details=oidc_details,
            ignore_test_connection=ignore_test_connection,
            execute_on_delegate=execute_on_delegate,
            default=default,
        )

        gcp_kms_connector.additional_properties = d
        return gcp_kms_connector

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
