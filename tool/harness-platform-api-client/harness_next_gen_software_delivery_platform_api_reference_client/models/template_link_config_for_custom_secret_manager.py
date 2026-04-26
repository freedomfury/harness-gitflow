from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_link_config_for_custom_secret_manager_template_inputs import (
        TemplateLinkConfigForCustomSecretManagerTemplateInputs,
    )


T = TypeVar("T", bound="TemplateLinkConfigForCustomSecretManager")


@_attrs_define
class TemplateLinkConfigForCustomSecretManager:
    """
    Attributes:
        template_ref (str):
        version_label (str):
        template_inputs (TemplateLinkConfigForCustomSecretManagerTemplateInputs | Unset):
    """

    template_ref: str
    version_label: str
    template_inputs: TemplateLinkConfigForCustomSecretManagerTemplateInputs | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_ref = self.template_ref

        version_label = self.version_label

        template_inputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template_inputs, Unset):
            template_inputs = self.template_inputs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "templateRef": template_ref,
                "versionLabel": version_label,
            }
        )
        if template_inputs is not UNSET:
            field_dict["templateInputs"] = template_inputs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_link_config_for_custom_secret_manager_template_inputs import (
            TemplateLinkConfigForCustomSecretManagerTemplateInputs,
        )

        d = dict(src_dict)
        template_ref = d.pop("templateRef")

        version_label = d.pop("versionLabel")

        _template_inputs = d.pop("templateInputs", UNSET)
        template_inputs: TemplateLinkConfigForCustomSecretManagerTemplateInputs | Unset
        if isinstance(_template_inputs, Unset):
            template_inputs = UNSET
        else:
            template_inputs = TemplateLinkConfigForCustomSecretManagerTemplateInputs.from_dict(_template_inputs)

        template_link_config_for_custom_secret_manager = cls(
            template_ref=template_ref,
            version_label=version_label,
            template_inputs=template_inputs,
        )

        template_link_config_for_custom_secret_manager.additional_properties = d
        return template_link_config_for_custom_secret_manager

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
