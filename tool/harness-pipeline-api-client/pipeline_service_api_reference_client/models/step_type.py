from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.step_type_step_category import StepTypeStepCategory, check_step_type_step_category
from ..models.step_type_sub_category import StepTypeSubCategory, check_step_type_sub_category
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.parser_step_type import ParserStepType
    from ..models.step_type_all_fields import StepTypeAllFields
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="StepType")


@_attrs_define
class StepType:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        type_ (str | Unset):
        initialized (bool | Unset):
        default_instance_for_type (StepType | Unset):
        parser_for_type (ParserStepType | Unset):
        serialized_size (int | Unset):
        type_bytes (ByteString | Unset):
        step_category_value (int | Unset):
        step_category (StepTypeStepCategory | Unset):
        sub_category_value (int | Unset):
        sub_category (StepTypeSubCategory | Unset):
        all_fields (StepTypeAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    type_: str | Unset = UNSET
    initialized: bool | Unset = UNSET
    default_instance_for_type: StepType | Unset = UNSET
    parser_for_type: ParserStepType | Unset = UNSET
    serialized_size: int | Unset = UNSET
    type_bytes: ByteString | Unset = UNSET
    step_category_value: int | Unset = UNSET
    step_category: StepTypeStepCategory | Unset = UNSET
    sub_category_value: int | Unset = UNSET
    sub_category: StepTypeSubCategory | Unset = UNSET
    all_fields: StepTypeAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        type_ = self.type_

        initialized = self.initialized

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

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
        if type_ is not UNSET:
            field_dict["type"] = type_
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
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
        from ..models.parser_step_type import ParserStepType
        from ..models.step_type_all_fields import StepTypeAllFields
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        type_ = d.pop("type", UNSET)

        initialized = d.pop("initialized", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: StepType | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = StepType.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserStepType | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserStepType.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _type_bytes = d.pop("typeBytes", UNSET)
        type_bytes: ByteString | Unset
        if isinstance(_type_bytes, Unset):
            type_bytes = UNSET
        else:
            type_bytes = ByteString.from_dict(_type_bytes)

        step_category_value = d.pop("stepCategoryValue", UNSET)

        _step_category = d.pop("stepCategory", UNSET)
        step_category: StepTypeStepCategory | Unset
        if isinstance(_step_category, Unset):
            step_category = UNSET
        else:
            step_category = check_step_type_step_category(_step_category)

        sub_category_value = d.pop("subCategoryValue", UNSET)

        _sub_category = d.pop("subCategory", UNSET)
        sub_category: StepTypeSubCategory | Unset
        if isinstance(_sub_category, Unset):
            sub_category = UNSET
        else:
            sub_category = check_step_type_sub_category(_sub_category)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: StepTypeAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = StepTypeAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        step_type = cls(
            unknown_fields=unknown_fields,
            type_=type_,
            initialized=initialized,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            type_bytes=type_bytes,
            step_category_value=step_category_value,
            step_category=step_category,
            sub_category_value=sub_category_value,
            sub_category=sub_category,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        step_type.additional_properties = d
        return step_type

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
