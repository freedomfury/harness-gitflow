from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_now_authentication import ServiceNowAuthentication


T = TypeVar("T", bound="ServiceNowConnector")


@_attrs_define
class ServiceNowConnector:
    """ServiceNow Connector details.

    Attributes:
        connector_type (str):
        service_now_url (str):
        auth (ServiceNowAuthentication): This entity contains the details for Service Now Authentication
        username (str | Unset):
        username_ref (str | Unset):
        password_ref (str | Unset):
        delegate_selectors (list[str] | Unset):
        ignore_test_connection (bool | Unset):
    """

    connector_type: str
    service_now_url: str
    auth: ServiceNowAuthentication
    username: str | Unset = UNSET
    username_ref: str | Unset = UNSET
    password_ref: str | Unset = UNSET
    delegate_selectors: list[str] | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        service_now_url = self.service_now_url

        auth = self.auth.to_dict()

        username = self.username

        username_ref = self.username_ref

        password_ref = self.password_ref

        delegate_selectors: list[str] | Unset = UNSET
        if not isinstance(self.delegate_selectors, Unset):
            delegate_selectors = self.delegate_selectors

        ignore_test_connection = self.ignore_test_connection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
                "serviceNowUrl": service_now_url,
                "auth": auth,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if username_ref is not UNSET:
            field_dict["usernameRef"] = username_ref
        if password_ref is not UNSET:
            field_dict["passwordRef"] = password_ref
        if delegate_selectors is not UNSET:
            field_dict["delegateSelectors"] = delegate_selectors
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_now_authentication import ServiceNowAuthentication

        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        service_now_url = d.pop("serviceNowUrl")

        auth = ServiceNowAuthentication.from_dict(d.pop("auth"))

        username = d.pop("username", UNSET)

        username_ref = d.pop("usernameRef", UNSET)

        password_ref = d.pop("passwordRef", UNSET)

        delegate_selectors = cast(list[str], d.pop("delegateSelectors", UNSET))

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        service_now_connector = cls(
            connector_type=connector_type,
            service_now_url=service_now_url,
            auth=auth,
            username=username,
            username_ref=username_ref,
            password_ref=password_ref,
            delegate_selectors=delegate_selectors,
            ignore_test_connection=ignore_test_connection,
        )

        service_now_connector.additional_properties = d
        return service_now_connector

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
