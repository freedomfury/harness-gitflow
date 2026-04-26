from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SecretSpec")


@_attrs_define
class SecretSpec:
    """This has details of the Secret defined in Harness.

    Attributes:
        type_ (str):
        error_message_for_invalid_yaml (str | Unset):
    """

    type_: str
    error_message_for_invalid_yaml: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        error_message_for_invalid_yaml = self.error_message_for_invalid_yaml

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if error_message_for_invalid_yaml is not UNSET:
            field_dict["errorMessageForInvalidYaml"] = error_message_for_invalid_yaml

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        error_message_for_invalid_yaml = d.pop("errorMessageForInvalidYaml", UNSET)

        secret_spec = cls(
            type_=type_,
            error_message_for_invalid_yaml=error_message_for_invalid_yaml,
        )

        secret_spec.additional_properties = d
        return secret_spec

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
