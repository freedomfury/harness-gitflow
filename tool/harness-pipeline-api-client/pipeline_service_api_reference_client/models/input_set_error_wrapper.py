from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.input_set_error_wrapper_uuid_to_error_response_map import InputSetErrorWrapperUuidToErrorResponseMap


T = TypeVar("T", bound="InputSetErrorWrapper")


@_attrs_define
class InputSetErrorWrapper:
    """This contains the error response if the Input Set save failed

    Attributes:
        error_pipeline_yaml (str | Unset): If an Input Set save fails, this field contains the error fields, with the
            field values replaced with a UUID
        uuid_to_error_response_map (InputSetErrorWrapperUuidToErrorResponseMap | Unset): If an Input Set save fails,
            this field contains the map from FQN to why that FQN threw an error
        invalid_input_set_references (list[str] | Unset): List of Input Sets that are invalid
        type_ (str | Unset):
    """

    error_pipeline_yaml: str | Unset = UNSET
    uuid_to_error_response_map: InputSetErrorWrapperUuidToErrorResponseMap | Unset = UNSET
    invalid_input_set_references: list[str] | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_pipeline_yaml = self.error_pipeline_yaml

        uuid_to_error_response_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.uuid_to_error_response_map, Unset):
            uuid_to_error_response_map = self.uuid_to_error_response_map.to_dict()

        invalid_input_set_references: list[str] | Unset = UNSET
        if not isinstance(self.invalid_input_set_references, Unset):
            invalid_input_set_references = self.invalid_input_set_references

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_pipeline_yaml is not UNSET:
            field_dict["errorPipelineYaml"] = error_pipeline_yaml
        if uuid_to_error_response_map is not UNSET:
            field_dict["uuidToErrorResponseMap"] = uuid_to_error_response_map
        if invalid_input_set_references is not UNSET:
            field_dict["invalidInputSetReferences"] = invalid_input_set_references
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.input_set_error_wrapper_uuid_to_error_response_map import (
            InputSetErrorWrapperUuidToErrorResponseMap,
        )

        d = dict(src_dict)
        error_pipeline_yaml = d.pop("errorPipelineYaml", UNSET)

        _uuid_to_error_response_map = d.pop("uuidToErrorResponseMap", UNSET)
        uuid_to_error_response_map: InputSetErrorWrapperUuidToErrorResponseMap | Unset
        if isinstance(_uuid_to_error_response_map, Unset):
            uuid_to_error_response_map = UNSET
        else:
            uuid_to_error_response_map = InputSetErrorWrapperUuidToErrorResponseMap.from_dict(
                _uuid_to_error_response_map
            )

        invalid_input_set_references = cast(list[str], d.pop("invalidInputSetReferences", UNSET))

        type_ = d.pop("type", UNSET)

        input_set_error_wrapper = cls(
            error_pipeline_yaml=error_pipeline_yaml,
            uuid_to_error_response_map=uuid_to_error_response_map,
            invalid_input_set_references=invalid_input_set_references,
            type_=type_,
        )

        input_set_error_wrapper.additional_properties = d
        return input_set_error_wrapper

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
