from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceAccountConfig")


@_attrs_define
class ServiceAccountConfig:
    """Service Account configuration associated with this Account.

    Attributes:
        api_key_limit (int | Unset):
        token_limit (int | Unset):
    """

    api_key_limit: int | Unset = UNSET
    token_limit: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key_limit = self.api_key_limit

        token_limit = self.token_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_key_limit is not UNSET:
            field_dict["apiKeyLimit"] = api_key_limit
        if token_limit is not UNSET:
            field_dict["tokenLimit"] = token_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key_limit = d.pop("apiKeyLimit", UNSET)

        token_limit = d.pop("tokenLimit", UNSET)

        service_account_config = cls(
            api_key_limit=api_key_limit,
            token_limit=token_limit,
        )

        service_account_config.additional_properties = d
        return service_account_config

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
