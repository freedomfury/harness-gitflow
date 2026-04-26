from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inputs_metadata import InputsMetadata


T = TypeVar("T", bound="EntityInputsMetadata")


@_attrs_define
class EntityInputsMetadata:
    """Metadata for runtime input for Entities.

    Attributes:
        identifier (str | Unset):
        entity_type (str | Unset):
        inputs_metadata_list (list[InputsMetadata] | Unset):
    """

    identifier: str | Unset = UNSET
    entity_type: str | Unset = UNSET
    inputs_metadata_list: list[InputsMetadata] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        entity_type = self.entity_type

        inputs_metadata_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inputs_metadata_list, Unset):
            inputs_metadata_list = []
            for inputs_metadata_list_item_data in self.inputs_metadata_list:
                inputs_metadata_list_item = inputs_metadata_list_item_data.to_dict()
                inputs_metadata_list.append(inputs_metadata_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if inputs_metadata_list is not UNSET:
            field_dict["inputsMetadataList"] = inputs_metadata_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inputs_metadata import InputsMetadata

        d = dict(src_dict)
        identifier = d.pop("identifier", UNSET)

        entity_type = d.pop("entityType", UNSET)

        _inputs_metadata_list = d.pop("inputsMetadataList", UNSET)
        inputs_metadata_list: list[InputsMetadata] | Unset = UNSET
        if _inputs_metadata_list is not UNSET:
            inputs_metadata_list = []
            for inputs_metadata_list_item_data in _inputs_metadata_list:
                inputs_metadata_list_item = InputsMetadata.from_dict(inputs_metadata_list_item_data)

                inputs_metadata_list.append(inputs_metadata_list_item)

        entity_inputs_metadata = cls(
            identifier=identifier,
            entity_type=entity_type,
            inputs_metadata_list=inputs_metadata_list,
        )

        entity_inputs_metadata.additional_properties = d
        return entity_inputs_metadata

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
