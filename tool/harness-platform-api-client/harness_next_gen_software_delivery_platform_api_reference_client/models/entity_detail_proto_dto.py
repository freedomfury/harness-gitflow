from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.entity_detail_proto_dto_entity_ref_case import (
    EntityDetailProtoDTOEntityRefCase,
    check_entity_detail_proto_dto_entity_ref_case,
)
from ..models.entity_detail_proto_dto_type import EntityDetailProtoDTOType, check_entity_detail_proto_dto_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.entity_detail_proto_dto_all_fields import EntityDetailProtoDTOAllFields
    from ..models.entity_git_metadata import EntityGitMetadata
    from ..models.entity_git_metadata_or_builder import EntityGitMetadataOrBuilder
    from ..models.identifier_ref_proto_dto import IdentifierRefProtoDTO
    from ..models.identifier_ref_proto_dto_or_builder import IdentifierRefProtoDTOOrBuilder
    from ..models.infra_definition_reference_proto_dto import InfraDefinitionReferenceProtoDTO
    from ..models.infra_definition_reference_proto_dto_or_builder import InfraDefinitionReferenceProtoDTOOrBuilder
    from ..models.input_set_reference_proto_dto import InputSetReferenceProtoDTO
    from ..models.input_set_reference_proto_dto_or_builder import InputSetReferenceProtoDTOOrBuilder
    from ..models.parser_entity_detail_proto_dto import ParserEntityDetailProtoDTO
    from ..models.template_reference_proto_dto import TemplateReferenceProtoDTO
    from ..models.template_reference_proto_dto_or_builder import TemplateReferenceProtoDTOOrBuilder
    from ..models.trigger_reference_proto_dto import TriggerReferenceProtoDTO
    from ..models.trigger_reference_proto_dto_or_builder import TriggerReferenceProtoDTOOrBuilder
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="EntityDetailProtoDTO")


@_attrs_define
class EntityDetailProtoDTO:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        identifier_ref (IdentifierRefProtoDTO | Unset):
        entity_git_metadata (EntityGitMetadata | Unset):
        name (str | Unset):
        type_ (EntityDetailProtoDTOType | Unset):
        identifier_ref_or_builder (IdentifierRefProtoDTOOrBuilder | Unset):
        input_set_ref_or_builder (InputSetReferenceProtoDTOOrBuilder | Unset):
        template_ref_or_builder (TemplateReferenceProtoDTOOrBuilder | Unset):
        type_value (int | Unset):
        infra_def_ref_or_builder (InfraDefinitionReferenceProtoDTOOrBuilder | Unset):
        trigger_ref_or_builder (TriggerReferenceProtoDTOOrBuilder | Unset):
        entity_git_metadata_or_builder (EntityGitMetadataOrBuilder | Unset):
        entity_ref_case (EntityDetailProtoDTOEntityRefCase | Unset):
        infra_def_ref (InfraDefinitionReferenceProtoDTO | Unset):
        trigger_ref (TriggerReferenceProtoDTO | Unset):
        input_set_ref (InputSetReferenceProtoDTO | Unset):
        parser_for_type (ParserEntityDetailProtoDTO | Unset):
        serialized_size (int | Unset):
        name_bytes (ByteString | Unset):
        template_ref (TemplateReferenceProtoDTO | Unset):
        default_instance_for_type (EntityDetailProtoDTO | Unset):
        initialized (bool | Unset):
        initialization_error_string (str | Unset):
        all_fields (EntityDetailProtoDTOAllFields | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    identifier_ref: IdentifierRefProtoDTO | Unset = UNSET
    entity_git_metadata: EntityGitMetadata | Unset = UNSET
    name: str | Unset = UNSET
    type_: EntityDetailProtoDTOType | Unset = UNSET
    identifier_ref_or_builder: IdentifierRefProtoDTOOrBuilder | Unset = UNSET
    input_set_ref_or_builder: InputSetReferenceProtoDTOOrBuilder | Unset = UNSET
    template_ref_or_builder: TemplateReferenceProtoDTOOrBuilder | Unset = UNSET
    type_value: int | Unset = UNSET
    infra_def_ref_or_builder: InfraDefinitionReferenceProtoDTOOrBuilder | Unset = UNSET
    trigger_ref_or_builder: TriggerReferenceProtoDTOOrBuilder | Unset = UNSET
    entity_git_metadata_or_builder: EntityGitMetadataOrBuilder | Unset = UNSET
    entity_ref_case: EntityDetailProtoDTOEntityRefCase | Unset = UNSET
    infra_def_ref: InfraDefinitionReferenceProtoDTO | Unset = UNSET
    trigger_ref: TriggerReferenceProtoDTO | Unset = UNSET
    input_set_ref: InputSetReferenceProtoDTO | Unset = UNSET
    parser_for_type: ParserEntityDetailProtoDTO | Unset = UNSET
    serialized_size: int | Unset = UNSET
    name_bytes: ByteString | Unset = UNSET
    template_ref: TemplateReferenceProtoDTO | Unset = UNSET
    default_instance_for_type: EntityDetailProtoDTO | Unset = UNSET
    initialized: bool | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    all_fields: EntityDetailProtoDTOAllFields | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        identifier_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifier_ref, Unset):
            identifier_ref = self.identifier_ref.to_dict()

        entity_git_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entity_git_metadata, Unset):
            entity_git_metadata = self.entity_git_metadata.to_dict()

        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        identifier_ref_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifier_ref_or_builder, Unset):
            identifier_ref_or_builder = self.identifier_ref_or_builder.to_dict()

        input_set_ref_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_set_ref_or_builder, Unset):
            input_set_ref_or_builder = self.input_set_ref_or_builder.to_dict()

        template_ref_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template_ref_or_builder, Unset):
            template_ref_or_builder = self.template_ref_or_builder.to_dict()

        type_value = self.type_value

        infra_def_ref_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.infra_def_ref_or_builder, Unset):
            infra_def_ref_or_builder = self.infra_def_ref_or_builder.to_dict()

        trigger_ref_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trigger_ref_or_builder, Unset):
            trigger_ref_or_builder = self.trigger_ref_or_builder.to_dict()

        entity_git_metadata_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entity_git_metadata_or_builder, Unset):
            entity_git_metadata_or_builder = self.entity_git_metadata_or_builder.to_dict()

        entity_ref_case: str | Unset = UNSET
        if not isinstance(self.entity_ref_case, Unset):
            entity_ref_case = self.entity_ref_case

        infra_def_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.infra_def_ref, Unset):
            infra_def_ref = self.infra_def_ref.to_dict()

        trigger_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trigger_ref, Unset):
            trigger_ref = self.trigger_ref.to_dict()

        input_set_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_set_ref, Unset):
            input_set_ref = self.input_set_ref.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        name_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.name_bytes, Unset):
            name_bytes = self.name_bytes.to_dict()

        template_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template_ref, Unset):
            template_ref = self.template_ref.to_dict()

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        initialized = self.initialized

        initialization_error_string = self.initialization_error_string

        all_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_fields, Unset):
            all_fields = self.all_fields.to_dict()

        descriptor_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.descriptor_for_type, Unset):
            descriptor_for_type = self.descriptor_for_type.to_dict()

        memoized_serialized_size = self.memoized_serialized_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unknown_fields is not UNSET:
            field_dict["unknownFields"] = unknown_fields
        if identifier_ref is not UNSET:
            field_dict["identifierRef"] = identifier_ref
        if entity_git_metadata is not UNSET:
            field_dict["entityGitMetadata"] = entity_git_metadata
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if identifier_ref_or_builder is not UNSET:
            field_dict["identifierRefOrBuilder"] = identifier_ref_or_builder
        if input_set_ref_or_builder is not UNSET:
            field_dict["inputSetRefOrBuilder"] = input_set_ref_or_builder
        if template_ref_or_builder is not UNSET:
            field_dict["templateRefOrBuilder"] = template_ref_or_builder
        if type_value is not UNSET:
            field_dict["typeValue"] = type_value
        if infra_def_ref_or_builder is not UNSET:
            field_dict["infraDefRefOrBuilder"] = infra_def_ref_or_builder
        if trigger_ref_or_builder is not UNSET:
            field_dict["triggerRefOrBuilder"] = trigger_ref_or_builder
        if entity_git_metadata_or_builder is not UNSET:
            field_dict["entityGitMetadataOrBuilder"] = entity_git_metadata_or_builder
        if entity_ref_case is not UNSET:
            field_dict["entityRefCase"] = entity_ref_case
        if infra_def_ref is not UNSET:
            field_dict["infraDefRef"] = infra_def_ref
        if trigger_ref is not UNSET:
            field_dict["triggerRef"] = trigger_ref
        if input_set_ref is not UNSET:
            field_dict["inputSetRef"] = input_set_ref
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if name_bytes is not UNSET:
            field_dict["nameBytes"] = name_bytes
        if template_ref is not UNSET:
            field_dict["templateRef"] = template_ref
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if initialization_error_string is not UNSET:
            field_dict["initializationErrorString"] = initialization_error_string
        if all_fields is not UNSET:
            field_dict["allFields"] = all_fields
        if descriptor_for_type is not UNSET:
            field_dict["descriptorForType"] = descriptor_for_type
        if memoized_serialized_size is not UNSET:
            field_dict["memoizedSerializedSize"] = memoized_serialized_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.byte_string import ByteString
        from ..models.descriptor import Descriptor
        from ..models.entity_detail_proto_dto_all_fields import EntityDetailProtoDTOAllFields
        from ..models.entity_git_metadata import EntityGitMetadata
        from ..models.entity_git_metadata_or_builder import EntityGitMetadataOrBuilder
        from ..models.identifier_ref_proto_dto import IdentifierRefProtoDTO
        from ..models.identifier_ref_proto_dto_or_builder import IdentifierRefProtoDTOOrBuilder
        from ..models.infra_definition_reference_proto_dto import InfraDefinitionReferenceProtoDTO
        from ..models.infra_definition_reference_proto_dto_or_builder import InfraDefinitionReferenceProtoDTOOrBuilder
        from ..models.input_set_reference_proto_dto import InputSetReferenceProtoDTO
        from ..models.input_set_reference_proto_dto_or_builder import InputSetReferenceProtoDTOOrBuilder
        from ..models.parser_entity_detail_proto_dto import ParserEntityDetailProtoDTO
        from ..models.template_reference_proto_dto import TemplateReferenceProtoDTO
        from ..models.template_reference_proto_dto_or_builder import TemplateReferenceProtoDTOOrBuilder
        from ..models.trigger_reference_proto_dto import TriggerReferenceProtoDTO
        from ..models.trigger_reference_proto_dto_or_builder import TriggerReferenceProtoDTOOrBuilder
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        _identifier_ref = d.pop("identifierRef", UNSET)
        identifier_ref: IdentifierRefProtoDTO | Unset
        if isinstance(_identifier_ref, Unset):
            identifier_ref = UNSET
        else:
            identifier_ref = IdentifierRefProtoDTO.from_dict(_identifier_ref)

        _entity_git_metadata = d.pop("entityGitMetadata", UNSET)
        entity_git_metadata: EntityGitMetadata | Unset
        if isinstance(_entity_git_metadata, Unset):
            entity_git_metadata = UNSET
        else:
            entity_git_metadata = EntityGitMetadata.from_dict(_entity_git_metadata)

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: EntityDetailProtoDTOType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_entity_detail_proto_dto_type(_type_)

        _identifier_ref_or_builder = d.pop("identifierRefOrBuilder", UNSET)
        identifier_ref_or_builder: IdentifierRefProtoDTOOrBuilder | Unset
        if isinstance(_identifier_ref_or_builder, Unset):
            identifier_ref_or_builder = UNSET
        else:
            identifier_ref_or_builder = IdentifierRefProtoDTOOrBuilder.from_dict(_identifier_ref_or_builder)

        _input_set_ref_or_builder = d.pop("inputSetRefOrBuilder", UNSET)
        input_set_ref_or_builder: InputSetReferenceProtoDTOOrBuilder | Unset
        if isinstance(_input_set_ref_or_builder, Unset):
            input_set_ref_or_builder = UNSET
        else:
            input_set_ref_or_builder = InputSetReferenceProtoDTOOrBuilder.from_dict(_input_set_ref_or_builder)

        _template_ref_or_builder = d.pop("templateRefOrBuilder", UNSET)
        template_ref_or_builder: TemplateReferenceProtoDTOOrBuilder | Unset
        if isinstance(_template_ref_or_builder, Unset):
            template_ref_or_builder = UNSET
        else:
            template_ref_or_builder = TemplateReferenceProtoDTOOrBuilder.from_dict(_template_ref_or_builder)

        type_value = d.pop("typeValue", UNSET)

        _infra_def_ref_or_builder = d.pop("infraDefRefOrBuilder", UNSET)
        infra_def_ref_or_builder: InfraDefinitionReferenceProtoDTOOrBuilder | Unset
        if isinstance(_infra_def_ref_or_builder, Unset):
            infra_def_ref_or_builder = UNSET
        else:
            infra_def_ref_or_builder = InfraDefinitionReferenceProtoDTOOrBuilder.from_dict(_infra_def_ref_or_builder)

        _trigger_ref_or_builder = d.pop("triggerRefOrBuilder", UNSET)
        trigger_ref_or_builder: TriggerReferenceProtoDTOOrBuilder | Unset
        if isinstance(_trigger_ref_or_builder, Unset):
            trigger_ref_or_builder = UNSET
        else:
            trigger_ref_or_builder = TriggerReferenceProtoDTOOrBuilder.from_dict(_trigger_ref_or_builder)

        _entity_git_metadata_or_builder = d.pop("entityGitMetadataOrBuilder", UNSET)
        entity_git_metadata_or_builder: EntityGitMetadataOrBuilder | Unset
        if isinstance(_entity_git_metadata_or_builder, Unset):
            entity_git_metadata_or_builder = UNSET
        else:
            entity_git_metadata_or_builder = EntityGitMetadataOrBuilder.from_dict(_entity_git_metadata_or_builder)

        _entity_ref_case = d.pop("entityRefCase", UNSET)
        entity_ref_case: EntityDetailProtoDTOEntityRefCase | Unset
        if isinstance(_entity_ref_case, Unset):
            entity_ref_case = UNSET
        else:
            entity_ref_case = check_entity_detail_proto_dto_entity_ref_case(_entity_ref_case)

        _infra_def_ref = d.pop("infraDefRef", UNSET)
        infra_def_ref: InfraDefinitionReferenceProtoDTO | Unset
        if isinstance(_infra_def_ref, Unset):
            infra_def_ref = UNSET
        else:
            infra_def_ref = InfraDefinitionReferenceProtoDTO.from_dict(_infra_def_ref)

        _trigger_ref = d.pop("triggerRef", UNSET)
        trigger_ref: TriggerReferenceProtoDTO | Unset
        if isinstance(_trigger_ref, Unset):
            trigger_ref = UNSET
        else:
            trigger_ref = TriggerReferenceProtoDTO.from_dict(_trigger_ref)

        _input_set_ref = d.pop("inputSetRef", UNSET)
        input_set_ref: InputSetReferenceProtoDTO | Unset
        if isinstance(_input_set_ref, Unset):
            input_set_ref = UNSET
        else:
            input_set_ref = InputSetReferenceProtoDTO.from_dict(_input_set_ref)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserEntityDetailProtoDTO | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserEntityDetailProtoDTO.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _name_bytes = d.pop("nameBytes", UNSET)
        name_bytes: ByteString | Unset
        if isinstance(_name_bytes, Unset):
            name_bytes = UNSET
        else:
            name_bytes = ByteString.from_dict(_name_bytes)

        _template_ref = d.pop("templateRef", UNSET)
        template_ref: TemplateReferenceProtoDTO | Unset
        if isinstance(_template_ref, Unset):
            template_ref = UNSET
        else:
            template_ref = TemplateReferenceProtoDTO.from_dict(_template_ref)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: EntityDetailProtoDTO | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = EntityDetailProtoDTO.from_dict(_default_instance_for_type)

        initialized = d.pop("initialized", UNSET)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: EntityDetailProtoDTOAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = EntityDetailProtoDTOAllFields.from_dict(_all_fields)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        entity_detail_proto_dto = cls(
            unknown_fields=unknown_fields,
            identifier_ref=identifier_ref,
            entity_git_metadata=entity_git_metadata,
            name=name,
            type_=type_,
            identifier_ref_or_builder=identifier_ref_or_builder,
            input_set_ref_or_builder=input_set_ref_or_builder,
            template_ref_or_builder=template_ref_or_builder,
            type_value=type_value,
            infra_def_ref_or_builder=infra_def_ref_or_builder,
            trigger_ref_or_builder=trigger_ref_or_builder,
            entity_git_metadata_or_builder=entity_git_metadata_or_builder,
            entity_ref_case=entity_ref_case,
            infra_def_ref=infra_def_ref,
            trigger_ref=trigger_ref,
            input_set_ref=input_set_ref,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            name_bytes=name_bytes,
            template_ref=template_ref,
            default_instance_for_type=default_instance_for_type,
            initialized=initialized,
            initialization_error_string=initialization_error_string,
            all_fields=all_fields,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        entity_detail_proto_dto.additional_properties = d
        return entity_detail_proto_dto

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
