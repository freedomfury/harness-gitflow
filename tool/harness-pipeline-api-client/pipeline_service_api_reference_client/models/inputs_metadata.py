from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.inputs_metadata_all_fields import InputsMetadataAllFields
    from ..models.parser_inputs_metadata import ParserInputsMetadata
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="InputsMetadata")


@_attrs_define
class InputsMetadata:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        initialized (bool | Unset):
        description (str | Unset):
        default_instance_for_type (InputsMetadata | Unset):
        parser_for_type (ParserInputsMetadata | Unset):
        serialized_size (int | Unset):
        description_bytes (ByteString | Unset):
        required (bool | Unset):
        all_fields (InputsMetadataAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    initialized: bool | Unset = UNSET
    description: str | Unset = UNSET
    default_instance_for_type: InputsMetadata | Unset = UNSET
    parser_for_type: ParserInputsMetadata | Unset = UNSET
    serialized_size: int | Unset = UNSET
    description_bytes: ByteString | Unset = UNSET
    required: bool | Unset = UNSET
    all_fields: InputsMetadataAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        initialized = self.initialized

        description = self.description

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        description_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.description_bytes, Unset):
            description_bytes = self.description_bytes.to_dict()

        required = self.required

        all_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_fields, Unset):
            all_fields = self.all_fields.to_dict()

        initialization_error_string = self.initialization_error_string

        descriptor_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.descriptor_for_type, Unset):
            descriptor_for_type = self.descriptor_for_type.to_dict()

        memoized_serialized_size = self.memoized_serialized_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unknown_fields is not UNSET:
            field_dict["unknownFields"] = unknown_fields
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if description is not UNSET:
            field_dict["description"] = description
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if description_bytes is not UNSET:
            field_dict["descriptionBytes"] = description_bytes
        if required is not UNSET:
            field_dict["required"] = required
        if all_fields is not UNSET:
            field_dict["allFields"] = all_fields
        if initialization_error_string is not UNSET:
            field_dict["initializationErrorString"] = initialization_error_string
        if descriptor_for_type is not UNSET:
            field_dict["descriptorForType"] = descriptor_for_type
        if memoized_serialized_size is not UNSET:
            field_dict["memoizedSerializedSize"] = memoized_serialized_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.byte_string import ByteString
        from ..models.descriptor import Descriptor
        from ..models.inputs_metadata_all_fields import InputsMetadataAllFields
        from ..models.parser_inputs_metadata import ParserInputsMetadata
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        initialized = d.pop("initialized", UNSET)

        description = d.pop("description", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: InputsMetadata | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = InputsMetadata.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserInputsMetadata | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserInputsMetadata.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _description_bytes = d.pop("descriptionBytes", UNSET)
        description_bytes: ByteString | Unset
        if isinstance(_description_bytes, Unset):
            description_bytes = UNSET
        else:
            description_bytes = ByteString.from_dict(_description_bytes)

        required = d.pop("required", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: InputsMetadataAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = InputsMetadataAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        inputs_metadata = cls(
            unknown_fields=unknown_fields,
            initialized=initialized,
            description=description,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            description_bytes=description_bytes,
            required=required,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        inputs_metadata.additional_properties = d
        return inputs_metadata

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
