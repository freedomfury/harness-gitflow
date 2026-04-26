from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.descriptor import Descriptor
    from ..models.extension_range_all_fields import ExtensionRangeAllFields
    from ..models.extension_range_options import ExtensionRangeOptions
    from ..models.extension_range_options_or_builder import ExtensionRangeOptionsOrBuilder
    from ..models.parser_extension_range import ParserExtensionRange
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="ExtensionRange")


@_attrs_define
class ExtensionRange:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        initialized (bool | Unset):
        options (ExtensionRangeOptions | Unset):
        start (int | Unset):
        end (int | Unset):
        default_instance_for_type (ExtensionRange | Unset):
        parser_for_type (ParserExtensionRange | Unset):
        serialized_size (int | Unset):
        options_or_builder (ExtensionRangeOptionsOrBuilder | Unset):
        all_fields (ExtensionRangeAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    initialized: bool | Unset = UNSET
    options: ExtensionRangeOptions | Unset = UNSET
    start: int | Unset = UNSET
    end: int | Unset = UNSET
    default_instance_for_type: ExtensionRange | Unset = UNSET
    parser_for_type: ParserExtensionRange | Unset = UNSET
    serialized_size: int | Unset = UNSET
    options_or_builder: ExtensionRangeOptionsOrBuilder | Unset = UNSET
    all_fields: ExtensionRangeAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        initialized = self.initialized

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        start = self.start

        end = self.end

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        options_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options_or_builder, Unset):
            options_or_builder = self.options_or_builder.to_dict()

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
        if options is not UNSET:
            field_dict["options"] = options
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if options_or_builder is not UNSET:
            field_dict["optionsOrBuilder"] = options_or_builder
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
        from ..models.descriptor import Descriptor
        from ..models.extension_range_all_fields import ExtensionRangeAllFields
        from ..models.extension_range_options import ExtensionRangeOptions
        from ..models.extension_range_options_or_builder import ExtensionRangeOptionsOrBuilder
        from ..models.parser_extension_range import ParserExtensionRange
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        initialized = d.pop("initialized", UNSET)

        _options = d.pop("options", UNSET)
        options: ExtensionRangeOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = ExtensionRangeOptions.from_dict(_options)

        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: ExtensionRange | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = ExtensionRange.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserExtensionRange | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserExtensionRange.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _options_or_builder = d.pop("optionsOrBuilder", UNSET)
        options_or_builder: ExtensionRangeOptionsOrBuilder | Unset
        if isinstance(_options_or_builder, Unset):
            options_or_builder = UNSET
        else:
            options_or_builder = ExtensionRangeOptionsOrBuilder.from_dict(_options_or_builder)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: ExtensionRangeAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = ExtensionRangeAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        extension_range = cls(
            unknown_fields=unknown_fields,
            initialized=initialized,
            options=options,
            start=start,
            end=end,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            options_or_builder=options_or_builder,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        extension_range.additional_properties = d
        return extension_range

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
