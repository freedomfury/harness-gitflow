from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.step_type_or_builder_step_category import (
    StepTypeOrBuilderStepCategory,
    check_step_type_or_builder_step_category,
)
from ..models.step_type_or_builder_sub_category import (
    StepTypeOrBuilderSubCategory,
    check_step_type_or_builder_sub_category,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.message import Message
    from ..models.step_type_or_builder_all_fields import StepTypeOrBuilderAllFields
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="StepTypeOrBuilder")


@_attrs_define
class StepTypeOrBuilder:
    """
    Attributes:
        type_ (str | Unset):
        type_bytes (ByteString | Unset):
        step_category_value (int | Unset):
        step_category (StepTypeOrBuilderStepCategory | Unset):
        sub_category_value (int | Unset):
        sub_category (StepTypeOrBuilderSubCategory | Unset):
        all_fields (StepTypeOrBuilderAllFields | Unset):
        default_instance_for_type (Message | Unset):
        unknown_fields (UnknownFieldSet | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        initialized (bool | Unset):
    """

    type_: str | Unset = UNSET
    type_bytes: ByteString | Unset = UNSET
    step_category_value: int | Unset = UNSET
    step_category: StepTypeOrBuilderStepCategory | Unset = UNSET
    sub_category_value: int | Unset = UNSET
    sub_category: StepTypeOrBuilderSubCategory | Unset = UNSET
    all_fields: StepTypeOrBuilderAllFields | Unset = UNSET
    default_instance_for_type: Message | Unset = UNSET
    unknown_fields: UnknownFieldSet | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    initialized: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        type_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.type_bytes, Unset):
            type_bytes = self.type_bytes.to_dict()

        step_category_value = self.step_category_value

        step_category: str | Unset = UNSET
        if not isinstance(self.step_category, Unset):
            step_category = self.step_category

        sub_category_value = self.sub_category_value

        sub_category: str | Unset = UNSET
        if not isinstance(self.sub_category, Unset):
            sub_category = self.sub_category

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
        if type_ is not UNSET:
            field_dict["type"] = type_
        if type_bytes is not UNSET:
            field_dict["typeBytes"] = type_bytes
        if step_category_value is not UNSET:
            field_dict["stepCategoryValue"] = step_category_value
        if step_category is not UNSET:
            field_dict["stepCategory"] = step_category
        if sub_category_value is not UNSET:
            field_dict["subCategoryValue"] = sub_category_value
        if sub_category is not UNSET:
            field_dict["subCategory"] = sub_category
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
        from ..models.byte_string import ByteString
        from ..models.descriptor import Descriptor
        from ..models.message import Message
        from ..models.step_type_or_builder_all_fields import StepTypeOrBuilderAllFields
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        _type_bytes = d.pop("typeBytes", UNSET)
        type_bytes: ByteString | Unset
        if isinstance(_type_bytes, Unset):
            type_bytes = UNSET
        else:
            type_bytes = ByteString.from_dict(_type_bytes)

        step_category_value = d.pop("stepCategoryValue", UNSET)

        _step_category = d.pop("stepCategory", UNSET)
        step_category: StepTypeOrBuilderStepCategory | Unset
        if isinstance(_step_category, Unset):
            step_category = UNSET
        else:
            step_category = check_step_type_or_builder_step_category(_step_category)

        sub_category_value = d.pop("subCategoryValue", UNSET)

        _sub_category = d.pop("subCategory", UNSET)
        sub_category: StepTypeOrBuilderSubCategory | Unset
        if isinstance(_sub_category, Unset):
            sub_category = UNSET
        else:
            sub_category = check_step_type_or_builder_sub_category(_sub_category)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: StepTypeOrBuilderAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = StepTypeOrBuilderAllFields.from_dict(_all_fields)

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

        step_type_or_builder = cls(
            type_=type_,
            type_bytes=type_bytes,
            step_category_value=step_category_value,
            step_category=step_category,
            sub_category_value=sub_category_value,
            sub_category=sub_category,
            all_fields=all_fields,
            default_instance_for_type=default_instance_for_type,
            unknown_fields=unknown_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            initialized=initialized,
        )

        step_type_or_builder.additional_properties = d
        return step_type_or_builder

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
