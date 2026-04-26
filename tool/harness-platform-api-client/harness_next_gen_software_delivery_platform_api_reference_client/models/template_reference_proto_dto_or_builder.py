from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_reference_proto_dto_or_builder_scope import (
    TemplateReferenceProtoDTOOrBuilderScope,
    check_template_reference_proto_dto_or_builder_scope,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.descriptor import Descriptor
    from ..models.message import Message
    from ..models.string_value import StringValue
    from ..models.string_value_or_builder import StringValueOrBuilder
    from ..models.template_reference_proto_dto_or_builder_all_fields import TemplateReferenceProtoDTOOrBuilderAllFields
    from ..models.template_reference_proto_dto_or_builder_metadata import TemplateReferenceProtoDTOOrBuilderMetadata
    from ..models.template_reference_proto_dto_or_builder_metadata_map import (
        TemplateReferenceProtoDTOOrBuilderMetadataMap,
    )
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="TemplateReferenceProtoDTOOrBuilder")


@_attrs_define
class TemplateReferenceProtoDTOOrBuilder:
    """
    Attributes:
        account_identifier (StringValue | Unset):
        org_identifier (StringValue | Unset):
        project_identifier (StringValue | Unset):
        parent_unique_id (StringValue | Unset):
        metadata_count (int | Unset):
        metadata (TemplateReferenceProtoDTOOrBuilderMetadata | Unset):
        identifier_or_builder (StringValueOrBuilder | Unset):
        account_identifier_or_builder (StringValueOrBuilder | Unset):
        version_label_or_builder (StringValueOrBuilder | Unset):
        parent_unique_id_or_builder (StringValueOrBuilder | Unset):
        org_identifier_or_builder (StringValueOrBuilder | Unset):
        project_identifier_or_builder (StringValueOrBuilder | Unset):
        scope_value (int | Unset):
        version_label (StringValue | Unset):
        metadata_map (TemplateReferenceProtoDTOOrBuilderMetadataMap | Unset):
        identifier (StringValue | Unset):
        scope (TemplateReferenceProtoDTOOrBuilderScope | Unset):
        initialization_error_string (str | Unset):
        all_fields (TemplateReferenceProtoDTOOrBuilderAllFields | Unset):
        unknown_fields (UnknownFieldSet | Unset):
        descriptor_for_type (Descriptor | Unset):
        default_instance_for_type (Message | Unset):
        initialized (bool | Unset):
    """

    account_identifier: StringValue | Unset = UNSET
    org_identifier: StringValue | Unset = UNSET
    project_identifier: StringValue | Unset = UNSET
    parent_unique_id: StringValue | Unset = UNSET
    metadata_count: int | Unset = UNSET
    metadata: TemplateReferenceProtoDTOOrBuilderMetadata | Unset = UNSET
    identifier_or_builder: StringValueOrBuilder | Unset = UNSET
    account_identifier_or_builder: StringValueOrBuilder | Unset = UNSET
    version_label_or_builder: StringValueOrBuilder | Unset = UNSET
    parent_unique_id_or_builder: StringValueOrBuilder | Unset = UNSET
    org_identifier_or_builder: StringValueOrBuilder | Unset = UNSET
    project_identifier_or_builder: StringValueOrBuilder | Unset = UNSET
    scope_value: int | Unset = UNSET
    version_label: StringValue | Unset = UNSET
    metadata_map: TemplateReferenceProtoDTOOrBuilderMetadataMap | Unset = UNSET
    identifier: StringValue | Unset = UNSET
    scope: TemplateReferenceProtoDTOOrBuilderScope | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    all_fields: TemplateReferenceProtoDTOOrBuilderAllFields | Unset = UNSET
    unknown_fields: UnknownFieldSet | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    default_instance_for_type: Message | Unset = UNSET
    initialized: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_identifier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account_identifier, Unset):
            account_identifier = self.account_identifier.to_dict()

        org_identifier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.org_identifier, Unset):
            org_identifier = self.org_identifier.to_dict()

        project_identifier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_identifier, Unset):
            project_identifier = self.project_identifier.to_dict()

        parent_unique_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent_unique_id, Unset):
            parent_unique_id = self.parent_unique_id.to_dict()

        metadata_count = self.metadata_count

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        identifier_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifier_or_builder, Unset):
            identifier_or_builder = self.identifier_or_builder.to_dict()

        account_identifier_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account_identifier_or_builder, Unset):
            account_identifier_or_builder = self.account_identifier_or_builder.to_dict()

        version_label_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.version_label_or_builder, Unset):
            version_label_or_builder = self.version_label_or_builder.to_dict()

        parent_unique_id_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent_unique_id_or_builder, Unset):
            parent_unique_id_or_builder = self.parent_unique_id_or_builder.to_dict()

        org_identifier_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.org_identifier_or_builder, Unset):
            org_identifier_or_builder = self.org_identifier_or_builder.to_dict()

        project_identifier_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_identifier_or_builder, Unset):
            project_identifier_or_builder = self.project_identifier_or_builder.to_dict()

        scope_value = self.scope_value

        version_label: dict[str, Any] | Unset = UNSET
        if not isinstance(self.version_label, Unset):
            version_label = self.version_label.to_dict()

        metadata_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata_map, Unset):
            metadata_map = self.metadata_map.to_dict()

        identifier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = self.identifier.to_dict()

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope

        initialization_error_string = self.initialization_error_string

        all_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_fields, Unset):
            all_fields = self.all_fields.to_dict()

        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        descriptor_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.descriptor_for_type, Unset):
            descriptor_for_type = self.descriptor_for_type.to_dict()

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        initialized = self.initialized

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_identifier is not UNSET:
            field_dict["accountIdentifier"] = account_identifier
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if parent_unique_id is not UNSET:
            field_dict["parentUniqueId"] = parent_unique_id
        if metadata_count is not UNSET:
            field_dict["metadataCount"] = metadata_count
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if identifier_or_builder is not UNSET:
            field_dict["identifierOrBuilder"] = identifier_or_builder
        if account_identifier_or_builder is not UNSET:
            field_dict["accountIdentifierOrBuilder"] = account_identifier_or_builder
        if version_label_or_builder is not UNSET:
            field_dict["versionLabelOrBuilder"] = version_label_or_builder
        if parent_unique_id_or_builder is not UNSET:
            field_dict["parentUniqueIdOrBuilder"] = parent_unique_id_or_builder
        if org_identifier_or_builder is not UNSET:
            field_dict["orgIdentifierOrBuilder"] = org_identifier_or_builder
        if project_identifier_or_builder is not UNSET:
            field_dict["projectIdentifierOrBuilder"] = project_identifier_or_builder
        if scope_value is not UNSET:
            field_dict["scopeValue"] = scope_value
        if version_label is not UNSET:
            field_dict["versionLabel"] = version_label
        if metadata_map is not UNSET:
            field_dict["metadataMap"] = metadata_map
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if scope is not UNSET:
            field_dict["scope"] = scope
        if initialization_error_string is not UNSET:
            field_dict["initializationErrorString"] = initialization_error_string
        if all_fields is not UNSET:
            field_dict["allFields"] = all_fields
        if unknown_fields is not UNSET:
            field_dict["unknownFields"] = unknown_fields
        if descriptor_for_type is not UNSET:
            field_dict["descriptorForType"] = descriptor_for_type
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if initialized is not UNSET:
            field_dict["initialized"] = initialized

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.descriptor import Descriptor
        from ..models.message import Message
        from ..models.string_value import StringValue
        from ..models.string_value_or_builder import StringValueOrBuilder
        from ..models.template_reference_proto_dto_or_builder_all_fields import (
            TemplateReferenceProtoDTOOrBuilderAllFields,
        )
        from ..models.template_reference_proto_dto_or_builder_metadata import TemplateReferenceProtoDTOOrBuilderMetadata
        from ..models.template_reference_proto_dto_or_builder_metadata_map import (
            TemplateReferenceProtoDTOOrBuilderMetadataMap,
        )
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _account_identifier = d.pop("accountIdentifier", UNSET)
        account_identifier: StringValue | Unset
        if isinstance(_account_identifier, Unset):
            account_identifier = UNSET
        else:
            account_identifier = StringValue.from_dict(_account_identifier)

        _org_identifier = d.pop("orgIdentifier", UNSET)
        org_identifier: StringValue | Unset
        if isinstance(_org_identifier, Unset):
            org_identifier = UNSET
        else:
            org_identifier = StringValue.from_dict(_org_identifier)

        _project_identifier = d.pop("projectIdentifier", UNSET)
        project_identifier: StringValue | Unset
        if isinstance(_project_identifier, Unset):
            project_identifier = UNSET
        else:
            project_identifier = StringValue.from_dict(_project_identifier)

        _parent_unique_id = d.pop("parentUniqueId", UNSET)
        parent_unique_id: StringValue | Unset
        if isinstance(_parent_unique_id, Unset):
            parent_unique_id = UNSET
        else:
            parent_unique_id = StringValue.from_dict(_parent_unique_id)

        metadata_count = d.pop("metadataCount", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: TemplateReferenceProtoDTOOrBuilderMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = TemplateReferenceProtoDTOOrBuilderMetadata.from_dict(_metadata)

        _identifier_or_builder = d.pop("identifierOrBuilder", UNSET)
        identifier_or_builder: StringValueOrBuilder | Unset
        if isinstance(_identifier_or_builder, Unset):
            identifier_or_builder = UNSET
        else:
            identifier_or_builder = StringValueOrBuilder.from_dict(_identifier_or_builder)

        _account_identifier_or_builder = d.pop("accountIdentifierOrBuilder", UNSET)
        account_identifier_or_builder: StringValueOrBuilder | Unset
        if isinstance(_account_identifier_or_builder, Unset):
            account_identifier_or_builder = UNSET
        else:
            account_identifier_or_builder = StringValueOrBuilder.from_dict(_account_identifier_or_builder)

        _version_label_or_builder = d.pop("versionLabelOrBuilder", UNSET)
        version_label_or_builder: StringValueOrBuilder | Unset
        if isinstance(_version_label_or_builder, Unset):
            version_label_or_builder = UNSET
        else:
            version_label_or_builder = StringValueOrBuilder.from_dict(_version_label_or_builder)

        _parent_unique_id_or_builder = d.pop("parentUniqueIdOrBuilder", UNSET)
        parent_unique_id_or_builder: StringValueOrBuilder | Unset
        if isinstance(_parent_unique_id_or_builder, Unset):
            parent_unique_id_or_builder = UNSET
        else:
            parent_unique_id_or_builder = StringValueOrBuilder.from_dict(_parent_unique_id_or_builder)

        _org_identifier_or_builder = d.pop("orgIdentifierOrBuilder", UNSET)
        org_identifier_or_builder: StringValueOrBuilder | Unset
        if isinstance(_org_identifier_or_builder, Unset):
            org_identifier_or_builder = UNSET
        else:
            org_identifier_or_builder = StringValueOrBuilder.from_dict(_org_identifier_or_builder)

        _project_identifier_or_builder = d.pop("projectIdentifierOrBuilder", UNSET)
        project_identifier_or_builder: StringValueOrBuilder | Unset
        if isinstance(_project_identifier_or_builder, Unset):
            project_identifier_or_builder = UNSET
        else:
            project_identifier_or_builder = StringValueOrBuilder.from_dict(_project_identifier_or_builder)

        scope_value = d.pop("scopeValue", UNSET)

        _version_label = d.pop("versionLabel", UNSET)
        version_label: StringValue | Unset
        if isinstance(_version_label, Unset):
            version_label = UNSET
        else:
            version_label = StringValue.from_dict(_version_label)

        _metadata_map = d.pop("metadataMap", UNSET)
        metadata_map: TemplateReferenceProtoDTOOrBuilderMetadataMap | Unset
        if isinstance(_metadata_map, Unset):
            metadata_map = UNSET
        else:
            metadata_map = TemplateReferenceProtoDTOOrBuilderMetadataMap.from_dict(_metadata_map)

        _identifier = d.pop("identifier", UNSET)
        identifier: StringValue | Unset
        if isinstance(_identifier, Unset):
            identifier = UNSET
        else:
            identifier = StringValue.from_dict(_identifier)

        _scope = d.pop("scope", UNSET)
        scope: TemplateReferenceProtoDTOOrBuilderScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = check_template_reference_proto_dto_or_builder_scope(_scope)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: TemplateReferenceProtoDTOOrBuilderAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = TemplateReferenceProtoDTOOrBuilderAllFields.from_dict(_all_fields)

        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: Message | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = Message.from_dict(_default_instance_for_type)

        initialized = d.pop("initialized", UNSET)

        template_reference_proto_dto_or_builder = cls(
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            parent_unique_id=parent_unique_id,
            metadata_count=metadata_count,
            metadata=metadata,
            identifier_or_builder=identifier_or_builder,
            account_identifier_or_builder=account_identifier_or_builder,
            version_label_or_builder=version_label_or_builder,
            parent_unique_id_or_builder=parent_unique_id_or_builder,
            org_identifier_or_builder=org_identifier_or_builder,
            project_identifier_or_builder=project_identifier_or_builder,
            scope_value=scope_value,
            version_label=version_label,
            metadata_map=metadata_map,
            identifier=identifier,
            scope=scope,
            initialization_error_string=initialization_error_string,
            all_fields=all_fields,
            unknown_fields=unknown_fields,
            descriptor_for_type=descriptor_for_type,
            default_instance_for_type=default_instance_for_type,
            initialized=initialized,
        )

        template_reference_proto_dto_or_builder.additional_properties = d
        return template_reference_proto_dto_or_builder

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
