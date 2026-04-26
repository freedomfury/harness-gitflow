from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stages_execution_metadata_expression_values import StagesExecutionMetadataExpressionValues
    from ..models.stages_execution_metadata_stage_identifier_to_name_map import (
        StagesExecutionMetadataStageIdentifierToNameMap,
    )


T = TypeVar("T", bound="StagesExecutionMetadata")


@_attrs_define
class StagesExecutionMetadata:
    """
    Attributes:
        is_stages_execution (bool | Unset):
        full_pipeline_yaml (str | Unset):
        stage_identifiers (list[str] | Unset):
        expression_values (StagesExecutionMetadataExpressionValues | Unset):
        stage_identifier_to_name_map (StagesExecutionMetadataStageIdentifierToNameMap | Unset):
        stages_execution (bool | Unset):
    """

    is_stages_execution: bool | Unset = UNSET
    full_pipeline_yaml: str | Unset = UNSET
    stage_identifiers: list[str] | Unset = UNSET
    expression_values: StagesExecutionMetadataExpressionValues | Unset = UNSET
    stage_identifier_to_name_map: StagesExecutionMetadataStageIdentifierToNameMap | Unset = UNSET
    stages_execution: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_stages_execution = self.is_stages_execution

        full_pipeline_yaml = self.full_pipeline_yaml

        stage_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.stage_identifiers, Unset):
            stage_identifiers = self.stage_identifiers

        expression_values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expression_values, Unset):
            expression_values = self.expression_values.to_dict()

        stage_identifier_to_name_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stage_identifier_to_name_map, Unset):
            stage_identifier_to_name_map = self.stage_identifier_to_name_map.to_dict()

        stages_execution = self.stages_execution

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_stages_execution is not UNSET:
            field_dict["isStagesExecution"] = is_stages_execution
        if full_pipeline_yaml is not UNSET:
            field_dict["fullPipelineYaml"] = full_pipeline_yaml
        if stage_identifiers is not UNSET:
            field_dict["stageIdentifiers"] = stage_identifiers
        if expression_values is not UNSET:
            field_dict["expressionValues"] = expression_values
        if stage_identifier_to_name_map is not UNSET:
            field_dict["stageIdentifierToNameMap"] = stage_identifier_to_name_map
        if stages_execution is not UNSET:
            field_dict["stagesExecution"] = stages_execution

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stages_execution_metadata_expression_values import StagesExecutionMetadataExpressionValues
        from ..models.stages_execution_metadata_stage_identifier_to_name_map import (
            StagesExecutionMetadataStageIdentifierToNameMap,
        )

        d = dict(src_dict)
        is_stages_execution = d.pop("isStagesExecution", UNSET)

        full_pipeline_yaml = d.pop("fullPipelineYaml", UNSET)

        stage_identifiers = cast(list[str], d.pop("stageIdentifiers", UNSET))

        _expression_values = d.pop("expressionValues", UNSET)
        expression_values: StagesExecutionMetadataExpressionValues | Unset
        if isinstance(_expression_values, Unset):
            expression_values = UNSET
        else:
            expression_values = StagesExecutionMetadataExpressionValues.from_dict(_expression_values)

        _stage_identifier_to_name_map = d.pop("stageIdentifierToNameMap", UNSET)
        stage_identifier_to_name_map: StagesExecutionMetadataStageIdentifierToNameMap | Unset
        if isinstance(_stage_identifier_to_name_map, Unset):
            stage_identifier_to_name_map = UNSET
        else:
            stage_identifier_to_name_map = StagesExecutionMetadataStageIdentifierToNameMap.from_dict(
                _stage_identifier_to_name_map
            )

        stages_execution = d.pop("stagesExecution", UNSET)

        stages_execution_metadata = cls(
            is_stages_execution=is_stages_execution,
            full_pipeline_yaml=full_pipeline_yaml,
            stage_identifiers=stage_identifiers,
            expression_values=expression_values,
            stage_identifier_to_name_map=stage_identifier_to_name_map,
            stages_execution=stages_execution,
        )

        stages_execution_metadata.additional_properties = d
        return stages_execution_metadata

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
