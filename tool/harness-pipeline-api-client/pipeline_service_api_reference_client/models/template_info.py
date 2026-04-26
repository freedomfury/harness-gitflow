from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_info_template_entity_type import (
    TemplateInfoTemplateEntityType,
    check_template_info_template_entity_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateInfo")


@_attrs_define
class TemplateInfo:
    """
    Attributes:
        template_identifier (str | Unset):
        version_label (str | Unset):
        template_entity_type (TemplateInfoTemplateEntityType | Unset):
    """

    template_identifier: str | Unset = UNSET
    version_label: str | Unset = UNSET
    template_entity_type: TemplateInfoTemplateEntityType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_identifier = self.template_identifier

        version_label = self.version_label

        template_entity_type: str | Unset = UNSET
        if not isinstance(self.template_entity_type, Unset):
            template_entity_type = self.template_entity_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if template_identifier is not UNSET:
            field_dict["templateIdentifier"] = template_identifier
        if version_label is not UNSET:
            field_dict["versionLabel"] = version_label
        if template_entity_type is not UNSET:
            field_dict["templateEntityType"] = template_entity_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        template_identifier = d.pop("templateIdentifier", UNSET)

        version_label = d.pop("versionLabel", UNSET)

        _template_entity_type = d.pop("templateEntityType", UNSET)
        template_entity_type: TemplateInfoTemplateEntityType | Unset
        if isinstance(_template_entity_type, Unset):
            template_entity_type = UNSET
        else:
            template_entity_type = check_template_info_template_entity_type(_template_entity_type)

        template_info = cls(
            template_identifier=template_identifier,
            version_label=version_label,
            template_entity_type=template_entity_type,
        )

        template_info.additional_properties = d
        return template_info

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
