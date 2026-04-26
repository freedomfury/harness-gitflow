from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.splunk_connector_type import SplunkConnectorType, check_splunk_connector_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="SplunkConnector")


@_attrs_define
class SplunkConnector:
    """This contains the Splunk Connector configuration

    Attributes:
        connector_type (str):
        splunk_url (str):
        account_id (str):
        username (str | Unset):
        delegate_selectors (list[str] | Unset):
        ignore_test_connection (bool | Unset):
        password_ref (str | Unset):
        token_ref (str | Unset):
        type_ (SplunkConnectorType | Unset):
    """

    connector_type: str
    splunk_url: str
    account_id: str
    username: str | Unset = UNSET
    delegate_selectors: list[str] | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    password_ref: str | Unset = UNSET
    token_ref: str | Unset = UNSET
    type_: SplunkConnectorType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        splunk_url = self.splunk_url

        account_id = self.account_id

        username = self.username

        delegate_selectors: list[str] | Unset = UNSET
        if not isinstance(self.delegate_selectors, Unset):
            delegate_selectors = self.delegate_selectors

        ignore_test_connection = self.ignore_test_connection

        password_ref = self.password_ref

        token_ref = self.token_ref

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
                "splunkUrl": splunk_url,
                "accountId": account_id,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if delegate_selectors is not UNSET:
            field_dict["delegateSelectors"] = delegate_selectors
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection
        if password_ref is not UNSET:
            field_dict["passwordRef"] = password_ref
        if token_ref is not UNSET:
            field_dict["tokenRef"] = token_ref
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        splunk_url = d.pop("splunkUrl")

        account_id = d.pop("accountId")

        username = d.pop("username", UNSET)

        delegate_selectors = cast(list[str], d.pop("delegateSelectors", UNSET))

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        password_ref = d.pop("passwordRef", UNSET)

        token_ref = d.pop("tokenRef", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: SplunkConnectorType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_splunk_connector_type(_type_)

        splunk_connector = cls(
            connector_type=connector_type,
            splunk_url=splunk_url,
            account_id=account_id,
            username=username,
            delegate_selectors=delegate_selectors,
            ignore_test_connection=ignore_test_connection,
            password_ref=password_ref,
            token_ref=token_ref,
            type_=type_,
        )

        splunk_connector.additional_properties = d
        return splunk_connector

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
