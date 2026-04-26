from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_response_store_type import TemplateResponseStoreType, check_template_response_store_type
from ..models.template_response_template_entity_type import (
    TemplateResponseTemplateEntityType,
    check_template_response_template_entity_type,
)
from ..models.template_response_template_scope import (
    TemplateResponseTemplateScope,
    check_template_response_template_scope,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cache_response_metadata import CacheResponseMetadata
    from ..models.entity_git_details import EntityGitDetails
    from ..models.template_response_tags import TemplateResponseTags


T = TypeVar("T", bound="TemplateResponse")


@_attrs_define
class TemplateResponse:
    """This contains details of the Template Response

    Attributes:
        account_id (str):
        identifier (str):
        name (str):
        yaml (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        description (str | Unset):
        tags (TemplateResponseTags | Unset):
        merged_yaml (str | Unset):
        version_label (str | Unset):
        is_stable_template (bool | Unset):
        enable_dag (bool | Unset):
        template_entity_type (TemplateResponseTemplateEntityType | Unset):
        child_type (str | Unset):
        template_scope (TemplateResponseTemplateScope | Unset):
        version (int | Unset):
        git_details (EntityGitDetails | Unset): This contains Validity Details of the Entity
        entity_validity_details (EntityGitDetails | Unset): This contains Validity Details of the Entity
        last_updated_at (int | Unset):
        store_type (TemplateResponseStoreType | Unset):
        connector_ref (str | Unset):
        icon (str | Unset):
        cache_response_metadata (CacheResponseMetadata | Unset): This tells the state of the cache from which the
            template was fetched.
        yaml_version (str | Unset):
        bulk_reconcile_uuid (str | Unset):
        has_insert (bool | Unset):
        is_inline_hc_entity (bool | Unset):
        stable_template (bool | Unset):
    """

    account_id: str
    identifier: str
    name: str
    yaml: str
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    description: str | Unset = UNSET
    tags: TemplateResponseTags | Unset = UNSET
    merged_yaml: str | Unset = UNSET
    version_label: str | Unset = UNSET
    is_stable_template: bool | Unset = UNSET
    enable_dag: bool | Unset = UNSET
    template_entity_type: TemplateResponseTemplateEntityType | Unset = UNSET
    child_type: str | Unset = UNSET
    template_scope: TemplateResponseTemplateScope | Unset = UNSET
    version: int | Unset = UNSET
    git_details: EntityGitDetails | Unset = UNSET
    entity_validity_details: EntityGitDetails | Unset = UNSET
    last_updated_at: int | Unset = UNSET
    store_type: TemplateResponseStoreType | Unset = UNSET
    connector_ref: str | Unset = UNSET
    icon: str | Unset = UNSET
    cache_response_metadata: CacheResponseMetadata | Unset = UNSET
    yaml_version: str | Unset = UNSET
    bulk_reconcile_uuid: str | Unset = UNSET
    has_insert: bool | Unset = UNSET
    is_inline_hc_entity: bool | Unset = UNSET
    stable_template: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        identifier = self.identifier

        name = self.name

        yaml = self.yaml

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        description = self.description

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        merged_yaml = self.merged_yaml

        version_label = self.version_label

        is_stable_template = self.is_stable_template

        enable_dag = self.enable_dag

        template_entity_type: str | Unset = UNSET
        if not isinstance(self.template_entity_type, Unset):
            template_entity_type = self.template_entity_type

        child_type = self.child_type

        template_scope: str | Unset = UNSET
        if not isinstance(self.template_scope, Unset):
            template_scope = self.template_scope

        version = self.version

        git_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.git_details, Unset):
            git_details = self.git_details.to_dict()

        entity_validity_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entity_validity_details, Unset):
            entity_validity_details = self.entity_validity_details.to_dict()

        last_updated_at = self.last_updated_at

        store_type: str | Unset = UNSET
        if not isinstance(self.store_type, Unset):
            store_type = self.store_type

        connector_ref = self.connector_ref

        icon = self.icon

        cache_response_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cache_response_metadata, Unset):
            cache_response_metadata = self.cache_response_metadata.to_dict()

        yaml_version = self.yaml_version

        bulk_reconcile_uuid = self.bulk_reconcile_uuid

        has_insert = self.has_insert

        is_inline_hc_entity = self.is_inline_hc_entity

        stable_template = self.stable_template

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "identifier": identifier,
                "name": name,
                "yaml": yaml,
            }
        )
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if merged_yaml is not UNSET:
            field_dict["mergedYaml"] = merged_yaml
        if version_label is not UNSET:
            field_dict["versionLabel"] = version_label
        if is_stable_template is not UNSET:
            field_dict["isStableTemplate"] = is_stable_template
        if enable_dag is not UNSET:
            field_dict["enableDAG"] = enable_dag
        if template_entity_type is not UNSET:
            field_dict["templateEntityType"] = template_entity_type
        if child_type is not UNSET:
            field_dict["childType"] = child_type
        if template_scope is not UNSET:
            field_dict["templateScope"] = template_scope
        if version is not UNSET:
            field_dict["version"] = version
        if git_details is not UNSET:
            field_dict["gitDetails"] = git_details
        if entity_validity_details is not UNSET:
            field_dict["entityValidityDetails"] = entity_validity_details
        if last_updated_at is not UNSET:
            field_dict["lastUpdatedAt"] = last_updated_at
        if store_type is not UNSET:
            field_dict["storeType"] = store_type
        if connector_ref is not UNSET:
            field_dict["connectorRef"] = connector_ref
        if icon is not UNSET:
            field_dict["icon"] = icon
        if cache_response_metadata is not UNSET:
            field_dict["cacheResponseMetadata"] = cache_response_metadata
        if yaml_version is not UNSET:
            field_dict["yamlVersion"] = yaml_version
        if bulk_reconcile_uuid is not UNSET:
            field_dict["bulkReconcileUUID"] = bulk_reconcile_uuid
        if has_insert is not UNSET:
            field_dict["hasInsert"] = has_insert
        if is_inline_hc_entity is not UNSET:
            field_dict["isInlineHCEntity"] = is_inline_hc_entity
        if stable_template is not UNSET:
            field_dict["stableTemplate"] = stable_template

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cache_response_metadata import CacheResponseMetadata
        from ..models.entity_git_details import EntityGitDetails
        from ..models.template_response_tags import TemplateResponseTags

        d = dict(src_dict)
        account_id = d.pop("accountId")

        identifier = d.pop("identifier")

        name = d.pop("name")

        yaml = d.pop("yaml")

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        description = d.pop("description", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: TemplateResponseTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = TemplateResponseTags.from_dict(_tags)

        merged_yaml = d.pop("mergedYaml", UNSET)

        version_label = d.pop("versionLabel", UNSET)

        is_stable_template = d.pop("isStableTemplate", UNSET)

        enable_dag = d.pop("enableDAG", UNSET)

        _template_entity_type = d.pop("templateEntityType", UNSET)
        template_entity_type: TemplateResponseTemplateEntityType | Unset
        if isinstance(_template_entity_type, Unset):
            template_entity_type = UNSET
        else:
            template_entity_type = check_template_response_template_entity_type(_template_entity_type)

        child_type = d.pop("childType", UNSET)

        _template_scope = d.pop("templateScope", UNSET)
        template_scope: TemplateResponseTemplateScope | Unset
        if isinstance(_template_scope, Unset):
            template_scope = UNSET
        else:
            template_scope = check_template_response_template_scope(_template_scope)

        version = d.pop("version", UNSET)

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

        last_updated_at = d.pop("lastUpdatedAt", UNSET)

        _store_type = d.pop("storeType", UNSET)
        store_type: TemplateResponseStoreType | Unset
        if isinstance(_store_type, Unset):
            store_type = UNSET
        else:
            store_type = check_template_response_store_type(_store_type)

        connector_ref = d.pop("connectorRef", UNSET)

        icon = d.pop("icon", UNSET)

        _cache_response_metadata = d.pop("cacheResponseMetadata", UNSET)
        cache_response_metadata: CacheResponseMetadata | Unset
        if isinstance(_cache_response_metadata, Unset):
            cache_response_metadata = UNSET
        else:
            cache_response_metadata = CacheResponseMetadata.from_dict(_cache_response_metadata)

        yaml_version = d.pop("yamlVersion", UNSET)

        bulk_reconcile_uuid = d.pop("bulkReconcileUUID", UNSET)

        has_insert = d.pop("hasInsert", UNSET)

        is_inline_hc_entity = d.pop("isInlineHCEntity", UNSET)

        stable_template = d.pop("stableTemplate", UNSET)

        template_response = cls(
            account_id=account_id,
            identifier=identifier,
            name=name,
            yaml=yaml,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            description=description,
            tags=tags,
            merged_yaml=merged_yaml,
            version_label=version_label,
            is_stable_template=is_stable_template,
            enable_dag=enable_dag,
            template_entity_type=template_entity_type,
            child_type=child_type,
            template_scope=template_scope,
            version=version,
            git_details=git_details,
            entity_validity_details=entity_validity_details,
            last_updated_at=last_updated_at,
            store_type=store_type,
            connector_ref=connector_ref,
            icon=icon,
            cache_response_metadata=cache_response_metadata,
            yaml_version=yaml_version,
            bulk_reconcile_uuid=bulk_reconcile_uuid,
            has_insert=has_insert,
            is_inline_hc_entity=is_inline_hc_entity,
            stable_template=stable_template,
        )

        template_response.additional_properties = d
        return template_response

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
