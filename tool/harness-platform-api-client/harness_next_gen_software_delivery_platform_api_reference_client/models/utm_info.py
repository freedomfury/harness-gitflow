from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UtmInfo")


@_attrs_define
class UtmInfo:
    """
    Attributes:
        utm_source (str | Unset):
        utm_content (str | Unset):
        utm_medium (str | Unset):
        utm_term (str | Unset):
        utm_campaign (str | Unset):
    """

    utm_source: str | Unset = UNSET
    utm_content: str | Unset = UNSET
    utm_medium: str | Unset = UNSET
    utm_term: str | Unset = UNSET
    utm_campaign: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        utm_source = self.utm_source

        utm_content = self.utm_content

        utm_medium = self.utm_medium

        utm_term = self.utm_term

        utm_campaign = self.utm_campaign

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if utm_source is not UNSET:
            field_dict["utmSource"] = utm_source
        if utm_content is not UNSET:
            field_dict["utmContent"] = utm_content
        if utm_medium is not UNSET:
            field_dict["utmMedium"] = utm_medium
        if utm_term is not UNSET:
            field_dict["utmTerm"] = utm_term
        if utm_campaign is not UNSET:
            field_dict["utmCampaign"] = utm_campaign

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        utm_source = d.pop("utmSource", UNSET)

        utm_content = d.pop("utmContent", UNSET)

        utm_medium = d.pop("utmMedium", UNSET)

        utm_term = d.pop("utmTerm", UNSET)

        utm_campaign = d.pop("utmCampaign", UNSET)

        utm_info = cls(
            utm_source=utm_source,
            utm_content=utm_content,
            utm_medium=utm_medium,
            utm_term=utm_term,
            utm_campaign=utm_campaign,
        )

        utm_info.additional_properties = d
        return utm_info

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
