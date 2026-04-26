from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_health_key_and_value import CustomHealthKeyAndValue


T = TypeVar("T", bound="PrometheusConnectorDTO")


@_attrs_define
class PrometheusConnectorDTO:
    """
    Attributes:
        connector_type (str):
        url (str):
        username (str | Unset):
        password_ref (str | Unset):
        headers (list[CustomHealthKeyAndValue] | Unset):
        delegate_selectors (list[str] | Unset):
        ignore_test_connection (bool | Unset):
    """

    connector_type: str
    url: str
    username: str | Unset = UNSET
    password_ref: str | Unset = UNSET
    headers: list[CustomHealthKeyAndValue] | Unset = UNSET
    delegate_selectors: list[str] | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        url = self.url

        username = self.username

        password_ref = self.password_ref

        headers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = []
            for headers_item_data in self.headers:
                headers_item = headers_item_data.to_dict()
                headers.append(headers_item)

        delegate_selectors: list[str] | Unset = UNSET
        if not isinstance(self.delegate_selectors, Unset):
            delegate_selectors = self.delegate_selectors

        ignore_test_connection = self.ignore_test_connection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
                "url": url,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if password_ref is not UNSET:
            field_dict["passwordRef"] = password_ref
        if headers is not UNSET:
            field_dict["headers"] = headers
        if delegate_selectors is not UNSET:
            field_dict["delegateSelectors"] = delegate_selectors
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_health_key_and_value import CustomHealthKeyAndValue

        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        url = d.pop("url")

        username = d.pop("username", UNSET)

        password_ref = d.pop("passwordRef", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: list[CustomHealthKeyAndValue] | Unset = UNSET
        if _headers is not UNSET:
            headers = []
            for headers_item_data in _headers:
                headers_item = CustomHealthKeyAndValue.from_dict(headers_item_data)

                headers.append(headers_item)

        delegate_selectors = cast(list[str], d.pop("delegateSelectors", UNSET))

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        prometheus_connector_dto = cls(
            connector_type=connector_type,
            url=url,
            username=username,
            password_ref=password_ref,
            headers=headers,
            delegate_selectors=delegate_selectors,
            ignore_test_connection=ignore_test_connection,
        )

        prometheus_connector_dto.additional_properties = d
        return prometheus_connector_dto

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
