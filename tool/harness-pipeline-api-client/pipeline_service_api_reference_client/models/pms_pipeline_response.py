from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pms_pipeline_response_store_type import (
    PMSPipelineResponseStoreType,
    check_pms_pipeline_response_store_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cache_response_metadata import CacheResponseMetadata
    from ..models.entity_git_details import EntityGitDetails
    from ..models.governance_metadata import GovernanceMetadata
    from ..models.public_access_response import PublicAccessResponse
    from ..models.validate_template_inputs_response_dto import ValidateTemplateInputsResponseDTO
    from ..models.yaml_schema_error_wrapper_dto import YamlSchemaErrorWrapperDTO


T = TypeVar("T", bound="PMSPipelineResponse")


@_attrs_define
class PMSPipelineResponse:
    """This contains pipeline yaml with the version.

    Attributes:
        yaml_pipeline (str | Unset):
        resolved_templates_pipeline_yaml (str | Unset): Pipeline YAML after resolving templates
        git_details (EntityGitDetails | Unset): This contains Validity Details of the Entity
        entity_validity_details (EntityGitDetails | Unset): This contains Validity Details of the Entity
        modules (list[str] | Unset):
        governance_metadata (GovernanceMetadata | Unset):
        yaml_schema_error_wrapper (YamlSchemaErrorWrapperDTO | Unset):
        validate_template_inputs_response (ValidateTemplateInputsResponseDTO | Unset):
        cache_response (CacheResponseMetadata | Unset): This tells the state of the cache from which the template was
            fetched.
        validation_uuid (str | Unset):
        store_type (PMSPipelineResponseStoreType | Unset):
        public_access_response (PublicAccessResponse | Unset):
        connector_ref (str | Unset):
        allow_dynamic_executions (bool | Unset):
        is_inline_hc_entity (bool | Unset):
    """

    yaml_pipeline: str | Unset = UNSET
    resolved_templates_pipeline_yaml: str | Unset = UNSET
    git_details: EntityGitDetails | Unset = UNSET
    entity_validity_details: EntityGitDetails | Unset = UNSET
    modules: list[str] | Unset = UNSET
    governance_metadata: GovernanceMetadata | Unset = UNSET
    yaml_schema_error_wrapper: YamlSchemaErrorWrapperDTO | Unset = UNSET
    validate_template_inputs_response: ValidateTemplateInputsResponseDTO | Unset = UNSET
    cache_response: CacheResponseMetadata | Unset = UNSET
    validation_uuid: str | Unset = UNSET
    store_type: PMSPipelineResponseStoreType | Unset = UNSET
    public_access_response: PublicAccessResponse | Unset = UNSET
    connector_ref: str | Unset = UNSET
    allow_dynamic_executions: bool | Unset = UNSET
    is_inline_hc_entity: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        yaml_pipeline = self.yaml_pipeline

        resolved_templates_pipeline_yaml = self.resolved_templates_pipeline_yaml

        git_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.git_details, Unset):
            git_details = self.git_details.to_dict()

        entity_validity_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entity_validity_details, Unset):
            entity_validity_details = self.entity_validity_details.to_dict()

        modules: list[str] | Unset = UNSET
        if not isinstance(self.modules, Unset):
            modules = self.modules

        governance_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.governance_metadata, Unset):
            governance_metadata = self.governance_metadata.to_dict()

        yaml_schema_error_wrapper: dict[str, Any] | Unset = UNSET
        if not isinstance(self.yaml_schema_error_wrapper, Unset):
            yaml_schema_error_wrapper = self.yaml_schema_error_wrapper.to_dict()

        validate_template_inputs_response: dict[str, Any] | Unset = UNSET
        if not isinstance(self.validate_template_inputs_response, Unset):
            validate_template_inputs_response = self.validate_template_inputs_response.to_dict()

        cache_response: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cache_response, Unset):
            cache_response = self.cache_response.to_dict()

        validation_uuid = self.validation_uuid

        store_type: str | Unset = UNSET
        if not isinstance(self.store_type, Unset):
            store_type = self.store_type

        public_access_response: dict[str, Any] | Unset = UNSET
        if not isinstance(self.public_access_response, Unset):
            public_access_response = self.public_access_response.to_dict()

        connector_ref = self.connector_ref

        allow_dynamic_executions = self.allow_dynamic_executions

        is_inline_hc_entity = self.is_inline_hc_entity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if yaml_pipeline is not UNSET:
            field_dict["yamlPipeline"] = yaml_pipeline
        if resolved_templates_pipeline_yaml is not UNSET:
            field_dict["resolvedTemplatesPipelineYaml"] = resolved_templates_pipeline_yaml
        if git_details is not UNSET:
            field_dict["gitDetails"] = git_details
        if entity_validity_details is not UNSET:
            field_dict["entityValidityDetails"] = entity_validity_details
        if modules is not UNSET:
            field_dict["modules"] = modules
        if governance_metadata is not UNSET:
            field_dict["governanceMetadata"] = governance_metadata
        if yaml_schema_error_wrapper is not UNSET:
            field_dict["yamlSchemaErrorWrapper"] = yaml_schema_error_wrapper
        if validate_template_inputs_response is not UNSET:
            field_dict["validateTemplateInputsResponse"] = validate_template_inputs_response
        if cache_response is not UNSET:
            field_dict["cacheResponse"] = cache_response
        if validation_uuid is not UNSET:
            field_dict["validationUuid"] = validation_uuid
        if store_type is not UNSET:
            field_dict["storeType"] = store_type
        if public_access_response is not UNSET:
            field_dict["publicAccessResponse"] = public_access_response
        if connector_ref is not UNSET:
            field_dict["connectorRef"] = connector_ref
        if allow_dynamic_executions is not UNSET:
            field_dict["allowDynamicExecutions"] = allow_dynamic_executions
        if is_inline_hc_entity is not UNSET:
            field_dict["isInlineHCEntity"] = is_inline_hc_entity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cache_response_metadata import CacheResponseMetadata
        from ..models.entity_git_details import EntityGitDetails
        from ..models.governance_metadata import GovernanceMetadata
        from ..models.public_access_response import PublicAccessResponse
        from ..models.validate_template_inputs_response_dto import ValidateTemplateInputsResponseDTO
        from ..models.yaml_schema_error_wrapper_dto import YamlSchemaErrorWrapperDTO

        d = dict(src_dict)
        yaml_pipeline = d.pop("yamlPipeline", UNSET)

        resolved_templates_pipeline_yaml = d.pop("resolvedTemplatesPipelineYaml", UNSET)

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

        modules = cast(list[str], d.pop("modules", UNSET))

        _governance_metadata = d.pop("governanceMetadata", UNSET)
        governance_metadata: GovernanceMetadata | Unset
        if isinstance(_governance_metadata, Unset):
            governance_metadata = UNSET
        else:
            governance_metadata = GovernanceMetadata.from_dict(_governance_metadata)

        _yaml_schema_error_wrapper = d.pop("yamlSchemaErrorWrapper", UNSET)
        yaml_schema_error_wrapper: YamlSchemaErrorWrapperDTO | Unset
        if isinstance(_yaml_schema_error_wrapper, Unset):
            yaml_schema_error_wrapper = UNSET
        else:
            yaml_schema_error_wrapper = YamlSchemaErrorWrapperDTO.from_dict(_yaml_schema_error_wrapper)

        _validate_template_inputs_response = d.pop("validateTemplateInputsResponse", UNSET)
        validate_template_inputs_response: ValidateTemplateInputsResponseDTO | Unset
        if isinstance(_validate_template_inputs_response, Unset):
            validate_template_inputs_response = UNSET
        else:
            validate_template_inputs_response = ValidateTemplateInputsResponseDTO.from_dict(
                _validate_template_inputs_response
            )

        _cache_response = d.pop("cacheResponse", UNSET)
        cache_response: CacheResponseMetadata | Unset
        if isinstance(_cache_response, Unset):
            cache_response = UNSET
        else:
            cache_response = CacheResponseMetadata.from_dict(_cache_response)

        validation_uuid = d.pop("validationUuid", UNSET)

        _store_type = d.pop("storeType", UNSET)
        store_type: PMSPipelineResponseStoreType | Unset
        if isinstance(_store_type, Unset):
            store_type = UNSET
        else:
            store_type = check_pms_pipeline_response_store_type(_store_type)

        _public_access_response = d.pop("publicAccessResponse", UNSET)
        public_access_response: PublicAccessResponse | Unset
        if isinstance(_public_access_response, Unset):
            public_access_response = UNSET
        else:
            public_access_response = PublicAccessResponse.from_dict(_public_access_response)

        connector_ref = d.pop("connectorRef", UNSET)

        allow_dynamic_executions = d.pop("allowDynamicExecutions", UNSET)

        is_inline_hc_entity = d.pop("isInlineHCEntity", UNSET)

        pms_pipeline_response = cls(
            yaml_pipeline=yaml_pipeline,
            resolved_templates_pipeline_yaml=resolved_templates_pipeline_yaml,
            git_details=git_details,
            entity_validity_details=entity_validity_details,
            modules=modules,
            governance_metadata=governance_metadata,
            yaml_schema_error_wrapper=yaml_schema_error_wrapper,
            validate_template_inputs_response=validate_template_inputs_response,
            cache_response=cache_response,
            validation_uuid=validation_uuid,
            store_type=store_type,
            public_access_response=public_access_response,
            connector_ref=connector_ref,
            allow_dynamic_executions=allow_dynamic_executions,
            is_inline_hc_entity=is_inline_hc_entity,
        )

        pms_pipeline_response.additional_properties = d
        return pms_pipeline_response

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
