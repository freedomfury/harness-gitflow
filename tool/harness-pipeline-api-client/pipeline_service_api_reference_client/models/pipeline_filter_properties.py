from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pipeline_filter_properties_filter_type import (
    PipelineFilterPropertiesFilterType,
    check_pipeline_filter_properties_filter_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ng_tag import NGTag
    from ..models.pipeline_filter_properties_module_properties import PipelineFilterPropertiesModuleProperties
    from ..models.pipeline_filter_properties_tags import PipelineFilterPropertiesTags


T = TypeVar("T", bound="PipelineFilterProperties")


@_attrs_define
class PipelineFilterProperties:
    """Properties of the Pipelines Filter defined in Harness

    Attributes:
        filter_type (PipelineFilterPropertiesFilterType): This specifies the corresponding Entity of the filter.
        tags (PipelineFilterPropertiesTags | Unset): Filter tags as a key-value pair.
        pipeline_tags (list[NGTag] | Unset): This is the list of the Pipeline Tags on which the filter will be applied.
        pipeline_identifiers (list[str] | Unset): This is the list of the Pipeline Identifiers on which the filter will
            be applied.
        name (str | Unset): This is the Pipeline Name on which the filter will be applied.
        description (str | Unset): This is the Pipeline Description on which the filter will be applied.
        module_properties (PipelineFilterPropertiesModuleProperties | Unset): These are the Module Properties on which
            the filter will be applied.
        repo_name (str | Unset): This is the Pipeline repo filter on which the filter will be applied.
    """

    filter_type: PipelineFilterPropertiesFilterType
    tags: PipelineFilterPropertiesTags | Unset = UNSET
    pipeline_tags: list[NGTag] | Unset = UNSET
    pipeline_identifiers: list[str] | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    module_properties: PipelineFilterPropertiesModuleProperties | Unset = UNSET
    repo_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_type: str = self.filter_type

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        pipeline_tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pipeline_tags, Unset):
            pipeline_tags = []
            for pipeline_tags_item_data in self.pipeline_tags:
                pipeline_tags_item = pipeline_tags_item_data.to_dict()
                pipeline_tags.append(pipeline_tags_item)

        pipeline_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.pipeline_identifiers, Unset):
            pipeline_identifiers = self.pipeline_identifiers

        name = self.name

        description = self.description

        module_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.module_properties, Unset):
            module_properties = self.module_properties.to_dict()

        repo_name = self.repo_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filterType": filter_type,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if pipeline_tags is not UNSET:
            field_dict["pipelineTags"] = pipeline_tags
        if pipeline_identifiers is not UNSET:
            field_dict["pipelineIdentifiers"] = pipeline_identifiers
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if module_properties is not UNSET:
            field_dict["moduleProperties"] = module_properties
        if repo_name is not UNSET:
            field_dict["repoName"] = repo_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ng_tag import NGTag
        from ..models.pipeline_filter_properties_module_properties import PipelineFilterPropertiesModuleProperties
        from ..models.pipeline_filter_properties_tags import PipelineFilterPropertiesTags

        d = dict(src_dict)
        filter_type = check_pipeline_filter_properties_filter_type(d.pop("filterType"))

        _tags = d.pop("tags", UNSET)
        tags: PipelineFilterPropertiesTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = PipelineFilterPropertiesTags.from_dict(_tags)

        _pipeline_tags = d.pop("pipelineTags", UNSET)
        pipeline_tags: list[NGTag] | Unset = UNSET
        if _pipeline_tags is not UNSET:
            pipeline_tags = []
            for pipeline_tags_item_data in _pipeline_tags:
                pipeline_tags_item = NGTag.from_dict(pipeline_tags_item_data)

                pipeline_tags.append(pipeline_tags_item)

        pipeline_identifiers = cast(list[str], d.pop("pipelineIdentifiers", UNSET))

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _module_properties = d.pop("moduleProperties", UNSET)
        module_properties: PipelineFilterPropertiesModuleProperties | Unset
        if isinstance(_module_properties, Unset):
            module_properties = UNSET
        else:
            module_properties = PipelineFilterPropertiesModuleProperties.from_dict(_module_properties)

        repo_name = d.pop("repoName", UNSET)

        pipeline_filter_properties = cls(
            filter_type=filter_type,
            tags=tags,
            pipeline_tags=pipeline_tags,
            pipeline_identifiers=pipeline_identifiers,
            name=name,
            description=description,
            module_properties=module_properties,
            repo_name=repo_name,
        )

        pipeline_filter_properties.additional_properties = d
        return pipeline_filter_properties

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
