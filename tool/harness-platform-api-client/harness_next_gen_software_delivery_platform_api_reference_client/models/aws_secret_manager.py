from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aws_oidc_token_exchange_details_for_delegate import AwsOidcTokenExchangeDetailsForDelegate
    from ..models.aws_secret_manager_credential import AwsSecretManagerCredential


T = TypeVar("T", bound="AwsSecretManager")


@_attrs_define
class AwsSecretManager:
    """Returns AWS Secret Manager configuration details.

    Attributes:
        connector_type (str):
        credential (AwsSecretManagerCredential): This contains the credential type and configuration of the AWS Secret
            Manager.
        region (str): Region for AWS SM.
        secret_name_prefix (str | Unset): Text that is prepended to the Secret name as a prefix.
        delegate_selectors (list[str] | Unset): List of Delegate Selectors that belong to the same Delegate and are used
            to connect to the Secret Manager.
        aws_oidc_token_exchange_details_for_delegate (AwsOidcTokenExchangeDetailsForDelegate | Unset):
        ignore_test_connection (bool | Unset):
        execute_on_delegate (bool | Unset): Should the secret manager execute operations on the delegate, or via Harness
            platform
        use_put_secret (bool | Unset): Whether to update secret value using putSecretValue action.
        force_delete_without_recovery (bool | Unset): Whether to delete the secret without any recovery window.
        recovery_window_in_days (int | Unset): Number of days a Secret can be recovered after it is deleted.
        default (bool | Unset):
    """

    connector_type: str
    credential: AwsSecretManagerCredential
    region: str
    secret_name_prefix: str | Unset = UNSET
    delegate_selectors: list[str] | Unset = UNSET
    aws_oidc_token_exchange_details_for_delegate: AwsOidcTokenExchangeDetailsForDelegate | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    execute_on_delegate: bool | Unset = UNSET
    use_put_secret: bool | Unset = UNSET
    force_delete_without_recovery: bool | Unset = UNSET
    recovery_window_in_days: int | Unset = UNSET
    default: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        credential = self.credential.to_dict()

        region = self.region

        secret_name_prefix = self.secret_name_prefix

        delegate_selectors: list[str] | Unset = UNSET
        if not isinstance(self.delegate_selectors, Unset):
            delegate_selectors = self.delegate_selectors

        aws_oidc_token_exchange_details_for_delegate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aws_oidc_token_exchange_details_for_delegate, Unset):
            aws_oidc_token_exchange_details_for_delegate = self.aws_oidc_token_exchange_details_for_delegate.to_dict()

        ignore_test_connection = self.ignore_test_connection

        execute_on_delegate = self.execute_on_delegate

        use_put_secret = self.use_put_secret

        force_delete_without_recovery = self.force_delete_without_recovery

        recovery_window_in_days = self.recovery_window_in_days

        default = self.default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
                "credential": credential,
                "region": region,
            }
        )
        if secret_name_prefix is not UNSET:
            field_dict["secretNamePrefix"] = secret_name_prefix
        if delegate_selectors is not UNSET:
            field_dict["delegateSelectors"] = delegate_selectors
        if aws_oidc_token_exchange_details_for_delegate is not UNSET:
            field_dict["awsOidcTokenExchangeDetailsForDelegate"] = aws_oidc_token_exchange_details_for_delegate
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection
        if execute_on_delegate is not UNSET:
            field_dict["executeOnDelegate"] = execute_on_delegate
        if use_put_secret is not UNSET:
            field_dict["usePutSecret"] = use_put_secret
        if force_delete_without_recovery is not UNSET:
            field_dict["forceDeleteWithoutRecovery"] = force_delete_without_recovery
        if recovery_window_in_days is not UNSET:
            field_dict["recoveryWindowInDays"] = recovery_window_in_days
        if default is not UNSET:
            field_dict["default"] = default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aws_oidc_token_exchange_details_for_delegate import AwsOidcTokenExchangeDetailsForDelegate
        from ..models.aws_secret_manager_credential import AwsSecretManagerCredential

        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        credential = AwsSecretManagerCredential.from_dict(d.pop("credential"))

        region = d.pop("region")

        secret_name_prefix = d.pop("secretNamePrefix", UNSET)

        delegate_selectors = cast(list[str], d.pop("delegateSelectors", UNSET))

        _aws_oidc_token_exchange_details_for_delegate = d.pop("awsOidcTokenExchangeDetailsForDelegate", UNSET)
        aws_oidc_token_exchange_details_for_delegate: AwsOidcTokenExchangeDetailsForDelegate | Unset
        if isinstance(_aws_oidc_token_exchange_details_for_delegate, Unset):
            aws_oidc_token_exchange_details_for_delegate = UNSET
        else:
            aws_oidc_token_exchange_details_for_delegate = AwsOidcTokenExchangeDetailsForDelegate.from_dict(
                _aws_oidc_token_exchange_details_for_delegate
            )

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        execute_on_delegate = d.pop("executeOnDelegate", UNSET)

        use_put_secret = d.pop("usePutSecret", UNSET)

        force_delete_without_recovery = d.pop("forceDeleteWithoutRecovery", UNSET)

        recovery_window_in_days = d.pop("recoveryWindowInDays", UNSET)

        default = d.pop("default", UNSET)

        aws_secret_manager = cls(
            connector_type=connector_type,
            credential=credential,
            region=region,
            secret_name_prefix=secret_name_prefix,
            delegate_selectors=delegate_selectors,
            aws_oidc_token_exchange_details_for_delegate=aws_oidc_token_exchange_details_for_delegate,
            ignore_test_connection=ignore_test_connection,
            execute_on_delegate=execute_on_delegate,
            use_put_secret=use_put_secret,
            force_delete_without_recovery=force_delete_without_recovery,
            recovery_window_in_days=recovery_window_in_days,
            default=default,
        )

        aws_secret_manager.additional_properties = d
        return aws_secret_manager

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
