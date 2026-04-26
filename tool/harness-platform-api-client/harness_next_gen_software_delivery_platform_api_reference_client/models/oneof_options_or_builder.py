from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.descriptor import Descriptor
    from ..models.feature_set import FeatureSet
    from ..models.feature_set_or_builder import FeatureSetOrBuilder
    from ..models.message import Message
    from ..models.oneof_options_or_builder_all_fields import OneofOptionsOrBuilderAllFields
    from ..models.uninterpreted_option import UninterpretedOption
    from ..models.uninterpreted_option_or_builder import UninterpretedOptionOrBuilder
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="OneofOptionsOrBuilder")


@_attrs_define
class OneofOptionsOrBuilder:
    """
    Attributes:
        features (FeatureSet | Unset):
        features_or_builder (FeatureSetOrBuilder | Unset):
        uninterpreted_option_list (list[UninterpretedOption] | Unset):
        uninterpreted_option_count (int | Unset):
        uninterpreted_option_or_builder_list (list[UninterpretedOptionOrBuilder] | Unset):
        default_instance_for_type (Message | Unset):
        initialization_error_string (str | Unset):
        all_fields (OneofOptionsOrBuilderAllFields | Unset):
        unknown_fields (UnknownFieldSet | Unset):
        descriptor_for_type (Descriptor | Unset):
        initialized (bool | Unset):
    """

    features: FeatureSet | Unset = UNSET
    features_or_builder: FeatureSetOrBuilder | Unset = UNSET
    uninterpreted_option_list: list[UninterpretedOption] | Unset = UNSET
    uninterpreted_option_count: int | Unset = UNSET
    uninterpreted_option_or_builder_list: list[UninterpretedOptionOrBuilder] | Unset = UNSET
    default_instance_for_type: Message | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    all_fields: OneofOptionsOrBuilderAllFields | Unset = UNSET
    unknown_fields: UnknownFieldSet | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    initialized: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        features: dict[str, Any] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = self.features.to_dict()

        features_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.features_or_builder, Unset):
            features_or_builder = self.features_or_builder.to_dict()

        uninterpreted_option_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.uninterpreted_option_list, Unset):
            uninterpreted_option_list = []
            for uninterpreted_option_list_item_data in self.uninterpreted_option_list:
                uninterpreted_option_list_item = uninterpreted_option_list_item_data.to_dict()
                uninterpreted_option_list.append(uninterpreted_option_list_item)

        uninterpreted_option_count = self.uninterpreted_option_count

        uninterpreted_option_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.uninterpreted_option_or_builder_list, Unset):
            uninterpreted_option_or_builder_list = []
            for uninterpreted_option_or_builder_list_item_data in self.uninterpreted_option_or_builder_list:
                uninterpreted_option_or_builder_list_item = uninterpreted_option_or_builder_list_item_data.to_dict()
                uninterpreted_option_or_builder_list.append(uninterpreted_option_or_builder_list_item)

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

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

        initialized = self.initialized

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if features is not UNSET:
            field_dict["features"] = features
        if features_or_builder is not UNSET:
            field_dict["featuresOrBuilder"] = features_or_builder
        if uninterpreted_option_list is not UNSET:
            field_dict["uninterpretedOptionList"] = uninterpreted_option_list
        if uninterpreted_option_count is not UNSET:
            field_dict["uninterpretedOptionCount"] = uninterpreted_option_count
        if uninterpreted_option_or_builder_list is not UNSET:
            field_dict["uninterpretedOptionOrBuilderList"] = uninterpreted_option_or_builder_list
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if initialization_error_string is not UNSET:
            field_dict["initializationErrorString"] = initialization_error_string
        if all_fields is not UNSET:
            field_dict["allFields"] = all_fields
        if unknown_fields is not UNSET:
            field_dict["unknownFields"] = unknown_fields
        if descriptor_for_type is not UNSET:
            field_dict["descriptorForType"] = descriptor_for_type
        if initialized is not UNSET:
            field_dict["initialized"] = initialized

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.descriptor import Descriptor
        from ..models.feature_set import FeatureSet
        from ..models.feature_set_or_builder import FeatureSetOrBuilder
        from ..models.message import Message
        from ..models.oneof_options_or_builder_all_fields import OneofOptionsOrBuilderAllFields
        from ..models.uninterpreted_option import UninterpretedOption
        from ..models.uninterpreted_option_or_builder import UninterpretedOptionOrBuilder
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _features = d.pop("features", UNSET)
        features: FeatureSet | Unset
        if isinstance(_features, Unset):
            features = UNSET
        else:
            features = FeatureSet.from_dict(_features)

        _features_or_builder = d.pop("featuresOrBuilder", UNSET)
        features_or_builder: FeatureSetOrBuilder | Unset
        if isinstance(_features_or_builder, Unset):
            features_or_builder = UNSET
        else:
            features_or_builder = FeatureSetOrBuilder.from_dict(_features_or_builder)

        _uninterpreted_option_list = d.pop("uninterpretedOptionList", UNSET)
        uninterpreted_option_list: list[UninterpretedOption] | Unset = UNSET
        if _uninterpreted_option_list is not UNSET:
            uninterpreted_option_list = []
            for uninterpreted_option_list_item_data in _uninterpreted_option_list:
                uninterpreted_option_list_item = UninterpretedOption.from_dict(uninterpreted_option_list_item_data)

                uninterpreted_option_list.append(uninterpreted_option_list_item)

        uninterpreted_option_count = d.pop("uninterpretedOptionCount", UNSET)

        _uninterpreted_option_or_builder_list = d.pop("uninterpretedOptionOrBuilderList", UNSET)
        uninterpreted_option_or_builder_list: list[UninterpretedOptionOrBuilder] | Unset = UNSET
        if _uninterpreted_option_or_builder_list is not UNSET:
            uninterpreted_option_or_builder_list = []
            for uninterpreted_option_or_builder_list_item_data in _uninterpreted_option_or_builder_list:
                uninterpreted_option_or_builder_list_item = UninterpretedOptionOrBuilder.from_dict(
                    uninterpreted_option_or_builder_list_item_data
                )

                uninterpreted_option_or_builder_list.append(uninterpreted_option_or_builder_list_item)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: Message | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = Message.from_dict(_default_instance_for_type)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: OneofOptionsOrBuilderAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = OneofOptionsOrBuilderAllFields.from_dict(_all_fields)

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

        initialized = d.pop("initialized", UNSET)

        oneof_options_or_builder = cls(
            features=features,
            features_or_builder=features_or_builder,
            uninterpreted_option_list=uninterpreted_option_list,
            uninterpreted_option_count=uninterpreted_option_count,
            uninterpreted_option_or_builder_list=uninterpreted_option_or_builder_list,
            default_instance_for_type=default_instance_for_type,
            initialization_error_string=initialization_error_string,
            all_fields=all_fields,
            unknown_fields=unknown_fields,
            descriptor_for_type=descriptor_for_type,
            initialized=initialized,
        )

        oneof_options_or_builder.additional_properties = d
        return oneof_options_or_builder

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
