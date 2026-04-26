from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.field_options_ctype import FieldOptionsCtype, check_field_options_ctype
from ..models.field_options_jstype import FieldOptionsJstype, check_field_options_jstype
from ..models.field_options_retention import FieldOptionsRetention, check_field_options_retention
from ..models.field_options_targets_list_item import FieldOptionsTargetsListItem, check_field_options_targets_list_item
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.descriptor import Descriptor
    from ..models.edition_default import EditionDefault
    from ..models.edition_default_or_builder import EditionDefaultOrBuilder
    from ..models.feature_set import FeatureSet
    from ..models.feature_set_or_builder import FeatureSetOrBuilder
    from ..models.feature_support import FeatureSupport
    from ..models.feature_support_or_builder import FeatureSupportOrBuilder
    from ..models.field_options_all_fields import FieldOptionsAllFields
    from ..models.field_options_all_fields_raw import FieldOptionsAllFieldsRaw
    from ..models.parser_field_options import ParserFieldOptions
    from ..models.uninterpreted_option import UninterpretedOption
    from ..models.uninterpreted_option_or_builder import UninterpretedOptionOrBuilder
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="FieldOptions")


@_attrs_define
class FieldOptions:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        initialized (bool | Unset):
        retention (FieldOptionsRetention | Unset):
        features (FeatureSet | Unset):
        default_instance_for_type (FieldOptions | Unset):
        parser_for_type (ParserFieldOptions | Unset):
        serialized_size (int | Unset):
        deprecated (bool | Unset):
        features_or_builder (FeatureSetOrBuilder | Unset):
        uninterpreted_option_list (list[UninterpretedOption] | Unset):
        uninterpreted_option_count (int | Unset):
        uninterpreted_option_or_builder_list (list[UninterpretedOptionOrBuilder] | Unset):
        packed (bool | Unset):
        targets_count (int | Unset):
        edition_defaults_list (list[EditionDefault] | Unset):
        edition_defaults_count (int | Unset):
        edition_defaults_or_builder_list (list[EditionDefaultOrBuilder] | Unset):
        feature_support (FeatureSupport | Unset):
        feature_support_or_builder (FeatureSupportOrBuilder | Unset):
        ctype (FieldOptionsCtype | Unset):
        jstype (FieldOptionsJstype | Unset):
        lazy (bool | Unset):
        unverified_lazy (bool | Unset):
        weak (bool | Unset):
        debug_redact (bool | Unset):
        targets_list (list[FieldOptionsTargetsListItem] | Unset):
        all_fields (FieldOptionsAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        all_fields_raw (FieldOptionsAllFieldsRaw | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    initialized: bool | Unset = UNSET
    retention: FieldOptionsRetention | Unset = UNSET
    features: FeatureSet | Unset = UNSET
    default_instance_for_type: FieldOptions | Unset = UNSET
    parser_for_type: ParserFieldOptions | Unset = UNSET
    serialized_size: int | Unset = UNSET
    deprecated: bool | Unset = UNSET
    features_or_builder: FeatureSetOrBuilder | Unset = UNSET
    uninterpreted_option_list: list[UninterpretedOption] | Unset = UNSET
    uninterpreted_option_count: int | Unset = UNSET
    uninterpreted_option_or_builder_list: list[UninterpretedOptionOrBuilder] | Unset = UNSET
    packed: bool | Unset = UNSET
    targets_count: int | Unset = UNSET
    edition_defaults_list: list[EditionDefault] | Unset = UNSET
    edition_defaults_count: int | Unset = UNSET
    edition_defaults_or_builder_list: list[EditionDefaultOrBuilder] | Unset = UNSET
    feature_support: FeatureSupport | Unset = UNSET
    feature_support_or_builder: FeatureSupportOrBuilder | Unset = UNSET
    ctype: FieldOptionsCtype | Unset = UNSET
    jstype: FieldOptionsJstype | Unset = UNSET
    lazy: bool | Unset = UNSET
    unverified_lazy: bool | Unset = UNSET
    weak: bool | Unset = UNSET
    debug_redact: bool | Unset = UNSET
    targets_list: list[FieldOptionsTargetsListItem] | Unset = UNSET
    all_fields: FieldOptionsAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    all_fields_raw: FieldOptionsAllFieldsRaw | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        initialized = self.initialized

        retention: str | Unset = UNSET
        if not isinstance(self.retention, Unset):
            retention = self.retention

        features: dict[str, Any] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = self.features.to_dict()

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        deprecated = self.deprecated

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

        packed = self.packed

        targets_count = self.targets_count

        edition_defaults_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.edition_defaults_list, Unset):
            edition_defaults_list = []
            for edition_defaults_list_item_data in self.edition_defaults_list:
                edition_defaults_list_item = edition_defaults_list_item_data.to_dict()
                edition_defaults_list.append(edition_defaults_list_item)

        edition_defaults_count = self.edition_defaults_count

        edition_defaults_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.edition_defaults_or_builder_list, Unset):
            edition_defaults_or_builder_list = []
            for edition_defaults_or_builder_list_item_data in self.edition_defaults_or_builder_list:
                edition_defaults_or_builder_list_item = edition_defaults_or_builder_list_item_data.to_dict()
                edition_defaults_or_builder_list.append(edition_defaults_or_builder_list_item)

        feature_support: dict[str, Any] | Unset = UNSET
        if not isinstance(self.feature_support, Unset):
            feature_support = self.feature_support.to_dict()

        feature_support_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.feature_support_or_builder, Unset):
            feature_support_or_builder = self.feature_support_or_builder.to_dict()

        ctype: str | Unset = UNSET
        if not isinstance(self.ctype, Unset):
            ctype = self.ctype

        jstype: str | Unset = UNSET
        if not isinstance(self.jstype, Unset):
            jstype = self.jstype

        lazy = self.lazy

        unverified_lazy = self.unverified_lazy

        weak = self.weak

        debug_redact = self.debug_redact

        targets_list: list[str] | Unset = UNSET
        if not isinstance(self.targets_list, Unset):
            targets_list = []
            for targets_list_item_data in self.targets_list:
                targets_list_item: str = targets_list_item_data
                targets_list.append(targets_list_item)

        all_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_fields, Unset):
            all_fields = self.all_fields.to_dict()

        initialization_error_string = self.initialization_error_string

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
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if retention is not UNSET:
            field_dict["retention"] = retention
        if features is not UNSET:
            field_dict["features"] = features
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if deprecated is not UNSET:
            field_dict["deprecated"] = deprecated
        if features_or_builder is not UNSET:
            field_dict["featuresOrBuilder"] = features_or_builder
        if uninterpreted_option_list is not UNSET:
            field_dict["uninterpretedOptionList"] = uninterpreted_option_list
        if uninterpreted_option_count is not UNSET:
            field_dict["uninterpretedOptionCount"] = uninterpreted_option_count
        if uninterpreted_option_or_builder_list is not UNSET:
            field_dict["uninterpretedOptionOrBuilderList"] = uninterpreted_option_or_builder_list
        if packed is not UNSET:
            field_dict["packed"] = packed
        if targets_count is not UNSET:
            field_dict["targetsCount"] = targets_count
        if edition_defaults_list is not UNSET:
            field_dict["editionDefaultsList"] = edition_defaults_list
        if edition_defaults_count is not UNSET:
            field_dict["editionDefaultsCount"] = edition_defaults_count
        if edition_defaults_or_builder_list is not UNSET:
            field_dict["editionDefaultsOrBuilderList"] = edition_defaults_or_builder_list
        if feature_support is not UNSET:
            field_dict["featureSupport"] = feature_support
        if feature_support_or_builder is not UNSET:
            field_dict["featureSupportOrBuilder"] = feature_support_or_builder
        if ctype is not UNSET:
            field_dict["ctype"] = ctype
        if jstype is not UNSET:
            field_dict["jstype"] = jstype
        if lazy is not UNSET:
            field_dict["lazy"] = lazy
        if unverified_lazy is not UNSET:
            field_dict["unverifiedLazy"] = unverified_lazy
        if weak is not UNSET:
            field_dict["weak"] = weak
        if debug_redact is not UNSET:
            field_dict["debugRedact"] = debug_redact
        if targets_list is not UNSET:
            field_dict["targetsList"] = targets_list
        if all_fields is not UNSET:
            field_dict["allFields"] = all_fields
        if initialization_error_string is not UNSET:
            field_dict["initializationErrorString"] = initialization_error_string
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
        from ..models.edition_default import EditionDefault
        from ..models.edition_default_or_builder import EditionDefaultOrBuilder
        from ..models.feature_set import FeatureSet
        from ..models.feature_set_or_builder import FeatureSetOrBuilder
        from ..models.feature_support import FeatureSupport
        from ..models.feature_support_or_builder import FeatureSupportOrBuilder
        from ..models.field_options_all_fields import FieldOptionsAllFields
        from ..models.field_options_all_fields_raw import FieldOptionsAllFieldsRaw
        from ..models.parser_field_options import ParserFieldOptions
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

        initialized = d.pop("initialized", UNSET)

        _retention = d.pop("retention", UNSET)
        retention: FieldOptionsRetention | Unset
        if isinstance(_retention, Unset):
            retention = UNSET
        else:
            retention = check_field_options_retention(_retention)

        _features = d.pop("features", UNSET)
        features: FeatureSet | Unset
        if isinstance(_features, Unset):
            features = UNSET
        else:
            features = FeatureSet.from_dict(_features)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: FieldOptions | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = FieldOptions.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserFieldOptions | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserFieldOptions.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        deprecated = d.pop("deprecated", UNSET)

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

        packed = d.pop("packed", UNSET)

        targets_count = d.pop("targetsCount", UNSET)

        _edition_defaults_list = d.pop("editionDefaultsList", UNSET)
        edition_defaults_list: list[EditionDefault] | Unset = UNSET
        if _edition_defaults_list is not UNSET:
            edition_defaults_list = []
            for edition_defaults_list_item_data in _edition_defaults_list:
                edition_defaults_list_item = EditionDefault.from_dict(edition_defaults_list_item_data)

                edition_defaults_list.append(edition_defaults_list_item)

        edition_defaults_count = d.pop("editionDefaultsCount", UNSET)

        _edition_defaults_or_builder_list = d.pop("editionDefaultsOrBuilderList", UNSET)
        edition_defaults_or_builder_list: list[EditionDefaultOrBuilder] | Unset = UNSET
        if _edition_defaults_or_builder_list is not UNSET:
            edition_defaults_or_builder_list = []
            for edition_defaults_or_builder_list_item_data in _edition_defaults_or_builder_list:
                edition_defaults_or_builder_list_item = EditionDefaultOrBuilder.from_dict(
                    edition_defaults_or_builder_list_item_data
                )

                edition_defaults_or_builder_list.append(edition_defaults_or_builder_list_item)

        _feature_support = d.pop("featureSupport", UNSET)
        feature_support: FeatureSupport | Unset
        if isinstance(_feature_support, Unset):
            feature_support = UNSET
        else:
            feature_support = FeatureSupport.from_dict(_feature_support)

        _feature_support_or_builder = d.pop("featureSupportOrBuilder", UNSET)
        feature_support_or_builder: FeatureSupportOrBuilder | Unset
        if isinstance(_feature_support_or_builder, Unset):
            feature_support_or_builder = UNSET
        else:
            feature_support_or_builder = FeatureSupportOrBuilder.from_dict(_feature_support_or_builder)

        _ctype = d.pop("ctype", UNSET)
        ctype: FieldOptionsCtype | Unset
        if isinstance(_ctype, Unset):
            ctype = UNSET
        else:
            ctype = check_field_options_ctype(_ctype)

        _jstype = d.pop("jstype", UNSET)
        jstype: FieldOptionsJstype | Unset
        if isinstance(_jstype, Unset):
            jstype = UNSET
        else:
            jstype = check_field_options_jstype(_jstype)

        lazy = d.pop("lazy", UNSET)

        unverified_lazy = d.pop("unverifiedLazy", UNSET)

        weak = d.pop("weak", UNSET)

        debug_redact = d.pop("debugRedact", UNSET)

        _targets_list = d.pop("targetsList", UNSET)
        targets_list: list[FieldOptionsTargetsListItem] | Unset = UNSET
        if _targets_list is not UNSET:
            targets_list = []
            for targets_list_item_data in _targets_list:
                targets_list_item = check_field_options_targets_list_item(targets_list_item_data)

                targets_list.append(targets_list_item)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: FieldOptionsAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = FieldOptionsAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        _all_fields_raw = d.pop("allFieldsRaw", UNSET)
        all_fields_raw: FieldOptionsAllFieldsRaw | Unset
        if isinstance(_all_fields_raw, Unset):
            all_fields_raw = UNSET
        else:
            all_fields_raw = FieldOptionsAllFieldsRaw.from_dict(_all_fields_raw)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        field_options = cls(
            unknown_fields=unknown_fields,
            initialized=initialized,
            retention=retention,
            features=features,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            deprecated=deprecated,
            features_or_builder=features_or_builder,
            uninterpreted_option_list=uninterpreted_option_list,
            uninterpreted_option_count=uninterpreted_option_count,
            uninterpreted_option_or_builder_list=uninterpreted_option_or_builder_list,
            packed=packed,
            targets_count=targets_count,
            edition_defaults_list=edition_defaults_list,
            edition_defaults_count=edition_defaults_count,
            edition_defaults_or_builder_list=edition_defaults_or_builder_list,
            feature_support=feature_support,
            feature_support_or_builder=feature_support_or_builder,
            ctype=ctype,
            jstype=jstype,
            lazy=lazy,
            unverified_lazy=unverified_lazy,
            weak=weak,
            debug_redact=debug_redact,
            targets_list=targets_list,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            all_fields_raw=all_fields_raw,
            memoized_serialized_size=memoized_serialized_size,
        )

        field_options.additional_properties = d
        return field_options

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
