from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_dynamics_connector_dto_auth_type import (
    AppDynamicsConnectorDTOAuthType,
    check_app_dynamics_connector_dto_auth_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppDynamicsConnectorDTO")


@_attrs_define
class AppDynamicsConnectorDTO:
    """
    Attributes:
        connector_type (str):
        accountname (str):
        controller_url (str):
        username (str | Unset):
        delegate_selectors (list[str] | Unset):
        ignore_test_connection (bool | Unset):
        password_ref (str | Unset):
        client_secret_ref (str | Unset):
        client_id (str | Unset):
        auth_type (AppDynamicsConnectorDTOAuthType | Unset):
    """

    connector_type: str
    accountname: str
    controller_url: str
    username: str | Unset = UNSET
    delegate_selectors: list[str] | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    password_ref: str | Unset = UNSET
    client_secret_ref: str | Unset = UNSET
    client_id: str | Unset = UNSET
    auth_type: AppDynamicsConnectorDTOAuthType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        accountname = self.accountname

        controller_url = self.controller_url

        username = self.username

        delegate_selectors: list[str] | Unset = UNSET
        if not isinstance(self.delegate_selectors, Unset):
            delegate_selectors = self.delegate_selectors

        ignore_test_connection = self.ignore_test_connection

        password_ref = self.password_ref

        client_secret_ref = self.client_secret_ref

        client_id = self.client_id

        auth_type: str | Unset = UNSET
        if not isinstance(self.auth_type, Unset):
            auth_type = self.auth_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
                "accountname": accountname,
                "controllerUrl": controller_url,
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
        if client_secret_ref is not UNSET:
            field_dict["clientSecretRef"] = client_secret_ref
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if auth_type is not UNSET:
            field_dict["authType"] = auth_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        accountname = d.pop("accountname")

        controller_url = d.pop("controllerUrl")

        username = d.pop("username", UNSET)

        delegate_selectors = cast(list[str], d.pop("delegateSelectors", UNSET))

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        password_ref = d.pop("passwordRef", UNSET)

        client_secret_ref = d.pop("clientSecretRef", UNSET)

        client_id = d.pop("clientId", UNSET)

        _auth_type = d.pop("authType", UNSET)
        auth_type: AppDynamicsConnectorDTOAuthType | Unset
        if isinstance(_auth_type, Unset):
            auth_type = UNSET
        else:
            auth_type = check_app_dynamics_connector_dto_auth_type(_auth_type)

        app_dynamics_connector_dto = cls(
            connector_type=connector_type,
            accountname=accountname,
            controller_url=controller_url,
            username=username,
            delegate_selectors=delegate_selectors,
            ignore_test_connection=ignore_test_connection,
            password_ref=password_ref,
            client_secret_ref=client_secret_ref,
            client_id=client_id,
            auth_type=auth_type,
        )

        app_dynamics_connector_dto.additional_properties = d
        return app_dynamics_connector_dto

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
