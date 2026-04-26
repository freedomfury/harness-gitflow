from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LicenseUsage")


@_attrs_define
class LicenseUsage:
    """This is the view of a License Usage object defined in Harness

    Attributes:
        class_name (str):
        account_identifier (str | Unset):
        module (str | Unset):
        timestamp (int | Unset):
    """

    class_name: str
    account_identifier: str | Unset = UNSET
    module: str | Unset = UNSET
    timestamp: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        class_name = self.class_name

        account_identifier = self.account_identifier

        module = self.module

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "className": class_name,
            }
        )
        if account_identifier is not UNSET:
            field_dict["accountIdentifier"] = account_identifier
        if module is not UNSET:
            field_dict["module"] = module
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        class_name = d.pop("className")

        account_identifier = d.pop("accountIdentifier", UNSET)

        module = d.pop("module", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        license_usage = cls(
            class_name=class_name,
            account_identifier=account_identifier,
            module=module,
            timestamp=timestamp,
        )

        license_usage.additional_properties = d
        return license_usage

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
