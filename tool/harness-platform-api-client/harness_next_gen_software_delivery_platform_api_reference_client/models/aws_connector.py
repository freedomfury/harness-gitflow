from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aws_credential import AwsCredential
    from ..models.aws_sdk_client_backoff_strategy import AwsSdkClientBackoffStrategy


T = TypeVar("T", bound="AwsConnector")


@_attrs_define
class AwsConnector:
    """This contains details of the AWS connector

    Attributes:
        connector_type (str):
        credential (AwsCredential): This contains details of the AWS connector credential
        aws_sdk_client_back_off_strategy_override (AwsSdkClientBackoffStrategy | Unset): This contains details of the
            AWS SDK Client Backoff Strategy
        delegate_selectors (list[str] | Unset):
        execute_on_delegate (bool | Unset):
        proxy (bool | Unset):
        ignore_test_connection (bool | Unset):
    """

    connector_type: str
    credential: AwsCredential
    aws_sdk_client_back_off_strategy_override: AwsSdkClientBackoffStrategy | Unset = UNSET
    delegate_selectors: list[str] | Unset = UNSET
    execute_on_delegate: bool | Unset = UNSET
    proxy: bool | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        credential = self.credential.to_dict()

        aws_sdk_client_back_off_strategy_override: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aws_sdk_client_back_off_strategy_override, Unset):
            aws_sdk_client_back_off_strategy_override = self.aws_sdk_client_back_off_strategy_override.to_dict()

        delegate_selectors: list[str] | Unset = UNSET
        if not isinstance(self.delegate_selectors, Unset):
            delegate_selectors = self.delegate_selectors

        execute_on_delegate = self.execute_on_delegate

        proxy = self.proxy

        ignore_test_connection = self.ignore_test_connection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
                "credential": credential,
            }
        )
        if aws_sdk_client_back_off_strategy_override is not UNSET:
            field_dict["awsSdkClientBackOffStrategyOverride"] = aws_sdk_client_back_off_strategy_override
        if delegate_selectors is not UNSET:
            field_dict["delegateSelectors"] = delegate_selectors
        if execute_on_delegate is not UNSET:
            field_dict["executeOnDelegate"] = execute_on_delegate
        if proxy is not UNSET:
            field_dict["proxy"] = proxy
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aws_credential import AwsCredential
        from ..models.aws_sdk_client_backoff_strategy import AwsSdkClientBackoffStrategy

        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        credential = AwsCredential.from_dict(d.pop("credential"))

        _aws_sdk_client_back_off_strategy_override = d.pop("awsSdkClientBackOffStrategyOverride", UNSET)
        aws_sdk_client_back_off_strategy_override: AwsSdkClientBackoffStrategy | Unset
        if isinstance(_aws_sdk_client_back_off_strategy_override, Unset):
            aws_sdk_client_back_off_strategy_override = UNSET
        else:
            aws_sdk_client_back_off_strategy_override = AwsSdkClientBackoffStrategy.from_dict(
                _aws_sdk_client_back_off_strategy_override
            )

        delegate_selectors = cast(list[str], d.pop("delegateSelectors", UNSET))

        execute_on_delegate = d.pop("executeOnDelegate", UNSET)

        proxy = d.pop("proxy", UNSET)

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        aws_connector = cls(
            connector_type=connector_type,
            credential=credential,
            aws_sdk_client_back_off_strategy_override=aws_sdk_client_back_off_strategy_override,
            delegate_selectors=delegate_selectors,
            execute_on_delegate=execute_on_delegate,
            proxy=proxy,
            ignore_test_connection=ignore_test_connection,
        )

        aws_connector.additional_properties = d
        return aws_connector

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
