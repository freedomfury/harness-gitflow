from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_health_connector_dto_method import (
    CustomHealthConnectorDTOMethod,
    check_custom_health_connector_dto_method,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_health_key_and_value import CustomHealthKeyAndValue


T = TypeVar("T", bound="CustomHealthConnectorDTO")


@_attrs_define
class CustomHealthConnectorDTO:
    """
    Attributes:
        connector_type (str):
        base_url (str):
        method (CustomHealthConnectorDTOMethod):
        headers (list[CustomHealthKeyAndValue] | Unset):
        params (list[CustomHealthKeyAndValue] | Unset):
        validation_body (str | Unset):
        validation_path (str | Unset):
        delegate_selectors (list[str] | Unset):
        ignore_test_connection (bool | Unset):
    """

    connector_type: str
    base_url: str
    method: CustomHealthConnectorDTOMethod
    headers: list[CustomHealthKeyAndValue] | Unset = UNSET
    params: list[CustomHealthKeyAndValue] | Unset = UNSET
    validation_body: str | Unset = UNSET
    validation_path: str | Unset = UNSET
    delegate_selectors: list[str] | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        base_url = self.base_url

        method: str = self.method

        headers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = []
            for headers_item_data in self.headers:
                headers_item = headers_item_data.to_dict()
                headers.append(headers_item)

        params: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = []
            for params_item_data in self.params:
                params_item = params_item_data.to_dict()
                params.append(params_item)

        validation_body = self.validation_body

        validation_path = self.validation_path

        delegate_selectors: list[str] | Unset = UNSET
        if not isinstance(self.delegate_selectors, Unset):
            delegate_selectors = self.delegate_selectors

        ignore_test_connection = self.ignore_test_connection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
                "baseURL": base_url,
                "method": method,
            }
        )
        if headers is not UNSET:
            field_dict["headers"] = headers
        if params is not UNSET:
            field_dict["params"] = params
        if validation_body is not UNSET:
            field_dict["validationBody"] = validation_body
        if validation_path is not UNSET:
            field_dict["validationPath"] = validation_path
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

        base_url = d.pop("baseURL")

        method = check_custom_health_connector_dto_method(d.pop("method"))

        _headers = d.pop("headers", UNSET)
        headers: list[CustomHealthKeyAndValue] | Unset = UNSET
        if _headers is not UNSET:
            headers = []
            for headers_item_data in _headers:
                headers_item = CustomHealthKeyAndValue.from_dict(headers_item_data)

                headers.append(headers_item)

        _params = d.pop("params", UNSET)
        params: list[CustomHealthKeyAndValue] | Unset = UNSET
        if _params is not UNSET:
            params = []
            for params_item_data in _params:
                params_item = CustomHealthKeyAndValue.from_dict(params_item_data)

                params.append(params_item)

        validation_body = d.pop("validationBody", UNSET)

        validation_path = d.pop("validationPath", UNSET)

        delegate_selectors = cast(list[str], d.pop("delegateSelectors", UNSET))

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        custom_health_connector_dto = cls(
            connector_type=connector_type,
            base_url=base_url,
            method=method,
            headers=headers,
            params=params,
            validation_body=validation_body,
            validation_path=validation_path,
            delegate_selectors=delegate_selectors,
            ignore_test_connection=ignore_test_connection,
        )

        custom_health_connector_dto.additional_properties = d
        return custom_health_connector_dto

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
