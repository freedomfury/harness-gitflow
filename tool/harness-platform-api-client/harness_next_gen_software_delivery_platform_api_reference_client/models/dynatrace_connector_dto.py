from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DynatraceConnectorDTO")


@_attrs_define
class DynatraceConnectorDTO:
    """
    Attributes:
        connector_type (str):
        url (str | Unset):
        platform_url (str | Unset):
        api_token_ref (str | Unset):
        platform_token_ref (str | Unset):
        delegate_selectors (list[str] | Unset):
        ignore_test_connection (bool | Unset):
    """

    connector_type: str
    url: str | Unset = UNSET
    platform_url: str | Unset = UNSET
    api_token_ref: str | Unset = UNSET
    platform_token_ref: str | Unset = UNSET
    delegate_selectors: list[str] | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        url = self.url

        platform_url = self.platform_url

        api_token_ref = self.api_token_ref

        platform_token_ref = self.platform_token_ref

        delegate_selectors: list[str] | Unset = UNSET
        if not isinstance(self.delegate_selectors, Unset):
            delegate_selectors = self.delegate_selectors

        ignore_test_connection = self.ignore_test_connection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if platform_url is not UNSET:
            field_dict["platformUrl"] = platform_url
        if api_token_ref is not UNSET:
            field_dict["apiTokenRef"] = api_token_ref
        if platform_token_ref is not UNSET:
            field_dict["platformTokenRef"] = platform_token_ref
        if delegate_selectors is not UNSET:
            field_dict["delegateSelectors"] = delegate_selectors
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        url = d.pop("url", UNSET)

        platform_url = d.pop("platformUrl", UNSET)

        api_token_ref = d.pop("apiTokenRef", UNSET)

        platform_token_ref = d.pop("platformTokenRef", UNSET)

        delegate_selectors = cast(list[str], d.pop("delegateSelectors", UNSET))

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        dynatrace_connector_dto = cls(
            connector_type=connector_type,
            url=url,
            platform_url=platform_url,
            api_token_ref=api_token_ref,
            platform_token_ref=platform_token_ref,
            delegate_selectors=delegate_selectors,
            ignore_test_connection=ignore_test_connection,
        )

        dynatrace_connector_dto.additional_properties = d
        return dynatrace_connector_dto

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
