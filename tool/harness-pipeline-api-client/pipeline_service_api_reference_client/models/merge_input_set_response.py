from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.input_set_error_wrapper import InputSetErrorWrapper


T = TypeVar("T", bound="MergeInputSetResponse")


@_attrs_define
class MergeInputSetResponse:
    """View of the Response of Merging of Input Sets of a Pipeline

    Attributes:
        pipeline_yaml (str | Unset): Merged YAML of all the Input Sets
        complete_pipeline_yaml (str | Unset): Pipeline YAML after merging with the Input Sets
        is_error_response (bool | Unset):
        input_set_error_wrapper (InputSetErrorWrapper | Unset): This contains the error response if the Input Set save
            failed
        error_response (bool | Unset):
    """

    pipeline_yaml: str | Unset = UNSET
    complete_pipeline_yaml: str | Unset = UNSET
    is_error_response: bool | Unset = UNSET
    input_set_error_wrapper: InputSetErrorWrapper | Unset = UNSET
    error_response: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pipeline_yaml = self.pipeline_yaml

        complete_pipeline_yaml = self.complete_pipeline_yaml

        is_error_response = self.is_error_response

        input_set_error_wrapper: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_set_error_wrapper, Unset):
            input_set_error_wrapper = self.input_set_error_wrapper.to_dict()

        error_response = self.error_response

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pipeline_yaml is not UNSET:
            field_dict["pipelineYaml"] = pipeline_yaml
        if complete_pipeline_yaml is not UNSET:
            field_dict["completePipelineYaml"] = complete_pipeline_yaml
        if is_error_response is not UNSET:
            field_dict["isErrorResponse"] = is_error_response
        if input_set_error_wrapper is not UNSET:
            field_dict["inputSetErrorWrapper"] = input_set_error_wrapper
        if error_response is not UNSET:
            field_dict["errorResponse"] = error_response

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.input_set_error_wrapper import InputSetErrorWrapper

        d = dict(src_dict)
        pipeline_yaml = d.pop("pipelineYaml", UNSET)

        complete_pipeline_yaml = d.pop("completePipelineYaml", UNSET)

        is_error_response = d.pop("isErrorResponse", UNSET)

        _input_set_error_wrapper = d.pop("inputSetErrorWrapper", UNSET)
        input_set_error_wrapper: InputSetErrorWrapper | Unset
        if isinstance(_input_set_error_wrapper, Unset):
            input_set_error_wrapper = UNSET
        else:
            input_set_error_wrapper = InputSetErrorWrapper.from_dict(_input_set_error_wrapper)

        error_response = d.pop("errorResponse", UNSET)

        merge_input_set_response = cls(
            pipeline_yaml=pipeline_yaml,
            complete_pipeline_yaml=complete_pipeline_yaml,
            is_error_response=is_error_response,
            input_set_error_wrapper=input_set_error_wrapper,
            error_response=error_response,
        )

        merge_input_set_response.additional_properties = d
        return merge_input_set_response

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
