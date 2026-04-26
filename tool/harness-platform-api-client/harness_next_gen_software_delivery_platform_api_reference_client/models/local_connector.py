from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocalConnector")


@_attrs_define
class LocalConnector:
    """This contains the local connector information.

    Attributes:
        connector_type (str):
        ignore_test_connection (bool | Unset):
        default (bool | Unset):
    """

    connector_type: str
    ignore_test_connection: bool | Unset = UNSET
    default: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        ignore_test_connection = self.ignore_test_connection

        default = self.default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
            }
        )
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection
        if default is not UNSET:
            field_dict["default"] = default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        default = d.pop("default", UNSET)

        local_connector = cls(
            connector_type=connector_type,
            ignore_test_connection=ignore_test_connection,
            default=default,
        )

        local_connector.additional_properties = d
        return local_connector

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
