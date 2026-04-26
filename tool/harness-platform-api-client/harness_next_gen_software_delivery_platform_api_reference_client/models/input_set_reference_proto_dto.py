from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.descriptor import Descriptor
    from ..models.input_set_reference_proto_dto_all_fields import InputSetReferenceProtoDTOAllFields
    from ..models.parser_input_set_reference_proto_dto import ParserInputSetReferenceProtoDTO
    from ..models.string_value import StringValue
    from ..models.string_value_or_builder import StringValueOrBuilder
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="InputSetReferenceProtoDTO")


@_attrs_define
class InputSetReferenceProtoDTO:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        account_identifier (StringValue | Unset):
        org_identifier (StringValue | Unset):
        project_identifier (StringValue | Unset):
        parent_unique_id (StringValue | Unset):
        identifier_or_builder (StringValueOrBuilder | Unset):
        account_identifier_or_builder (StringValueOrBuilder | Unset):
        parent_unique_id_or_builder (StringValueOrBuilder | Unset):
        org_identifier_or_builder (StringValueOrBuilder | Unset):
        project_identifier_or_builder (StringValueOrBuilder | Unset):
        pipeline_identifier_or_builder (StringValueOrBuilder | Unset):
        parser_for_type (ParserInputSetReferenceProtoDTO | Unset):
        serialized_size (int | Unset):
        default_instance_for_type (InputSetReferenceProtoDTO | Unset):
        pipeline_identifier (StringValue | Unset):
        initialized (bool | Unset):
        identifier (StringValue | Unset):
        initialization_error_string (str | Unset):
        all_fields (InputSetReferenceProtoDTOAllFields | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    account_identifier: StringValue | Unset = UNSET
    org_identifier: StringValue | Unset = UNSET
    project_identifier: StringValue | Unset = UNSET
    parent_unique_id: StringValue | Unset = UNSET
    identifier_or_builder: StringValueOrBuilder | Unset = UNSET
    account_identifier_or_builder: StringValueOrBuilder | Unset = UNSET
    parent_unique_id_or_builder: StringValueOrBuilder | Unset = UNSET
    org_identifier_or_builder: StringValueOrBuilder | Unset = UNSET
    project_identifier_or_builder: StringValueOrBuilder | Unset = UNSET
    pipeline_identifier_or_builder: StringValueOrBuilder | Unset = UNSET
    parser_for_type: ParserInputSetReferenceProtoDTO | Unset = UNSET
    serialized_size: int | Unset = UNSET
    default_instance_for_type: InputSetReferenceProtoDTO | Unset = UNSET
    pipeline_identifier: StringValue | Unset = UNSET
    initialized: bool | Unset = UNSET
    identifier: StringValue | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    all_fields: InputSetReferenceProtoDTOAllFields | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

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

        identifier_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifier_or_builder, Unset):
            identifier_or_builder = self.identifier_or_builder.to_dict()

        account_identifier_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account_identifier_or_builder, Unset):
            account_identifier_or_builder = self.account_identifier_or_builder.to_dict()

        parent_unique_id_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent_unique_id_or_builder, Unset):
            parent_unique_id_or_builder = self.parent_unique_id_or_builder.to_dict()

        org_identifier_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.org_identifier_or_builder, Unset):
            org_identifier_or_builder = self.org_identifier_or_builder.to_dict()

        project_identifier_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_identifier_or_builder, Unset):
            project_identifier_or_builder = self.project_identifier_or_builder.to_dict()

        pipeline_identifier_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pipeline_identifier_or_builder, Unset):
            pipeline_identifier_or_builder = self.pipeline_identifier_or_builder.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        pipeline_identifier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pipeline_identifier, Unset):
            pipeline_identifier = self.pipeline_identifier.to_dict()

        initialized = self.initialized

        identifier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = self.identifier.to_dict()

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
        if account_identifier is not UNSET:
            field_dict["accountIdentifier"] = account_identifier
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if parent_unique_id is not UNSET:
            field_dict["parentUniqueId"] = parent_unique_id
        if identifier_or_builder is not UNSET:
            field_dict["identifierOrBuilder"] = identifier_or_builder
        if account_identifier_or_builder is not UNSET:
            field_dict["accountIdentifierOrBuilder"] = account_identifier_or_builder
        if parent_unique_id_or_builder is not UNSET:
            field_dict["parentUniqueIdOrBuilder"] = parent_unique_id_or_builder
        if org_identifier_or_builder is not UNSET:
            field_dict["orgIdentifierOrBuilder"] = org_identifier_or_builder
        if project_identifier_or_builder is not UNSET:
            field_dict["projectIdentifierOrBuilder"] = project_identifier_or_builder
        if pipeline_identifier_or_builder is not UNSET:
            field_dict["pipelineIdentifierOrBuilder"] = pipeline_identifier_or_builder
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if pipeline_identifier is not UNSET:
            field_dict["pipelineIdentifier"] = pipeline_identifier
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
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
        from ..models.descriptor import Descriptor
        from ..models.input_set_reference_proto_dto_all_fields import InputSetReferenceProtoDTOAllFields
        from ..models.parser_input_set_reference_proto_dto import ParserInputSetReferenceProtoDTO
        from ..models.string_value import StringValue
        from ..models.string_value_or_builder import StringValueOrBuilder
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

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

        _pipeline_identifier_or_builder = d.pop("pipelineIdentifierOrBuilder", UNSET)
        pipeline_identifier_or_builder: StringValueOrBuilder | Unset
        if isinstance(_pipeline_identifier_or_builder, Unset):
            pipeline_identifier_or_builder = UNSET
        else:
            pipeline_identifier_or_builder = StringValueOrBuilder.from_dict(_pipeline_identifier_or_builder)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserInputSetReferenceProtoDTO | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserInputSetReferenceProtoDTO.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: InputSetReferenceProtoDTO | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = InputSetReferenceProtoDTO.from_dict(_default_instance_for_type)

        _pipeline_identifier = d.pop("pipelineIdentifier", UNSET)
        pipeline_identifier: StringValue | Unset
        if isinstance(_pipeline_identifier, Unset):
            pipeline_identifier = UNSET
        else:
            pipeline_identifier = StringValue.from_dict(_pipeline_identifier)

        initialized = d.pop("initialized", UNSET)

        _identifier = d.pop("identifier", UNSET)
        identifier: StringValue | Unset
        if isinstance(_identifier, Unset):
            identifier = UNSET
        else:
            identifier = StringValue.from_dict(_identifier)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: InputSetReferenceProtoDTOAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = InputSetReferenceProtoDTOAllFields.from_dict(_all_fields)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        input_set_reference_proto_dto = cls(
            unknown_fields=unknown_fields,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            parent_unique_id=parent_unique_id,
            identifier_or_builder=identifier_or_builder,
            account_identifier_or_builder=account_identifier_or_builder,
            parent_unique_id_or_builder=parent_unique_id_or_builder,
            org_identifier_or_builder=org_identifier_or_builder,
            project_identifier_or_builder=project_identifier_or_builder,
            pipeline_identifier_or_builder=pipeline_identifier_or_builder,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            default_instance_for_type=default_instance_for_type,
            pipeline_identifier=pipeline_identifier,
            initialized=initialized,
            identifier=identifier,
            initialization_error_string=initialization_error_string,
            all_fields=all_fields,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        input_set_reference_proto_dto.additional_properties = d
        return input_set_reference_proto_dto

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
