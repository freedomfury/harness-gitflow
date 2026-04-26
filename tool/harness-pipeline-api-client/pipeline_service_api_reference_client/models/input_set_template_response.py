from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.input_set_details import InputSetDetails


T = TypeVar("T", bound="InputSetTemplateResponse")


@_attrs_define
class InputSetTemplateResponse:
    """This contains the Runtime Input YAML used during a Pipeline Execution.

    Attributes:
        input_set_template_yaml (str | Unset): Template Yaml at the time of execution
        input_set_yaml (str | Unset): Input set Yaml used during execution
        input_set_details (list[InputSetDetails] | Unset): Details of inputsets used in this execution
        input_set_branch_name (str | Unset): Branch name from which input sets were fetched
        resolved_yaml (str | Unset): Resolved Yaml with all expressions and runtime inputs resolved
    """

    input_set_template_yaml: str | Unset = UNSET
    input_set_yaml: str | Unset = UNSET
    input_set_details: list[InputSetDetails] | Unset = UNSET
    input_set_branch_name: str | Unset = UNSET
    resolved_yaml: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_set_template_yaml = self.input_set_template_yaml

        input_set_yaml = self.input_set_yaml

        input_set_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.input_set_details, Unset):
            input_set_details = []
            for input_set_details_item_data in self.input_set_details:
                input_set_details_item = input_set_details_item_data.to_dict()
                input_set_details.append(input_set_details_item)

        input_set_branch_name = self.input_set_branch_name

        resolved_yaml = self.resolved_yaml

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if input_set_template_yaml is not UNSET:
            field_dict["inputSetTemplateYaml"] = input_set_template_yaml
        if input_set_yaml is not UNSET:
            field_dict["inputSetYaml"] = input_set_yaml
        if input_set_details is not UNSET:
            field_dict["inputSetDetails"] = input_set_details
        if input_set_branch_name is not UNSET:
            field_dict["inputSetBranchName"] = input_set_branch_name
        if resolved_yaml is not UNSET:
            field_dict["resolvedYaml"] = resolved_yaml

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.input_set_details import InputSetDetails

        d = dict(src_dict)
        input_set_template_yaml = d.pop("inputSetTemplateYaml", UNSET)

        input_set_yaml = d.pop("inputSetYaml", UNSET)

        _input_set_details = d.pop("inputSetDetails", UNSET)
        input_set_details: list[InputSetDetails] | Unset = UNSET
        if _input_set_details is not UNSET:
            input_set_details = []
            for input_set_details_item_data in _input_set_details:
                input_set_details_item = InputSetDetails.from_dict(input_set_details_item_data)

                input_set_details.append(input_set_details_item)

        input_set_branch_name = d.pop("inputSetBranchName", UNSET)

        resolved_yaml = d.pop("resolvedYaml", UNSET)

        input_set_template_response = cls(
            input_set_template_yaml=input_set_template_yaml,
            input_set_yaml=input_set_yaml,
            input_set_details=input_set_details,
            input_set_branch_name=input_set_branch_name,
            resolved_yaml=resolved_yaml,
        )

        input_set_template_response.additional_properties = d
        return input_set_template_response

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
