from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pms_pipeline_summary_response_store_type import (
    PMSPipelineSummaryResponseStoreType,
    check_pms_pipeline_summary_response_store_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_git_details import EntityGitDetails
    from ..models.execution_summary_info import ExecutionSummaryInfo
    from ..models.pms_pipeline_summary_response_filters import PMSPipelineSummaryResponseFilters
    from ..models.pms_pipeline_summary_response_tags import PMSPipelineSummaryResponseTags


T = TypeVar("T", bound="PMSPipelineSummaryResponse")


@_attrs_define
class PMSPipelineSummaryResponse:
    """This is the view of the Pipeline Summary for Pipeline entity defined in Harness.

    Attributes:
        name (str | Unset):
        identifier (str | Unset):
        description (str | Unset):
        tags (PMSPipelineSummaryResponseTags | Unset):
        version (int | Unset):
        num_of_stages (int | Unset):
        created_at (int | Unset):
        last_updated_at (int | Unset):
        modules (list[str] | Unset):
        execution_summary_info (ExecutionSummaryInfo | Unset): This is the view of the Execution Summary
        filters (PMSPipelineSummaryResponseFilters | Unset):
        stage_names (list[str] | Unset):
        git_details (EntityGitDetails | Unset): This contains Validity Details of the Entity
        entity_validity_details (EntityGitDetails | Unset): This contains Validity Details of the Entity
        store_type (PMSPipelineSummaryResponseStoreType | Unset):
        connector_ref (str | Unset):
        is_draft (bool | Unset):
        yaml_version (str | Unset):
        is_inline_hc_entity (bool | Unset):
        enable_dag (bool | Unset):
    """

    name: str | Unset = UNSET
    identifier: str | Unset = UNSET
    description: str | Unset = UNSET
    tags: PMSPipelineSummaryResponseTags | Unset = UNSET
    version: int | Unset = UNSET
    num_of_stages: int | Unset = UNSET
    created_at: int | Unset = UNSET
    last_updated_at: int | Unset = UNSET
    modules: list[str] | Unset = UNSET
    execution_summary_info: ExecutionSummaryInfo | Unset = UNSET
    filters: PMSPipelineSummaryResponseFilters | Unset = UNSET
    stage_names: list[str] | Unset = UNSET
    git_details: EntityGitDetails | Unset = UNSET
    entity_validity_details: EntityGitDetails | Unset = UNSET
    store_type: PMSPipelineSummaryResponseStoreType | Unset = UNSET
    connector_ref: str | Unset = UNSET
    is_draft: bool | Unset = UNSET
    yaml_version: str | Unset = UNSET
    is_inline_hc_entity: bool | Unset = UNSET
    enable_dag: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        identifier = self.identifier

        description = self.description

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        version = self.version

        num_of_stages = self.num_of_stages

        created_at = self.created_at

        last_updated_at = self.last_updated_at

        modules: list[str] | Unset = UNSET
        if not isinstance(self.modules, Unset):
            modules = self.modules

        execution_summary_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.execution_summary_info, Unset):
            execution_summary_info = self.execution_summary_info.to_dict()

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        stage_names: list[str] | Unset = UNSET
        if not isinstance(self.stage_names, Unset):
            stage_names = self.stage_names

        git_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.git_details, Unset):
            git_details = self.git_details.to_dict()

        entity_validity_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entity_validity_details, Unset):
            entity_validity_details = self.entity_validity_details.to_dict()

        store_type: str | Unset = UNSET
        if not isinstance(self.store_type, Unset):
            store_type = self.store_type

        connector_ref = self.connector_ref

        is_draft = self.is_draft

        yaml_version = self.yaml_version

        is_inline_hc_entity = self.is_inline_hc_entity

        enable_dag = self.enable_dag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if version is not UNSET:
            field_dict["version"] = version
        if num_of_stages is not UNSET:
            field_dict["numOfStages"] = num_of_stages
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if last_updated_at is not UNSET:
            field_dict["lastUpdatedAt"] = last_updated_at
        if modules is not UNSET:
            field_dict["modules"] = modules
        if execution_summary_info is not UNSET:
            field_dict["executionSummaryInfo"] = execution_summary_info
        if filters is not UNSET:
            field_dict["filters"] = filters
        if stage_names is not UNSET:
            field_dict["stageNames"] = stage_names
        if git_details is not UNSET:
            field_dict["gitDetails"] = git_details
        if entity_validity_details is not UNSET:
            field_dict["entityValidityDetails"] = entity_validity_details
        if store_type is not UNSET:
            field_dict["storeType"] = store_type
        if connector_ref is not UNSET:
            field_dict["connectorRef"] = connector_ref
        if is_draft is not UNSET:
            field_dict["isDraft"] = is_draft
        if yaml_version is not UNSET:
            field_dict["yamlVersion"] = yaml_version
        if is_inline_hc_entity is not UNSET:
            field_dict["isInlineHCEntity"] = is_inline_hc_entity
        if enable_dag is not UNSET:
            field_dict["enableDAG"] = enable_dag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_git_details import EntityGitDetails
        from ..models.execution_summary_info import ExecutionSummaryInfo
        from ..models.pms_pipeline_summary_response_filters import PMSPipelineSummaryResponseFilters
        from ..models.pms_pipeline_summary_response_tags import PMSPipelineSummaryResponseTags

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        identifier = d.pop("identifier", UNSET)

        description = d.pop("description", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: PMSPipelineSummaryResponseTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = PMSPipelineSummaryResponseTags.from_dict(_tags)

        version = d.pop("version", UNSET)

        num_of_stages = d.pop("numOfStages", UNSET)

        created_at = d.pop("createdAt", UNSET)

        last_updated_at = d.pop("lastUpdatedAt", UNSET)

        modules = cast(list[str], d.pop("modules", UNSET))

        _execution_summary_info = d.pop("executionSummaryInfo", UNSET)
        execution_summary_info: ExecutionSummaryInfo | Unset
        if isinstance(_execution_summary_info, Unset):
            execution_summary_info = UNSET
        else:
            execution_summary_info = ExecutionSummaryInfo.from_dict(_execution_summary_info)

        _filters = d.pop("filters", UNSET)
        filters: PMSPipelineSummaryResponseFilters | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = PMSPipelineSummaryResponseFilters.from_dict(_filters)

        stage_names = cast(list[str], d.pop("stageNames", UNSET))

        _git_details = d.pop("gitDetails", UNSET)
        git_details: EntityGitDetails | Unset
        if isinstance(_git_details, Unset):
            git_details = UNSET
        else:
            git_details = EntityGitDetails.from_dict(_git_details)

        _entity_validity_details = d.pop("entityValidityDetails", UNSET)
        entity_validity_details: EntityGitDetails | Unset
        if isinstance(_entity_validity_details, Unset):
            entity_validity_details = UNSET
        else:
            entity_validity_details = EntityGitDetails.from_dict(_entity_validity_details)

        _store_type = d.pop("storeType", UNSET)
        store_type: PMSPipelineSummaryResponseStoreType | Unset
        if isinstance(_store_type, Unset):
            store_type = UNSET
        else:
            store_type = check_pms_pipeline_summary_response_store_type(_store_type)

        connector_ref = d.pop("connectorRef", UNSET)

        is_draft = d.pop("isDraft", UNSET)

        yaml_version = d.pop("yamlVersion", UNSET)

        is_inline_hc_entity = d.pop("isInlineHCEntity", UNSET)

        enable_dag = d.pop("enableDAG", UNSET)

        pms_pipeline_summary_response = cls(
            name=name,
            identifier=identifier,
            description=description,
            tags=tags,
            version=version,
            num_of_stages=num_of_stages,
            created_at=created_at,
            last_updated_at=last_updated_at,
            modules=modules,
            execution_summary_info=execution_summary_info,
            filters=filters,
            stage_names=stage_names,
            git_details=git_details,
            entity_validity_details=entity_validity_details,
            store_type=store_type,
            connector_ref=connector_ref,
            is_draft=is_draft,
            yaml_version=yaml_version,
            is_inline_hc_entity=is_inline_hc_entity,
            enable_dag=enable_dag,
        )

        pms_pipeline_summary_response.additional_properties = d
        return pms_pipeline_summary_response

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
