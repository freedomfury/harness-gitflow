from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.feature_set_or_builder_enum_type import (
    FeatureSetOrBuilderEnumType,
    check_feature_set_or_builder_enum_type,
)
from ..models.feature_set_or_builder_field_presence import (
    FeatureSetOrBuilderFieldPresence,
    check_feature_set_or_builder_field_presence,
)
from ..models.feature_set_or_builder_json_format import (
    FeatureSetOrBuilderJsonFormat,
    check_feature_set_or_builder_json_format,
)
from ..models.feature_set_or_builder_message_encoding import (
    FeatureSetOrBuilderMessageEncoding,
    check_feature_set_or_builder_message_encoding,
)
from ..models.feature_set_or_builder_repeated_field_encoding import (
    FeatureSetOrBuilderRepeatedFieldEncoding,
    check_feature_set_or_builder_repeated_field_encoding,
)
from ..models.feature_set_or_builder_utf_8_validation import (
    FeatureSetOrBuilderUtf8Validation,
    check_feature_set_or_builder_utf_8_validation,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.descriptor import Descriptor
    from ..models.feature_set_or_builder_all_fields import FeatureSetOrBuilderAllFields
    from ..models.message import Message
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="FeatureSetOrBuilder")


@_attrs_define
class FeatureSetOrBuilder:
    """
    Attributes:
        enum_type (FeatureSetOrBuilderEnumType | Unset):
        message_encoding (FeatureSetOrBuilderMessageEncoding | Unset):
        utf_8_validation (FeatureSetOrBuilderUtf8Validation | Unset):
        field_presence (FeatureSetOrBuilderFieldPresence | Unset):
        repeated_field_encoding (FeatureSetOrBuilderRepeatedFieldEncoding | Unset):
        json_format (FeatureSetOrBuilderJsonFormat | Unset):
        default_instance_for_type (Message | Unset):
        all_fields (FeatureSetOrBuilderAllFields | Unset):
        unknown_fields (UnknownFieldSet | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        initialized (bool | Unset):
    """

    enum_type: FeatureSetOrBuilderEnumType | Unset = UNSET
    message_encoding: FeatureSetOrBuilderMessageEncoding | Unset = UNSET
    utf_8_validation: FeatureSetOrBuilderUtf8Validation | Unset = UNSET
    field_presence: FeatureSetOrBuilderFieldPresence | Unset = UNSET
    repeated_field_encoding: FeatureSetOrBuilderRepeatedFieldEncoding | Unset = UNSET
    json_format: FeatureSetOrBuilderJsonFormat | Unset = UNSET
    default_instance_for_type: Message | Unset = UNSET
    all_fields: FeatureSetOrBuilderAllFields | Unset = UNSET
    unknown_fields: UnknownFieldSet | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    initialized: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enum_type: str | Unset = UNSET
        if not isinstance(self.enum_type, Unset):
            enum_type = self.enum_type

        message_encoding: str | Unset = UNSET
        if not isinstance(self.message_encoding, Unset):
            message_encoding = self.message_encoding

        utf_8_validation: str | Unset = UNSET
        if not isinstance(self.utf_8_validation, Unset):
            utf_8_validation = self.utf_8_validation

        field_presence: str | Unset = UNSET
        if not isinstance(self.field_presence, Unset):
            field_presence = self.field_presence

        repeated_field_encoding: str | Unset = UNSET
        if not isinstance(self.repeated_field_encoding, Unset):
            repeated_field_encoding = self.repeated_field_encoding

        json_format: str | Unset = UNSET
        if not isinstance(self.json_format, Unset):
            json_format = self.json_format

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        all_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_fields, Unset):
            all_fields = self.all_fields.to_dict()

        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        initialization_error_string = self.initialization_error_string

        descriptor_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.descriptor_for_type, Unset):
            descriptor_for_type = self.descriptor_for_type.to_dict()

        initialized = self.initialized

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enum_type is not UNSET:
            field_dict["enumType"] = enum_type
        if message_encoding is not UNSET:
            field_dict["messageEncoding"] = message_encoding
        if utf_8_validation is not UNSET:
            field_dict["utf8Validation"] = utf_8_validation
        if field_presence is not UNSET:
            field_dict["fieldPresence"] = field_presence
        if repeated_field_encoding is not UNSET:
            field_dict["repeatedFieldEncoding"] = repeated_field_encoding
        if json_format is not UNSET:
            field_dict["jsonFormat"] = json_format
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if all_fields is not UNSET:
            field_dict["allFields"] = all_fields
        if unknown_fields is not UNSET:
            field_dict["unknownFields"] = unknown_fields
        if initialization_error_string is not UNSET:
            field_dict["initializationErrorString"] = initialization_error_string
        if descriptor_for_type is not UNSET:
            field_dict["descriptorForType"] = descriptor_for_type
        if initialized is not UNSET:
            field_dict["initialized"] = initialized

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.descriptor import Descriptor
        from ..models.feature_set_or_builder_all_fields import FeatureSetOrBuilderAllFields
        from ..models.message import Message
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _enum_type = d.pop("enumType", UNSET)
        enum_type: FeatureSetOrBuilderEnumType | Unset
        if isinstance(_enum_type, Unset):
            enum_type = UNSET
        else:
            enum_type = check_feature_set_or_builder_enum_type(_enum_type)

        _message_encoding = d.pop("messageEncoding", UNSET)
        message_encoding: FeatureSetOrBuilderMessageEncoding | Unset
        if isinstance(_message_encoding, Unset):
            message_encoding = UNSET
        else:
            message_encoding = check_feature_set_or_builder_message_encoding(_message_encoding)

        _utf_8_validation = d.pop("utf8Validation", UNSET)
        utf_8_validation: FeatureSetOrBuilderUtf8Validation | Unset
        if isinstance(_utf_8_validation, Unset):
            utf_8_validation = UNSET
        else:
            utf_8_validation = check_feature_set_or_builder_utf_8_validation(_utf_8_validation)

        _field_presence = d.pop("fieldPresence", UNSET)
        field_presence: FeatureSetOrBuilderFieldPresence | Unset
        if isinstance(_field_presence, Unset):
            field_presence = UNSET
        else:
            field_presence = check_feature_set_or_builder_field_presence(_field_presence)

        _repeated_field_encoding = d.pop("repeatedFieldEncoding", UNSET)
        repeated_field_encoding: FeatureSetOrBuilderRepeatedFieldEncoding | Unset
        if isinstance(_repeated_field_encoding, Unset):
            repeated_field_encoding = UNSET
        else:
            repeated_field_encoding = check_feature_set_or_builder_repeated_field_encoding(_repeated_field_encoding)

        _json_format = d.pop("jsonFormat", UNSET)
        json_format: FeatureSetOrBuilderJsonFormat | Unset
        if isinstance(_json_format, Unset):
            json_format = UNSET
        else:
            json_format = check_feature_set_or_builder_json_format(_json_format)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: Message | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = Message.from_dict(_default_instance_for_type)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: FeatureSetOrBuilderAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = FeatureSetOrBuilderAllFields.from_dict(_all_fields)

        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        initialized = d.pop("initialized", UNSET)

        feature_set_or_builder = cls(
            enum_type=enum_type,
            message_encoding=message_encoding,
            utf_8_validation=utf_8_validation,
            field_presence=field_presence,
            repeated_field_encoding=repeated_field_encoding,
            json_format=json_format,
            default_instance_for_type=default_instance_for_type,
            all_fields=all_fields,
            unknown_fields=unknown_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            initialized=initialized,
        )

        feature_set_or_builder.additional_properties = d
        return feature_set_or_builder

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
