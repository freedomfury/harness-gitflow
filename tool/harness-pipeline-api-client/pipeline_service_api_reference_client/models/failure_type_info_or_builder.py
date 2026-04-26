from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.failure_type_info_or_builder_failure_sub_type import (
    FailureTypeInfoOrBuilderFailureSubType,
    check_failure_type_info_or_builder_failure_sub_type,
)
from ..models.failure_type_info_or_builder_failure_type import (
    FailureTypeInfoOrBuilderFailureType,
    check_failure_type_info_or_builder_failure_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.descriptor import Descriptor
    from ..models.failure_type_info_or_builder_all_fields import FailureTypeInfoOrBuilderAllFields
    from ..models.message import Message
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="FailureTypeInfoOrBuilder")


@_attrs_define
class FailureTypeInfoOrBuilder:
    """
    Attributes:
        failure_type (FailureTypeInfoOrBuilderFailureType | Unset):
        failure_sub_type (FailureTypeInfoOrBuilderFailureSubType | Unset):
        failure_type_value (int | Unset):
        failure_sub_type_value (int | Unset):
        all_fields (FailureTypeInfoOrBuilderAllFields | Unset):
        default_instance_for_type (Message | Unset):
        unknown_fields (UnknownFieldSet | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        initialized (bool | Unset):
    """

    failure_type: FailureTypeInfoOrBuilderFailureType | Unset = UNSET
    failure_sub_type: FailureTypeInfoOrBuilderFailureSubType | Unset = UNSET
    failure_type_value: int | Unset = UNSET
    failure_sub_type_value: int | Unset = UNSET
    all_fields: FailureTypeInfoOrBuilderAllFields | Unset = UNSET
    default_instance_for_type: Message | Unset = UNSET
    unknown_fields: UnknownFieldSet | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    initialized: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        failure_type: str | Unset = UNSET
        if not isinstance(self.failure_type, Unset):
            failure_type = self.failure_type

        failure_sub_type: str | Unset = UNSET
        if not isinstance(self.failure_sub_type, Unset):
            failure_sub_type = self.failure_sub_type

        failure_type_value = self.failure_type_value

        failure_sub_type_value = self.failure_sub_type_value

        all_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_fields, Unset):
            all_fields = self.all_fields.to_dict()

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

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
        if failure_type is not UNSET:
            field_dict["failureType"] = failure_type
        if failure_sub_type is not UNSET:
            field_dict["failureSubType"] = failure_sub_type
        if failure_type_value is not UNSET:
            field_dict["failureTypeValue"] = failure_type_value
        if failure_sub_type_value is not UNSET:
            field_dict["failureSubTypeValue"] = failure_sub_type_value
        if all_fields is not UNSET:
            field_dict["allFields"] = all_fields
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
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
        from ..models.failure_type_info_or_builder_all_fields import FailureTypeInfoOrBuilderAllFields
        from ..models.message import Message
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _failure_type = d.pop("failureType", UNSET)
        failure_type: FailureTypeInfoOrBuilderFailureType | Unset
        if isinstance(_failure_type, Unset):
            failure_type = UNSET
        else:
            failure_type = check_failure_type_info_or_builder_failure_type(_failure_type)

        _failure_sub_type = d.pop("failureSubType", UNSET)
        failure_sub_type: FailureTypeInfoOrBuilderFailureSubType | Unset
        if isinstance(_failure_sub_type, Unset):
            failure_sub_type = UNSET
        else:
            failure_sub_type = check_failure_type_info_or_builder_failure_sub_type(_failure_sub_type)

        failure_type_value = d.pop("failureTypeValue", UNSET)

        failure_sub_type_value = d.pop("failureSubTypeValue", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: FailureTypeInfoOrBuilderAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = FailureTypeInfoOrBuilderAllFields.from_dict(_all_fields)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: Message | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = Message.from_dict(_default_instance_for_type)

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

        failure_type_info_or_builder = cls(
            failure_type=failure_type,
            failure_sub_type=failure_sub_type,
            failure_type_value=failure_type_value,
            failure_sub_type_value=failure_sub_type_value,
            all_fields=all_fields,
            default_instance_for_type=default_instance_for_type,
            unknown_fields=unknown_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            initialized=initialized,
        )

        failure_type_info_or_builder.additional_properties = d
        return failure_type_info_or_builder

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
