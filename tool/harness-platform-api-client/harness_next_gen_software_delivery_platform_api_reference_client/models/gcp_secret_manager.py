from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gcp_connector_credential import GcpConnectorCredential
    from ..models.gcp_oidc_token_exchange_details_for_delegate import GcpOidcTokenExchangeDetailsForDelegate


T = TypeVar("T", bound="GcpSecretManager")


@_attrs_define
class GcpSecretManager:
    """This contains details of GCP Secret Manager

    Attributes:
        connector_type (str):
        credentials_ref (str | Unset): Reference to the secret containing credentials of IAM service account for Google
            Secret Manager
        delegate_selectors (list[str] | Unset): List of Delegate Selectors that belong to the same Delegate and are used
            to connect to the Secret Manager.
        execute_on_delegate (bool | Unset): Should the secret manager execute operations on the delegate, or via Harness
            platform
        assume_credentials_on_delegate (bool | Unset): Boolean value to indicate that Credentials are taken from the
            Delegate.
        credential (GcpConnectorCredential | Unset): This contains GCP connector credentials
        gcp_oidc_token_exchange_details_for_delegate (GcpOidcTokenExchangeDetailsForDelegate | Unset):
        ignore_test_connection (bool | Unset):
        default (bool | Unset):
    """

    connector_type: str
    credentials_ref: str | Unset = UNSET
    delegate_selectors: list[str] | Unset = UNSET
    execute_on_delegate: bool | Unset = UNSET
    assume_credentials_on_delegate: bool | Unset = UNSET
    credential: GcpConnectorCredential | Unset = UNSET
    gcp_oidc_token_exchange_details_for_delegate: GcpOidcTokenExchangeDetailsForDelegate | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    default: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        credentials_ref = self.credentials_ref

        delegate_selectors: list[str] | Unset = UNSET
        if not isinstance(self.delegate_selectors, Unset):
            delegate_selectors = self.delegate_selectors

        execute_on_delegate = self.execute_on_delegate

        assume_credentials_on_delegate = self.assume_credentials_on_delegate

        credential: dict[str, Any] | Unset = UNSET
        if not isinstance(self.credential, Unset):
            credential = self.credential.to_dict()

        gcp_oidc_token_exchange_details_for_delegate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gcp_oidc_token_exchange_details_for_delegate, Unset):
            gcp_oidc_token_exchange_details_for_delegate = self.gcp_oidc_token_exchange_details_for_delegate.to_dict()

        ignore_test_connection = self.ignore_test_connection

        default = self.default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
            }
        )
        if credentials_ref is not UNSET:
            field_dict["credentialsRef"] = credentials_ref
        if delegate_selectors is not UNSET:
            field_dict["delegateSelectors"] = delegate_selectors
        if execute_on_delegate is not UNSET:
            field_dict["executeOnDelegate"] = execute_on_delegate
        if assume_credentials_on_delegate is not UNSET:
            field_dict["assumeCredentialsOnDelegate"] = assume_credentials_on_delegate
        if credential is not UNSET:
            field_dict["credential"] = credential
        if gcp_oidc_token_exchange_details_for_delegate is not UNSET:
            field_dict["gcpOidcTokenExchangeDetailsForDelegate"] = gcp_oidc_token_exchange_details_for_delegate
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection
        if default is not UNSET:
            field_dict["default"] = default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gcp_connector_credential import GcpConnectorCredential
        from ..models.gcp_oidc_token_exchange_details_for_delegate import GcpOidcTokenExchangeDetailsForDelegate

        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        credentials_ref = d.pop("credentialsRef", UNSET)

        delegate_selectors = cast(list[str], d.pop("delegateSelectors", UNSET))

        execute_on_delegate = d.pop("executeOnDelegate", UNSET)

        assume_credentials_on_delegate = d.pop("assumeCredentialsOnDelegate", UNSET)

        _credential = d.pop("credential", UNSET)
        credential: GcpConnectorCredential | Unset
        if isinstance(_credential, Unset):
            credential = UNSET
        else:
            credential = GcpConnectorCredential.from_dict(_credential)

        _gcp_oidc_token_exchange_details_for_delegate = d.pop("gcpOidcTokenExchangeDetailsForDelegate", UNSET)
        gcp_oidc_token_exchange_details_for_delegate: GcpOidcTokenExchangeDetailsForDelegate | Unset
        if isinstance(_gcp_oidc_token_exchange_details_for_delegate, Unset):
            gcp_oidc_token_exchange_details_for_delegate = UNSET
        else:
            gcp_oidc_token_exchange_details_for_delegate = GcpOidcTokenExchangeDetailsForDelegate.from_dict(
                _gcp_oidc_token_exchange_details_for_delegate
            )

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        default = d.pop("default", UNSET)

        gcp_secret_manager = cls(
            connector_type=connector_type,
            credentials_ref=credentials_ref,
            delegate_selectors=delegate_selectors,
            execute_on_delegate=execute_on_delegate,
            assume_credentials_on_delegate=assume_credentials_on_delegate,
            credential=credential,
            gcp_oidc_token_exchange_details_for_delegate=gcp_oidc_token_exchange_details_for_delegate,
            ignore_test_connection=ignore_test_connection,
            default=default,
        )

        gcp_secret_manager.additional_properties = d
        return gcp_secret_manager

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
