from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MergeInputSetRequest")


@_attrs_define
class MergeInputSetRequest:
    """Contains list of Input Set references and Stage Ids

    Attributes:
        input_set_references (list[str] | Unset): List of Input Set References to be merged
        with_merged_pipeline_yaml (bool | Unset): This is a boolean value that indicates if the response must contain
            the YAML for the merged Pipeline. The default value is False.
        stage_identifiers (list[str] | Unset): List of Stage Ids. Input Sets corresponding to these Ids will be merged.
        last_yaml_to_merge (str | Unset): Runtime Input Yaml needed to be merged into the result of the merged Yaml of
            the inputSetReferences
        input_set_branch_name (str | Unset): InputSetBranchName
    """

    input_set_references: list[str] | Unset = UNSET
    with_merged_pipeline_yaml: bool | Unset = UNSET
    stage_identifiers: list[str] | Unset = UNSET
    last_yaml_to_merge: str | Unset = UNSET
    input_set_branch_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_set_references: list[str] | Unset = UNSET
        if not isinstance(self.input_set_references, Unset):
            input_set_references = self.input_set_references

        with_merged_pipeline_yaml = self.with_merged_pipeline_yaml

        stage_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.stage_identifiers, Unset):
            stage_identifiers = self.stage_identifiers

        last_yaml_to_merge = self.last_yaml_to_merge

        input_set_branch_name = self.input_set_branch_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if input_set_references is not UNSET:
            field_dict["inputSetReferences"] = input_set_references
        if with_merged_pipeline_yaml is not UNSET:
            field_dict["withMergedPipelineYaml"] = with_merged_pipeline_yaml
        if stage_identifiers is not UNSET:
            field_dict["stageIdentifiers"] = stage_identifiers
        if last_yaml_to_merge is not UNSET:
            field_dict["lastYamlToMerge"] = last_yaml_to_merge
        if input_set_branch_name is not UNSET:
            field_dict["inputSetBranchName"] = input_set_branch_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_set_references = cast(list[str], d.pop("inputSetReferences", UNSET))

        with_merged_pipeline_yaml = d.pop("withMergedPipelineYaml", UNSET)

        stage_identifiers = cast(list[str], d.pop("stageIdentifiers", UNSET))

        last_yaml_to_merge = d.pop("lastYamlToMerge", UNSET)

        input_set_branch_name = d.pop("inputSetBranchName", UNSET)

        merge_input_set_request = cls(
            input_set_references=input_set_references,
            with_merged_pipeline_yaml=with_merged_pipeline_yaml,
            stage_identifiers=stage_identifiers,
            last_yaml_to_merge=last_yaml_to_merge,
            input_set_branch_name=input_set_branch_name,
        )

        merge_input_set_request.additional_properties = d
        return merge_input_set_request

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
