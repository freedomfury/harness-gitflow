from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookDetails")


@_attrs_define
class WebhookDetails:
    """
    Attributes:
        webhook_secret (str | Unset):
        webhook_source_repo (str | Unset):
    """

    webhook_secret: str | Unset = UNSET
    webhook_source_repo: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        webhook_secret = self.webhook_secret

        webhook_source_repo = self.webhook_source_repo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if webhook_secret is not UNSET:
            field_dict["webhookSecret"] = webhook_secret
        if webhook_source_repo is not UNSET:
            field_dict["webhookSourceRepo"] = webhook_source_repo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        webhook_secret = d.pop("webhookSecret", UNSET)

        webhook_source_repo = d.pop("webhookSourceRepo", UNSET)

        webhook_details = cls(
            webhook_secret=webhook_secret,
            webhook_source_repo=webhook_source_repo,
        )

        webhook_details.additional_properties = d
        return webhook_details

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
