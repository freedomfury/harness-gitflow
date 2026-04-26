from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.name_part import NamePart
    from ..models.name_part_or_builder import NamePartOrBuilder
    from ..models.parser_uninterpreted_option import ParserUninterpretedOption
    from ..models.uninterpreted_option_all_fields import UninterpretedOptionAllFields
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="UninterpretedOption")


@_attrs_define
class UninterpretedOption:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        string_value (ByteString | Unset):
        double_value (float | Unset):
        name_count (int | Unset):
        initialized (bool | Unset):
        default_instance_for_type (UninterpretedOption | Unset):
        parser_for_type (ParserUninterpretedOption | Unset):
        serialized_size (int | Unset):
        name_or_builder_list (list[NamePartOrBuilder] | Unset):
        identifier_value (str | Unset):
        identifier_value_bytes (ByteString | Unset):
        positive_int_value (int | Unset):
        negative_int_value (int | Unset):
        aggregate_value (str | Unset):
        aggregate_value_bytes (ByteString | Unset):
        name_list (list[NamePart] | Unset):
        all_fields (UninterpretedOptionAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    string_value: ByteString | Unset = UNSET
    double_value: float | Unset = UNSET
    name_count: int | Unset = UNSET
    initialized: bool | Unset = UNSET
    default_instance_for_type: UninterpretedOption | Unset = UNSET
    parser_for_type: ParserUninterpretedOption | Unset = UNSET
    serialized_size: int | Unset = UNSET
    name_or_builder_list: list[NamePartOrBuilder] | Unset = UNSET
    identifier_value: str | Unset = UNSET
    identifier_value_bytes: ByteString | Unset = UNSET
    positive_int_value: int | Unset = UNSET
    negative_int_value: int | Unset = UNSET
    aggregate_value: str | Unset = UNSET
    aggregate_value_bytes: ByteString | Unset = UNSET
    name_list: list[NamePart] | Unset = UNSET
    all_fields: UninterpretedOptionAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        string_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.string_value, Unset):
            string_value = self.string_value.to_dict()

        double_value = self.double_value

        name_count = self.name_count

        initialized = self.initialized

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        name_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.name_or_builder_list, Unset):
            name_or_builder_list = []
            for name_or_builder_list_item_data in self.name_or_builder_list:
                name_or_builder_list_item = name_or_builder_list_item_data.to_dict()
                name_or_builder_list.append(name_or_builder_list_item)

        identifier_value = self.identifier_value

        identifier_value_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifier_value_bytes, Unset):
            identifier_value_bytes = self.identifier_value_bytes.to_dict()

        positive_int_value = self.positive_int_value

        negative_int_value = self.negative_int_value

        aggregate_value = self.aggregate_value

        aggregate_value_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aggregate_value_bytes, Unset):
            aggregate_value_bytes = self.aggregate_value_bytes.to_dict()

        name_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.name_list, Unset):
            name_list = []
            for name_list_item_data in self.name_list:
                name_list_item = name_list_item_data.to_dict()
                name_list.append(name_list_item)

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
        if string_value is not UNSET:
            field_dict["stringValue"] = string_value
        if double_value is not UNSET:
            field_dict["doubleValue"] = double_value
        if name_count is not UNSET:
            field_dict["nameCount"] = name_count
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if name_or_builder_list is not UNSET:
            field_dict["nameOrBuilderList"] = name_or_builder_list
        if identifier_value is not UNSET:
            field_dict["identifierValue"] = identifier_value
        if identifier_value_bytes is not UNSET:
            field_dict["identifierValueBytes"] = identifier_value_bytes
        if positive_int_value is not UNSET:
            field_dict["positiveIntValue"] = positive_int_value
        if negative_int_value is not UNSET:
            field_dict["negativeIntValue"] = negative_int_value
        if aggregate_value is not UNSET:
            field_dict["aggregateValue"] = aggregate_value
        if aggregate_value_bytes is not UNSET:
            field_dict["aggregateValueBytes"] = aggregate_value_bytes
        if name_list is not UNSET:
            field_dict["nameList"] = name_list
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
        from ..models.name_part import NamePart
        from ..models.name_part_or_builder import NamePartOrBuilder
        from ..models.parser_uninterpreted_option import ParserUninterpretedOption
        from ..models.uninterpreted_option_all_fields import UninterpretedOptionAllFields
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        _string_value = d.pop("stringValue", UNSET)
        string_value: ByteString | Unset
        if isinstance(_string_value, Unset):
            string_value = UNSET
        else:
            string_value = ByteString.from_dict(_string_value)

        double_value = d.pop("doubleValue", UNSET)

        name_count = d.pop("nameCount", UNSET)

        initialized = d.pop("initialized", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: UninterpretedOption | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = UninterpretedOption.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserUninterpretedOption | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserUninterpretedOption.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _name_or_builder_list = d.pop("nameOrBuilderList", UNSET)
        name_or_builder_list: list[NamePartOrBuilder] | Unset = UNSET
        if _name_or_builder_list is not UNSET:
            name_or_builder_list = []
            for name_or_builder_list_item_data in _name_or_builder_list:
                name_or_builder_list_item = NamePartOrBuilder.from_dict(name_or_builder_list_item_data)

                name_or_builder_list.append(name_or_builder_list_item)

        identifier_value = d.pop("identifierValue", UNSET)

        _identifier_value_bytes = d.pop("identifierValueBytes", UNSET)
        identifier_value_bytes: ByteString | Unset
        if isinstance(_identifier_value_bytes, Unset):
            identifier_value_bytes = UNSET
        else:
            identifier_value_bytes = ByteString.from_dict(_identifier_value_bytes)

        positive_int_value = d.pop("positiveIntValue", UNSET)

        negative_int_value = d.pop("negativeIntValue", UNSET)

        aggregate_value = d.pop("aggregateValue", UNSET)

        _aggregate_value_bytes = d.pop("aggregateValueBytes", UNSET)
        aggregate_value_bytes: ByteString | Unset
        if isinstance(_aggregate_value_bytes, Unset):
            aggregate_value_bytes = UNSET
        else:
            aggregate_value_bytes = ByteString.from_dict(_aggregate_value_bytes)

        _name_list = d.pop("nameList", UNSET)
        name_list: list[NamePart] | Unset = UNSET
        if _name_list is not UNSET:
            name_list = []
            for name_list_item_data in _name_list:
                name_list_item = NamePart.from_dict(name_list_item_data)

                name_list.append(name_list_item)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: UninterpretedOptionAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = UninterpretedOptionAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        uninterpreted_option = cls(
            unknown_fields=unknown_fields,
            string_value=string_value,
            double_value=double_value,
            name_count=name_count,
            initialized=initialized,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            name_or_builder_list=name_or_builder_list,
            identifier_value=identifier_value,
            identifier_value_bytes=identifier_value_bytes,
            positive_int_value=positive_int_value,
            negative_int_value=negative_int_value,
            aggregate_value=aggregate_value,
            aggregate_value_bytes=aggregate_value_bytes,
            name_list=name_list,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        uninterpreted_option.additional_properties = d
        return uninterpreted_option

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
