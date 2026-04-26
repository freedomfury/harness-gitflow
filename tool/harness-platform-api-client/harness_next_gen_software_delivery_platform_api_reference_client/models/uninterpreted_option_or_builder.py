from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.message import Message
    from ..models.name_part import NamePart
    from ..models.name_part_or_builder import NamePartOrBuilder
    from ..models.uninterpreted_option_or_builder_all_fields import UninterpretedOptionOrBuilderAllFields
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="UninterpretedOptionOrBuilder")


@_attrs_define
class UninterpretedOptionOrBuilder:
    """
    Attributes:
        name_list (list[NamePart] | Unset):
        name_or_builder_list (list[NamePartOrBuilder] | Unset):
        identifier_value (str | Unset):
        identifier_value_bytes (ByteString | Unset):
        positive_int_value (int | Unset):
        negative_int_value (int | Unset):
        aggregate_value (str | Unset):
        aggregate_value_bytes (ByteString | Unset):
        name_count (int | Unset):
        string_value (ByteString | Unset):
        double_value (float | Unset):
        initialization_error_string (str | Unset):
        all_fields (UninterpretedOptionOrBuilderAllFields | Unset):
        unknown_fields (UnknownFieldSet | Unset):
        descriptor_for_type (Descriptor | Unset):
        default_instance_for_type (Message | Unset):
        initialized (bool | Unset):
    """

    name_list: list[NamePart] | Unset = UNSET
    name_or_builder_list: list[NamePartOrBuilder] | Unset = UNSET
    identifier_value: str | Unset = UNSET
    identifier_value_bytes: ByteString | Unset = UNSET
    positive_int_value: int | Unset = UNSET
    negative_int_value: int | Unset = UNSET
    aggregate_value: str | Unset = UNSET
    aggregate_value_bytes: ByteString | Unset = UNSET
    name_count: int | Unset = UNSET
    string_value: ByteString | Unset = UNSET
    double_value: float | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    all_fields: UninterpretedOptionOrBuilderAllFields | Unset = UNSET
    unknown_fields: UnknownFieldSet | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    default_instance_for_type: Message | Unset = UNSET
    initialized: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.name_list, Unset):
            name_list = []
            for name_list_item_data in self.name_list:
                name_list_item = name_list_item_data.to_dict()
                name_list.append(name_list_item)

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

        name_count = self.name_count

        string_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.string_value, Unset):
            string_value = self.string_value.to_dict()

        double_value = self.double_value

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
        if name_list is not UNSET:
            field_dict["nameList"] = name_list
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
        if name_count is not UNSET:
            field_dict["nameCount"] = name_count
        if string_value is not UNSET:
            field_dict["stringValue"] = string_value
        if double_value is not UNSET:
            field_dict["doubleValue"] = double_value
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
        from ..models.byte_string import ByteString
        from ..models.descriptor import Descriptor
        from ..models.message import Message
        from ..models.name_part import NamePart
        from ..models.name_part_or_builder import NamePartOrBuilder
        from ..models.uninterpreted_option_or_builder_all_fields import UninterpretedOptionOrBuilderAllFields
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _name_list = d.pop("nameList", UNSET)
        name_list: list[NamePart] | Unset = UNSET
        if _name_list is not UNSET:
            name_list = []
            for name_list_item_data in _name_list:
                name_list_item = NamePart.from_dict(name_list_item_data)

                name_list.append(name_list_item)

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

        name_count = d.pop("nameCount", UNSET)

        _string_value = d.pop("stringValue", UNSET)
        string_value: ByteString | Unset
        if isinstance(_string_value, Unset):
            string_value = UNSET
        else:
            string_value = ByteString.from_dict(_string_value)

        double_value = d.pop("doubleValue", UNSET)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: UninterpretedOptionOrBuilderAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = UninterpretedOptionOrBuilderAllFields.from_dict(_all_fields)

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

        uninterpreted_option_or_builder = cls(
            name_list=name_list,
            name_or_builder_list=name_or_builder_list,
            identifier_value=identifier_value,
            identifier_value_bytes=identifier_value_bytes,
            positive_int_value=positive_int_value,
            negative_int_value=negative_int_value,
            aggregate_value=aggregate_value,
            aggregate_value_bytes=aggregate_value_bytes,
            name_count=name_count,
            string_value=string_value,
            double_value=double_value,
            initialization_error_string=initialization_error_string,
            all_fields=all_fields,
            unknown_fields=unknown_fields,
            descriptor_for_type=descriptor_for_type,
            default_instance_for_type=default_instance_for_type,
            initialized=initialized,
        )

        uninterpreted_option_or_builder.additional_properties = d
        return uninterpreted_option_or_builder

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
