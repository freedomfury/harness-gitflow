from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NGTriggerMetaData")


@_attrs_define
class NGTriggerMetaData:
    """
    Attributes:
        polling_document_id (str | Unset):
        build (str | Unset):
    """

    polling_document_id: str | Unset = UNSET
    build: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        polling_document_id = self.polling_document_id

        build = self.build

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if polling_document_id is not UNSET:
            field_dict["pollingDocumentId"] = polling_document_id
        if build is not UNSET:
            field_dict["build"] = build

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        polling_document_id = d.pop("pollingDocumentId", UNSET)

        build = d.pop("build", UNSET)

        ng_trigger_meta_data = cls(
            polling_document_id=polling_document_id,
            build=build,
        )

        ng_trigger_meta_data.additional_properties = d
        return ng_trigger_meta_data

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
