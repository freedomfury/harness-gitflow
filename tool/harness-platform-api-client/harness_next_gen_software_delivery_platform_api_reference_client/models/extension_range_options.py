from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.extension_range_options_verification import (
    ExtensionRangeOptionsVerification,
    check_extension_range_options_verification,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.declaration import Declaration
    from ..models.declaration_or_builder import DeclarationOrBuilder
    from ..models.descriptor import Descriptor
    from ..models.extension_range_options_all_fields import ExtensionRangeOptionsAllFields
    from ..models.extension_range_options_all_fields_raw import ExtensionRangeOptionsAllFieldsRaw
    from ..models.feature_set import FeatureSet
    from ..models.feature_set_or_builder import FeatureSetOrBuilder
    from ..models.parser_extension_range_options import ParserExtensionRangeOptions
    from ..models.uninterpreted_option import UninterpretedOption
    from ..models.uninterpreted_option_or_builder import UninterpretedOptionOrBuilder
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="ExtensionRangeOptions")


@_attrs_define
class ExtensionRangeOptions:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        features (FeatureSet | Unset):
        parser_for_type (ParserExtensionRangeOptions | Unset):
        serialized_size (int | Unset):
        declaration_list (list[Declaration] | Unset):
        declaration_count (int | Unset):
        declaration_or_builder_list (list[DeclarationOrBuilder] | Unset):
        verification (ExtensionRangeOptionsVerification | Unset):
        features_or_builder (FeatureSetOrBuilder | Unset):
        uninterpreted_option_list (list[UninterpretedOption] | Unset):
        uninterpreted_option_count (int | Unset):
        uninterpreted_option_or_builder_list (list[UninterpretedOptionOrBuilder] | Unset):
        default_instance_for_type (ExtensionRangeOptions | Unset):
        initialized (bool | Unset):
        all_fields (ExtensionRangeOptionsAllFields | Unset):
        all_fields_raw (ExtensionRangeOptionsAllFieldsRaw | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    features: FeatureSet | Unset = UNSET
    parser_for_type: ParserExtensionRangeOptions | Unset = UNSET
    serialized_size: int | Unset = UNSET
    declaration_list: list[Declaration] | Unset = UNSET
    declaration_count: int | Unset = UNSET
    declaration_or_builder_list: list[DeclarationOrBuilder] | Unset = UNSET
    verification: ExtensionRangeOptionsVerification | Unset = UNSET
    features_or_builder: FeatureSetOrBuilder | Unset = UNSET
    uninterpreted_option_list: list[UninterpretedOption] | Unset = UNSET
    uninterpreted_option_count: int | Unset = UNSET
    uninterpreted_option_or_builder_list: list[UninterpretedOptionOrBuilder] | Unset = UNSET
    default_instance_for_type: ExtensionRangeOptions | Unset = UNSET
    initialized: bool | Unset = UNSET
    all_fields: ExtensionRangeOptionsAllFields | Unset = UNSET
    all_fields_raw: ExtensionRangeOptionsAllFieldsRaw | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        features: dict[str, Any] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = self.features.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        declaration_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.declaration_list, Unset):
            declaration_list = []
            for declaration_list_item_data in self.declaration_list:
                declaration_list_item = declaration_list_item_data.to_dict()
                declaration_list.append(declaration_list_item)

        declaration_count = self.declaration_count

        declaration_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.declaration_or_builder_list, Unset):
            declaration_or_builder_list = []
            for declaration_or_builder_list_item_data in self.declaration_or_builder_list:
                declaration_or_builder_list_item = declaration_or_builder_list_item_data.to_dict()
                declaration_or_builder_list.append(declaration_or_builder_list_item)

        verification: str | Unset = UNSET
        if not isinstance(self.verification, Unset):
            verification = self.verification

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

        initialized = self.initialized

        all_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_fields, Unset):
            all_fields = self.all_fields.to_dict()

        all_fields_raw: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_fields_raw, Unset):
            all_fields_raw = self.all_fields_raw.to_dict()

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
        if features is not UNSET:
            field_dict["features"] = features
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if declaration_list is not UNSET:
            field_dict["declarationList"] = declaration_list
        if declaration_count is not UNSET:
            field_dict["declarationCount"] = declaration_count
        if declaration_or_builder_list is not UNSET:
            field_dict["declarationOrBuilderList"] = declaration_or_builder_list
        if verification is not UNSET:
            field_dict["verification"] = verification
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
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if all_fields is not UNSET:
            field_dict["allFields"] = all_fields
        if all_fields_raw is not UNSET:
            field_dict["allFieldsRaw"] = all_fields_raw
        if initialization_error_string is not UNSET:
            field_dict["initializationErrorString"] = initialization_error_string
        if descriptor_for_type is not UNSET:
            field_dict["descriptorForType"] = descriptor_for_type
        if memoized_serialized_size is not UNSET:
            field_dict["memoizedSerializedSize"] = memoized_serialized_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.declaration import Declaration
        from ..models.declaration_or_builder import DeclarationOrBuilder
        from ..models.descriptor import Descriptor
        from ..models.extension_range_options_all_fields import ExtensionRangeOptionsAllFields
        from ..models.extension_range_options_all_fields_raw import ExtensionRangeOptionsAllFieldsRaw
        from ..models.feature_set import FeatureSet
        from ..models.feature_set_or_builder import FeatureSetOrBuilder
        from ..models.parser_extension_range_options import ParserExtensionRangeOptions
        from ..models.uninterpreted_option import UninterpretedOption
        from ..models.uninterpreted_option_or_builder import UninterpretedOptionOrBuilder
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        _features = d.pop("features", UNSET)
        features: FeatureSet | Unset
        if isinstance(_features, Unset):
            features = UNSET
        else:
            features = FeatureSet.from_dict(_features)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserExtensionRangeOptions | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserExtensionRangeOptions.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _declaration_list = d.pop("declarationList", UNSET)
        declaration_list: list[Declaration] | Unset = UNSET
        if _declaration_list is not UNSET:
            declaration_list = []
            for declaration_list_item_data in _declaration_list:
                declaration_list_item = Declaration.from_dict(declaration_list_item_data)

                declaration_list.append(declaration_list_item)

        declaration_count = d.pop("declarationCount", UNSET)

        _declaration_or_builder_list = d.pop("declarationOrBuilderList", UNSET)
        declaration_or_builder_list: list[DeclarationOrBuilder] | Unset = UNSET
        if _declaration_or_builder_list is not UNSET:
            declaration_or_builder_list = []
            for declaration_or_builder_list_item_data in _declaration_or_builder_list:
                declaration_or_builder_list_item = DeclarationOrBuilder.from_dict(declaration_or_builder_list_item_data)

                declaration_or_builder_list.append(declaration_or_builder_list_item)

        _verification = d.pop("verification", UNSET)
        verification: ExtensionRangeOptionsVerification | Unset
        if isinstance(_verification, Unset):
            verification = UNSET
        else:
            verification = check_extension_range_options_verification(_verification)

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
        default_instance_for_type: ExtensionRangeOptions | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = ExtensionRangeOptions.from_dict(_default_instance_for_type)

        initialized = d.pop("initialized", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: ExtensionRangeOptionsAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = ExtensionRangeOptionsAllFields.from_dict(_all_fields)

        _all_fields_raw = d.pop("allFieldsRaw", UNSET)
        all_fields_raw: ExtensionRangeOptionsAllFieldsRaw | Unset
        if isinstance(_all_fields_raw, Unset):
            all_fields_raw = UNSET
        else:
            all_fields_raw = ExtensionRangeOptionsAllFieldsRaw.from_dict(_all_fields_raw)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        extension_range_options = cls(
            unknown_fields=unknown_fields,
            features=features,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            declaration_list=declaration_list,
            declaration_count=declaration_count,
            declaration_or_builder_list=declaration_or_builder_list,
            verification=verification,
            features_or_builder=features_or_builder,
            uninterpreted_option_list=uninterpreted_option_list,
            uninterpreted_option_count=uninterpreted_option_count,
            uninterpreted_option_or_builder_list=uninterpreted_option_or_builder_list,
            default_instance_for_type=default_instance_for_type,
            initialized=initialized,
            all_fields=all_fields,
            all_fields_raw=all_fields_raw,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        extension_range_options.additional_properties = d
        return extension_range_options

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
