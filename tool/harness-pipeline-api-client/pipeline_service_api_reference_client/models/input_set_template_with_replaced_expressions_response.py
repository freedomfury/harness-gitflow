from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_inputs_metadata import EntityInputsMetadata
    from ..models.input_set_template_with_replaced_expressions_response_replaced_expressions_per_stage import (
        InputSetTemplateWithReplacedExpressionsResponseReplacedExpressionsPerStage,
    )


T = TypeVar("T", bound="InputSetTemplateWithReplacedExpressionsResponse")


@_attrs_define
class InputSetTemplateWithReplacedExpressionsResponse:
    """This is the Runtime Input Template for a Pipeline defined in Harness.

    Attributes:
        input_set_template_yaml (str | Unset): Runtime Input template for the Pipeline
        replaced_expressions (list[str] | Unset): List of Expressions that need to be replaced for running selected
            Stages. Empty if the full Pipeline is being run or no expressions need to be replaced
        modules (list[str] | Unset): Modules in which the Pipeline belongs
        has_input_sets (bool | Unset): Tells whether there are any Input Sets for this Pipeline or not.
        replaced_expressions_per_stage (InputSetTemplateWithReplacedExpressionsResponseReplacedExpressionsPerStage |
            Unset):
        inputs_metadata (list[EntityInputsMetadata] | Unset): Metadata for runtime input for Entities.
    """

    input_set_template_yaml: str | Unset = UNSET
    replaced_expressions: list[str] | Unset = UNSET
    modules: list[str] | Unset = UNSET
    has_input_sets: bool | Unset = UNSET
    replaced_expressions_per_stage: (
        InputSetTemplateWithReplacedExpressionsResponseReplacedExpressionsPerStage | Unset
    ) = UNSET
    inputs_metadata: list[EntityInputsMetadata] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_set_template_yaml = self.input_set_template_yaml

        replaced_expressions: list[str] | Unset = UNSET
        if not isinstance(self.replaced_expressions, Unset):
            replaced_expressions = self.replaced_expressions

        modules: list[str] | Unset = UNSET
        if not isinstance(self.modules, Unset):
            modules = self.modules

        has_input_sets = self.has_input_sets

        replaced_expressions_per_stage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.replaced_expressions_per_stage, Unset):
            replaced_expressions_per_stage = self.replaced_expressions_per_stage.to_dict()

        inputs_metadata: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inputs_metadata, Unset):
            inputs_metadata = []
            for inputs_metadata_item_data in self.inputs_metadata:
                inputs_metadata_item = inputs_metadata_item_data.to_dict()
                inputs_metadata.append(inputs_metadata_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if input_set_template_yaml is not UNSET:
            field_dict["inputSetTemplateYaml"] = input_set_template_yaml
        if replaced_expressions is not UNSET:
            field_dict["replacedExpressions"] = replaced_expressions
        if modules is not UNSET:
            field_dict["modules"] = modules
        if has_input_sets is not UNSET:
            field_dict["hasInputSets"] = has_input_sets
        if replaced_expressions_per_stage is not UNSET:
            field_dict["replacedExpressionsPerStage"] = replaced_expressions_per_stage
        if inputs_metadata is not UNSET:
            field_dict["inputsMetadata"] = inputs_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_inputs_metadata import EntityInputsMetadata
        from ..models.input_set_template_with_replaced_expressions_response_replaced_expressions_per_stage import (
            InputSetTemplateWithReplacedExpressionsResponseReplacedExpressionsPerStage,
        )

        d = dict(src_dict)
        input_set_template_yaml = d.pop("inputSetTemplateYaml", UNSET)

        replaced_expressions = cast(list[str], d.pop("replacedExpressions", UNSET))

        modules = cast(list[str], d.pop("modules", UNSET))

        has_input_sets = d.pop("hasInputSets", UNSET)

        _replaced_expressions_per_stage = d.pop("replacedExpressionsPerStage", UNSET)
        replaced_expressions_per_stage: (
            InputSetTemplateWithReplacedExpressionsResponseReplacedExpressionsPerStage | Unset
        )
        if isinstance(_replaced_expressions_per_stage, Unset):
            replaced_expressions_per_stage = UNSET
        else:
            replaced_expressions_per_stage = (
                InputSetTemplateWithReplacedExpressionsResponseReplacedExpressionsPerStage.from_dict(
                    _replaced_expressions_per_stage
                )
            )

        _inputs_metadata = d.pop("inputsMetadata", UNSET)
        inputs_metadata: list[EntityInputsMetadata] | Unset = UNSET
        if _inputs_metadata is not UNSET:
            inputs_metadata = []
            for inputs_metadata_item_data in _inputs_metadata:
                inputs_metadata_item = EntityInputsMetadata.from_dict(inputs_metadata_item_data)

                inputs_metadata.append(inputs_metadata_item)

        input_set_template_with_replaced_expressions_response = cls(
            input_set_template_yaml=input_set_template_yaml,
            replaced_expressions=replaced_expressions,
            modules=modules,
            has_input_sets=has_input_sets,
            replaced_expressions_per_stage=replaced_expressions_per_stage,
            inputs_metadata=inputs_metadata,
        )

        input_set_template_with_replaced_expressions_response.additional_properties = d
        return input_set_template_with_replaced_expressions_response

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
