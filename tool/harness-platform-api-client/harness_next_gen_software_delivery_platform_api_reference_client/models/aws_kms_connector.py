from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aws_kms_connector_credential import AwsKmsConnectorCredential
    from ..models.aws_oidc_token_exchange_details_for_delegate import AwsOidcTokenExchangeDetailsForDelegate


T = TypeVar("T", bound="AwsKmsConnector")


@_attrs_define
class AwsKmsConnector:
    """This has configuration details for the AWS KMS Secret Manager.

    Attributes:
        connector_type (str):
        credential (AwsKmsConnectorCredential): Returns the configuration details for the AWS KMS Secret Manager.
        region (str): Region for AWS KMS.
        kms_arn (str | Unset): ARN for AWS KMS.
        kms_arn_in_plain_text (str | Unset):
        is_default (bool | Unset):
        delegate_selectors (list[str] | Unset): List of Delegate Selectors that belong to the same Delegate and are used
            to connect to the Secret Manager.
        aws_oidc_token_exchange_details_for_delegate (AwsOidcTokenExchangeDetailsForDelegate | Unset):
        ignore_test_connection (bool | Unset):
        execute_on_delegate (bool | Unset): Should the secret manager execute operations on the delegate, or via Harness
            platform
        default (bool | Unset):
    """

    connector_type: str
    credential: AwsKmsConnectorCredential
    region: str
    kms_arn: str | Unset = UNSET
    kms_arn_in_plain_text: str | Unset = UNSET
    is_default: bool | Unset = UNSET
    delegate_selectors: list[str] | Unset = UNSET
    aws_oidc_token_exchange_details_for_delegate: AwsOidcTokenExchangeDetailsForDelegate | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    execute_on_delegate: bool | Unset = UNSET
    default: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        credential = self.credential.to_dict()

        region = self.region

        kms_arn = self.kms_arn

        kms_arn_in_plain_text = self.kms_arn_in_plain_text

        is_default = self.is_default

        delegate_selectors: list[str] | Unset = UNSET
        if not isinstance(self.delegate_selectors, Unset):
            delegate_selectors = self.delegate_selectors

        aws_oidc_token_exchange_details_for_delegate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aws_oidc_token_exchange_details_for_delegate, Unset):
            aws_oidc_token_exchange_details_for_delegate = self.aws_oidc_token_exchange_details_for_delegate.to_dict()

        ignore_test_connection = self.ignore_test_connection

        execute_on_delegate = self.execute_on_delegate

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
        if kms_arn is not UNSET:
            field_dict["kmsArn"] = kms_arn
        if kms_arn_in_plain_text is not UNSET:
            field_dict["kmsArnInPlainText"] = kms_arn_in_plain_text
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if delegate_selectors is not UNSET:
            field_dict["delegateSelectors"] = delegate_selectors
        if aws_oidc_token_exchange_details_for_delegate is not UNSET:
            field_dict["awsOidcTokenExchangeDetailsForDelegate"] = aws_oidc_token_exchange_details_for_delegate
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection
        if execute_on_delegate is not UNSET:
            field_dict["executeOnDelegate"] = execute_on_delegate
        if default is not UNSET:
            field_dict["default"] = default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aws_kms_connector_credential import AwsKmsConnectorCredential
        from ..models.aws_oidc_token_exchange_details_for_delegate import AwsOidcTokenExchangeDetailsForDelegate

        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        credential = AwsKmsConnectorCredential.from_dict(d.pop("credential"))

        region = d.pop("region")

        kms_arn = d.pop("kmsArn", UNSET)

        kms_arn_in_plain_text = d.pop("kmsArnInPlainText", UNSET)

        is_default = d.pop("isDefault", UNSET)

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

        default = d.pop("default", UNSET)

        aws_kms_connector = cls(
            connector_type=connector_type,
            credential=credential,
            region=region,
            kms_arn=kms_arn,
            kms_arn_in_plain_text=kms_arn_in_plain_text,
            is_default=is_default,
            delegate_selectors=delegate_selectors,
            aws_oidc_token_exchange_details_for_delegate=aws_oidc_token_exchange_details_for_delegate,
            ignore_test_connection=ignore_test_connection,
            execute_on_delegate=execute_on_delegate,
            default=default,
        )

        aws_kms_connector.additional_properties = d
        return aws_kms_connector

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
