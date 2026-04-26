from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SignalFXConnectorDTO")


@_attrs_define
class SignalFXConnectorDTO:
    """
    Attributes:
        connector_type (str):
        url (str):
        api_token_ref (str):
        delegate_selectors (list[str] | Unset):
        ignore_test_connection (bool | Unset):
    """

    connector_type: str
    url: str
    api_token_ref: str
    delegate_selectors: list[str] | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        url = self.url

        api_token_ref = self.api_token_ref

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
                "apiTokenRef": api_token_ref,
            }
        )
        if delegate_selectors is not UNSET:
            field_dict["delegateSelectors"] = delegate_selectors
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        url = d.pop("url")

        api_token_ref = d.pop("apiTokenRef")

        delegate_selectors = cast(list[str], d.pop("delegateSelectors", UNSET))

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        signal_fx_connector_dto = cls(
            connector_type=connector_type,
            url=url,
            api_token_ref=api_token_ref,
            delegate_selectors=delegate_selectors,
            ignore_test_connection=ignore_test_connection,
        )

        signal_fx_connector_dto.additional_properties = d
        return signal_fx_connector_dto

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
