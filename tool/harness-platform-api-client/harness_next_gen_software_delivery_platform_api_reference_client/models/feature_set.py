from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.feature_set_enum_type import FeatureSetEnumType, check_feature_set_enum_type
from ..models.feature_set_field_presence import FeatureSetFieldPresence, check_feature_set_field_presence
from ..models.feature_set_json_format import FeatureSetJsonFormat, check_feature_set_json_format
from ..models.feature_set_message_encoding import FeatureSetMessageEncoding, check_feature_set_message_encoding
from ..models.feature_set_repeated_field_encoding import (
    FeatureSetRepeatedFieldEncoding,
    check_feature_set_repeated_field_encoding,
)
from ..models.feature_set_utf_8_validation import FeatureSetUtf8Validation, check_feature_set_utf_8_validation
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.descriptor import Descriptor
    from ..models.feature_set_all_fields import FeatureSetAllFields
    from ..models.feature_set_all_fields_raw import FeatureSetAllFieldsRaw
    from ..models.parser_feature_set import ParserFeatureSet
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="FeatureSet")


@_attrs_define
class FeatureSet:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        json_format (FeatureSetJsonFormat | Unset):
        enum_type (FeatureSetEnumType | Unset):
        parser_for_type (ParserFeatureSet | Unset):
        serialized_size (int | Unset):
        repeated_field_encoding (FeatureSetRepeatedFieldEncoding | Unset):
        default_instance_for_type (FeatureSet | Unset):
        message_encoding (FeatureSetMessageEncoding | Unset):
        utf_8_validation (FeatureSetUtf8Validation | Unset):
        field_presence (FeatureSetFieldPresence | Unset):
        initialized (bool | Unset):
        initialization_error_string (str | Unset):
        all_fields (FeatureSetAllFields | Unset):
        descriptor_for_type (Descriptor | Unset):
        all_fields_raw (FeatureSetAllFieldsRaw | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    json_format: FeatureSetJsonFormat | Unset = UNSET
    enum_type: FeatureSetEnumType | Unset = UNSET
    parser_for_type: ParserFeatureSet | Unset = UNSET
    serialized_size: int | Unset = UNSET
    repeated_field_encoding: FeatureSetRepeatedFieldEncoding | Unset = UNSET
    default_instance_for_type: FeatureSet | Unset = UNSET
    message_encoding: FeatureSetMessageEncoding | Unset = UNSET
    utf_8_validation: FeatureSetUtf8Validation | Unset = UNSET
    field_presence: FeatureSetFieldPresence | Unset = UNSET
    initialized: bool | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    all_fields: FeatureSetAllFields | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    all_fields_raw: FeatureSetAllFieldsRaw | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        json_format: str | Unset = UNSET
        if not isinstance(self.json_format, Unset):
            json_format = self.json_format

        enum_type: str | Unset = UNSET
        if not isinstance(self.enum_type, Unset):
            enum_type = self.enum_type

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        repeated_field_encoding: str | Unset = UNSET
        if not isinstance(self.repeated_field_encoding, Unset):
            repeated_field_encoding = self.repeated_field_encoding

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        message_encoding: str | Unset = UNSET
        if not isinstance(self.message_encoding, Unset):
            message_encoding = self.message_encoding

        utf_8_validation: str | Unset = UNSET
        if not isinstance(self.utf_8_validation, Unset):
            utf_8_validation = self.utf_8_validation

        field_presence: str | Unset = UNSET
        if not isinstance(self.field_presence, Unset):
            field_presence = self.field_presence

        initialized = self.initialized

        initialization_error_string = self.initialization_error_string

        all_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_fields, Unset):
            all_fields = self.all_fields.to_dict()

        descriptor_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.descriptor_for_type, Unset):
            descriptor_for_type = self.descriptor_for_type.to_dict()

        all_fields_raw: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_fields_raw, Unset):
            all_fields_raw = self.all_fields_raw.to_dict()

        memoized_serialized_size = self.memoized_serialized_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unknown_fields is not UNSET:
            field_dict["unknownFields"] = unknown_fields
        if json_format is not UNSET:
            field_dict["jsonFormat"] = json_format
        if enum_type is not UNSET:
            field_dict["enumType"] = enum_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if repeated_field_encoding is not UNSET:
            field_dict["repeatedFieldEncoding"] = repeated_field_encoding
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if message_encoding is not UNSET:
            field_dict["messageEncoding"] = message_encoding
        if utf_8_validation is not UNSET:
            field_dict["utf8Validation"] = utf_8_validation
        if field_presence is not UNSET:
            field_dict["fieldPresence"] = field_presence
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if initialization_error_string is not UNSET:
            field_dict["initializationErrorString"] = initialization_error_string
        if all_fields is not UNSET:
            field_dict["allFields"] = all_fields
        if descriptor_for_type is not UNSET:
            field_dict["descriptorForType"] = descriptor_for_type
        if all_fields_raw is not UNSET:
            field_dict["allFieldsRaw"] = all_fields_raw
        if memoized_serialized_size is not UNSET:
            field_dict["memoizedSerializedSize"] = memoized_serialized_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.descriptor import Descriptor
        from ..models.feature_set_all_fields import FeatureSetAllFields
        from ..models.feature_set_all_fields_raw import FeatureSetAllFieldsRaw
        from ..models.parser_feature_set import ParserFeatureSet
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        _json_format = d.pop("jsonFormat", UNSET)
        json_format: FeatureSetJsonFormat | Unset
        if isinstance(_json_format, Unset):
            json_format = UNSET
        else:
            json_format = check_feature_set_json_format(_json_format)

        _enum_type = d.pop("enumType", UNSET)
        enum_type: FeatureSetEnumType | Unset
        if isinstance(_enum_type, Unset):
            enum_type = UNSET
        else:
            enum_type = check_feature_set_enum_type(_enum_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserFeatureSet | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserFeatureSet.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _repeated_field_encoding = d.pop("repeatedFieldEncoding", UNSET)
        repeated_field_encoding: FeatureSetRepeatedFieldEncoding | Unset
        if isinstance(_repeated_field_encoding, Unset):
            repeated_field_encoding = UNSET
        else:
            repeated_field_encoding = check_feature_set_repeated_field_encoding(_repeated_field_encoding)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: FeatureSet | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = FeatureSet.from_dict(_default_instance_for_type)

        _message_encoding = d.pop("messageEncoding", UNSET)
        message_encoding: FeatureSetMessageEncoding | Unset
        if isinstance(_message_encoding, Unset):
            message_encoding = UNSET
        else:
            message_encoding = check_feature_set_message_encoding(_message_encoding)

        _utf_8_validation = d.pop("utf8Validation", UNSET)
        utf_8_validation: FeatureSetUtf8Validation | Unset
        if isinstance(_utf_8_validation, Unset):
            utf_8_validation = UNSET
        else:
            utf_8_validation = check_feature_set_utf_8_validation(_utf_8_validation)

        _field_presence = d.pop("fieldPresence", UNSET)
        field_presence: FeatureSetFieldPresence | Unset
        if isinstance(_field_presence, Unset):
            field_presence = UNSET
        else:
            field_presence = check_feature_set_field_presence(_field_presence)

        initialized = d.pop("initialized", UNSET)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: FeatureSetAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = FeatureSetAllFields.from_dict(_all_fields)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        _all_fields_raw = d.pop("allFieldsRaw", UNSET)
        all_fields_raw: FeatureSetAllFieldsRaw | Unset
        if isinstance(_all_fields_raw, Unset):
            all_fields_raw = UNSET
        else:
            all_fields_raw = FeatureSetAllFieldsRaw.from_dict(_all_fields_raw)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        feature_set = cls(
            unknown_fields=unknown_fields,
            json_format=json_format,
            enum_type=enum_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            repeated_field_encoding=repeated_field_encoding,
            default_instance_for_type=default_instance_for_type,
            message_encoding=message_encoding,
            utf_8_validation=utf_8_validation,
            field_presence=field_presence,
            initialized=initialized,
            initialization_error_string=initialization_error_string,
            all_fields=all_fields,
            descriptor_for_type=descriptor_for_type,
            all_fields_raw=all_fields_raw,
            memoized_serialized_size=memoized_serialized_size,
        )

        feature_set.additional_properties = d
        return feature_set

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
