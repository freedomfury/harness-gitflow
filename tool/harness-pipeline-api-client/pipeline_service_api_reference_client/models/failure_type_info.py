from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.failure_type_info_failure_sub_type import (
    FailureTypeInfoFailureSubType,
    check_failure_type_info_failure_sub_type,
)
from ..models.failure_type_info_failure_type import FailureTypeInfoFailureType, check_failure_type_info_failure_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.descriptor import Descriptor
    from ..models.failure_type_info_all_fields import FailureTypeInfoAllFields
    from ..models.parser_failure_type_info import ParserFailureTypeInfo
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="FailureTypeInfo")


@_attrs_define
class FailureTypeInfo:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        failure_type (FailureTypeInfoFailureType | Unset):
        failure_sub_type (FailureTypeInfoFailureSubType | Unset):
        failure_type_value (int | Unset):
        failure_sub_type_value (int | Unset):
        initialized (bool | Unset):
        default_instance_for_type (FailureTypeInfo | Unset):
        parser_for_type (ParserFailureTypeInfo | Unset):
        serialized_size (int | Unset):
        all_fields (FailureTypeInfoAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    failure_type: FailureTypeInfoFailureType | Unset = UNSET
    failure_sub_type: FailureTypeInfoFailureSubType | Unset = UNSET
    failure_type_value: int | Unset = UNSET
    failure_sub_type_value: int | Unset = UNSET
    initialized: bool | Unset = UNSET
    default_instance_for_type: FailureTypeInfo | Unset = UNSET
    parser_for_type: ParserFailureTypeInfo | Unset = UNSET
    serialized_size: int | Unset = UNSET
    all_fields: FailureTypeInfoAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        failure_type: str | Unset = UNSET
        if not isinstance(self.failure_type, Unset):
            failure_type = self.failure_type

        failure_sub_type: str | Unset = UNSET
        if not isinstance(self.failure_sub_type, Unset):
            failure_sub_type = self.failure_sub_type

        failure_type_value = self.failure_type_value

        failure_sub_type_value = self.failure_sub_type_value

        initialized = self.initialized

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

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
        if failure_type is not UNSET:
            field_dict["failureType"] = failure_type
        if failure_sub_type is not UNSET:
            field_dict["failureSubType"] = failure_sub_type
        if failure_type_value is not UNSET:
            field_dict["failureTypeValue"] = failure_type_value
        if failure_sub_type_value is not UNSET:
            field_dict["failureSubTypeValue"] = failure_sub_type_value
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
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
        from ..models.failure_type_info_all_fields import FailureTypeInfoAllFields
        from ..models.parser_failure_type_info import ParserFailureTypeInfo
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        _failure_type = d.pop("failureType", UNSET)
        failure_type: FailureTypeInfoFailureType | Unset
        if isinstance(_failure_type, Unset):
            failure_type = UNSET
        else:
            failure_type = check_failure_type_info_failure_type(_failure_type)

        _failure_sub_type = d.pop("failureSubType", UNSET)
        failure_sub_type: FailureTypeInfoFailureSubType | Unset
        if isinstance(_failure_sub_type, Unset):
            failure_sub_type = UNSET
        else:
            failure_sub_type = check_failure_type_info_failure_sub_type(_failure_sub_type)

        failure_type_value = d.pop("failureTypeValue", UNSET)

        failure_sub_type_value = d.pop("failureSubTypeValue", UNSET)

        initialized = d.pop("initialized", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: FailureTypeInfo | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = FailureTypeInfo.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserFailureTypeInfo | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserFailureTypeInfo.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: FailureTypeInfoAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = FailureTypeInfoAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        failure_type_info = cls(
            unknown_fields=unknown_fields,
            failure_type=failure_type,
            failure_sub_type=failure_sub_type,
            failure_type_value=failure_type_value,
            failure_sub_type_value=failure_sub_type_value,
            initialized=initialized,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        failure_type_info.additional_properties = d
        return failure_type_info

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
