from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.elk_connector_dto_auth_type import ELKConnectorDTOAuthType, check_elk_connector_dto_auth_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="ELKConnectorDTO")


@_attrs_define
class ELKConnectorDTO:
    """
    Attributes:
        connector_type (str):
        url (str):
        delegate_selectors (list[str] | Unset):
        username (str | Unset):
        api_key_id (str | Unset):
        password_ref (str | Unset):
        api_key_ref (str | Unset):
        auth_type (ELKConnectorDTOAuthType | Unset):
        ignore_test_connection (bool | Unset):
    """

    connector_type: str
    url: str
    delegate_selectors: list[str] | Unset = UNSET
    username: str | Unset = UNSET
    api_key_id: str | Unset = UNSET
    password_ref: str | Unset = UNSET
    api_key_ref: str | Unset = UNSET
    auth_type: ELKConnectorDTOAuthType | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        url = self.url

        delegate_selectors: list[str] | Unset = UNSET
        if not isinstance(self.delegate_selectors, Unset):
            delegate_selectors = self.delegate_selectors

        username = self.username

        api_key_id = self.api_key_id

        password_ref = self.password_ref

        api_key_ref = self.api_key_ref

        auth_type: str | Unset = UNSET
        if not isinstance(self.auth_type, Unset):
            auth_type = self.auth_type

        ignore_test_connection = self.ignore_test_connection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
                "url": url,
            }
        )
        if delegate_selectors is not UNSET:
            field_dict["delegateSelectors"] = delegate_selectors
        if username is not UNSET:
            field_dict["username"] = username
        if api_key_id is not UNSET:
            field_dict["apiKeyId"] = api_key_id
        if password_ref is not UNSET:
            field_dict["passwordRef"] = password_ref
        if api_key_ref is not UNSET:
            field_dict["apiKeyRef"] = api_key_ref
        if auth_type is not UNSET:
            field_dict["authType"] = auth_type
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        url = d.pop("url")

        delegate_selectors = cast(list[str], d.pop("delegateSelectors", UNSET))

        username = d.pop("username", UNSET)

        api_key_id = d.pop("apiKeyId", UNSET)

        password_ref = d.pop("passwordRef", UNSET)

        api_key_ref = d.pop("apiKeyRef", UNSET)

        _auth_type = d.pop("authType", UNSET)
        auth_type: ELKConnectorDTOAuthType | Unset
        if isinstance(_auth_type, Unset):
            auth_type = UNSET
        else:
            auth_type = check_elk_connector_dto_auth_type(_auth_type)

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        elk_connector_dto = cls(
            connector_type=connector_type,
            url=url,
            delegate_selectors=delegate_selectors,
            username=username,
            api_key_id=api_key_id,
            password_ref=password_ref,
            api_key_ref=api_key_ref,
            auth_type=auth_type,
            ignore_test_connection=ignore_test_connection,
        )

        elk_connector_dto.additional_properties = d
        return elk_connector_dto

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
