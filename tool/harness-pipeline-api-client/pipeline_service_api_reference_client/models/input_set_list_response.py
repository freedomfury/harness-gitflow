from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.input_set_list_response_input_set_type import (
    InputSetListResponseInputSetType,
    check_input_set_list_response_input_set_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InputSetListResponse")


@_attrs_define
class InputSetListResponse:
    """This is the response of InputSet list call.

    Attributes:
        identifier (str | Unset): Input Set Identifier
        name (str | Unset): Input Set Name
        pipeline_identifier (str | Unset): Pipeline Identifier for the entity.
        input_set_id_with_pipeline_id (str | Unset): InputSet Identifier prefixed with Pipeline Identifier.
        description (str | Unset): Input Set description
        input_set_type (InputSetListResponseInputSetType | Unset): Type of Input Set. The default value is ALL.
    """

    identifier: str | Unset = UNSET
    name: str | Unset = UNSET
    pipeline_identifier: str | Unset = UNSET
    input_set_id_with_pipeline_id: str | Unset = UNSET
    description: str | Unset = UNSET
    input_set_type: InputSetListResponseInputSetType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        name = self.name

        pipeline_identifier = self.pipeline_identifier

        input_set_id_with_pipeline_id = self.input_set_id_with_pipeline_id

        description = self.description

        input_set_type: str | Unset = UNSET
        if not isinstance(self.input_set_type, Unset):
            input_set_type = self.input_set_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if name is not UNSET:
            field_dict["name"] = name
        if pipeline_identifier is not UNSET:
            field_dict["pipelineIdentifier"] = pipeline_identifier
        if input_set_id_with_pipeline_id is not UNSET:
            field_dict["inputSetIdWithPipelineId"] = input_set_id_with_pipeline_id
        if description is not UNSET:
            field_dict["description"] = description
        if input_set_type is not UNSET:
            field_dict["inputSetType"] = input_set_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = d.pop("identifier", UNSET)

        name = d.pop("name", UNSET)

        pipeline_identifier = d.pop("pipelineIdentifier", UNSET)

        input_set_id_with_pipeline_id = d.pop("inputSetIdWithPipelineId", UNSET)

        description = d.pop("description", UNSET)

        _input_set_type = d.pop("inputSetType", UNSET)
        input_set_type: InputSetListResponseInputSetType | Unset
        if isinstance(_input_set_type, Unset):
            input_set_type = UNSET
        else:
            input_set_type = check_input_set_list_response_input_set_type(_input_set_type)

        input_set_list_response = cls(
            identifier=identifier,
            name=name,
            pipeline_identifier=pipeline_identifier,
            input_set_id_with_pipeline_id=input_set_id_with_pipeline_id,
            description=description,
            input_set_type=input_set_type,
        )

        input_set_list_response.additional_properties = d
        return input_set_list_response

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
