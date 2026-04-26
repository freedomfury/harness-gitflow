from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_options_or_builder_optimize_for import (
    FileOptionsOrBuilderOptimizeFor,
    check_file_options_or_builder_optimize_for,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.feature_set import FeatureSet
    from ..models.feature_set_or_builder import FeatureSetOrBuilder
    from ..models.file_options_or_builder_all_fields import FileOptionsOrBuilderAllFields
    from ..models.message import Message
    from ..models.uninterpreted_option import UninterpretedOption
    from ..models.uninterpreted_option_or_builder import UninterpretedOptionOrBuilder
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="FileOptionsOrBuilder")


@_attrs_define
class FileOptionsOrBuilder:
    """
    Attributes:
        features (FeatureSet | Unset):
        java_string_check_utf_8 (bool | Unset):
        java_package_bytes (ByteString | Unset):
        java_outer_classname (str | Unset):
        java_outer_classname_bytes (ByteString | Unset):
        java_multiple_files (bool | Unset):
        java_generate_equals_and_hash (bool | Unset):
        optimize_for (FileOptionsOrBuilderOptimizeFor | Unset):
        go_package (str | Unset):
        go_package_bytes (ByteString | Unset):
        java_package (str | Unset):
        cc_generic_services (bool | Unset):
        java_generic_services (bool | Unset):
        py_generic_services (bool | Unset):
        deprecated (bool | Unset):
        cc_enable_arenas (bool | Unset):
        objc_class_prefix (str | Unset):
        objc_class_prefix_bytes (ByteString | Unset):
        csharp_namespace (str | Unset):
        csharp_namespace_bytes (ByteString | Unset):
        swift_prefix (str | Unset):
        swift_prefix_bytes (ByteString | Unset):
        php_class_prefix (str | Unset):
        php_class_prefix_bytes (ByteString | Unset):
        php_namespace (str | Unset):
        php_namespace_bytes (ByteString | Unset):
        php_metadata_namespace (str | Unset):
        php_metadata_namespace_bytes (ByteString | Unset):
        ruby_package (str | Unset):
        ruby_package_bytes (ByteString | Unset):
        features_or_builder (FeatureSetOrBuilder | Unset):
        uninterpreted_option_list (list[UninterpretedOption] | Unset):
        uninterpreted_option_count (int | Unset):
        uninterpreted_option_or_builder_list (list[UninterpretedOptionOrBuilder] | Unset):
        default_instance_for_type (Message | Unset):
        all_fields (FileOptionsOrBuilderAllFields | Unset):
        unknown_fields (UnknownFieldSet | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        initialized (bool | Unset):
    """

    features: FeatureSet | Unset = UNSET
    java_string_check_utf_8: bool | Unset = UNSET
    java_package_bytes: ByteString | Unset = UNSET
    java_outer_classname: str | Unset = UNSET
    java_outer_classname_bytes: ByteString | Unset = UNSET
    java_multiple_files: bool | Unset = UNSET
    java_generate_equals_and_hash: bool | Unset = UNSET
    optimize_for: FileOptionsOrBuilderOptimizeFor | Unset = UNSET
    go_package: str | Unset = UNSET
    go_package_bytes: ByteString | Unset = UNSET
    java_package: str | Unset = UNSET
    cc_generic_services: bool | Unset = UNSET
    java_generic_services: bool | Unset = UNSET
    py_generic_services: bool | Unset = UNSET
    deprecated: bool | Unset = UNSET
    cc_enable_arenas: bool | Unset = UNSET
    objc_class_prefix: str | Unset = UNSET
    objc_class_prefix_bytes: ByteString | Unset = UNSET
    csharp_namespace: str | Unset = UNSET
    csharp_namespace_bytes: ByteString | Unset = UNSET
    swift_prefix: str | Unset = UNSET
    swift_prefix_bytes: ByteString | Unset = UNSET
    php_class_prefix: str | Unset = UNSET
    php_class_prefix_bytes: ByteString | Unset = UNSET
    php_namespace: str | Unset = UNSET
    php_namespace_bytes: ByteString | Unset = UNSET
    php_metadata_namespace: str | Unset = UNSET
    php_metadata_namespace_bytes: ByteString | Unset = UNSET
    ruby_package: str | Unset = UNSET
    ruby_package_bytes: ByteString | Unset = UNSET
    features_or_builder: FeatureSetOrBuilder | Unset = UNSET
    uninterpreted_option_list: list[UninterpretedOption] | Unset = UNSET
    uninterpreted_option_count: int | Unset = UNSET
    uninterpreted_option_or_builder_list: list[UninterpretedOptionOrBuilder] | Unset = UNSET
    default_instance_for_type: Message | Unset = UNSET
    all_fields: FileOptionsOrBuilderAllFields | Unset = UNSET
    unknown_fields: UnknownFieldSet | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    initialized: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        features: dict[str, Any] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = self.features.to_dict()

        java_string_check_utf_8 = self.java_string_check_utf_8

        java_package_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.java_package_bytes, Unset):
            java_package_bytes = self.java_package_bytes.to_dict()

        java_outer_classname = self.java_outer_classname

        java_outer_classname_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.java_outer_classname_bytes, Unset):
            java_outer_classname_bytes = self.java_outer_classname_bytes.to_dict()

        java_multiple_files = self.java_multiple_files

        java_generate_equals_and_hash = self.java_generate_equals_and_hash

        optimize_for: str | Unset = UNSET
        if not isinstance(self.optimize_for, Unset):
            optimize_for = self.optimize_for

        go_package = self.go_package

        go_package_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.go_package_bytes, Unset):
            go_package_bytes = self.go_package_bytes.to_dict()

        java_package = self.java_package

        cc_generic_services = self.cc_generic_services

        java_generic_services = self.java_generic_services

        py_generic_services = self.py_generic_services

        deprecated = self.deprecated

        cc_enable_arenas = self.cc_enable_arenas

        objc_class_prefix = self.objc_class_prefix

        objc_class_prefix_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.objc_class_prefix_bytes, Unset):
            objc_class_prefix_bytes = self.objc_class_prefix_bytes.to_dict()

        csharp_namespace = self.csharp_namespace

        csharp_namespace_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.csharp_namespace_bytes, Unset):
            csharp_namespace_bytes = self.csharp_namespace_bytes.to_dict()

        swift_prefix = self.swift_prefix

        swift_prefix_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.swift_prefix_bytes, Unset):
            swift_prefix_bytes = self.swift_prefix_bytes.to_dict()

        php_class_prefix = self.php_class_prefix

        php_class_prefix_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.php_class_prefix_bytes, Unset):
            php_class_prefix_bytes = self.php_class_prefix_bytes.to_dict()

        php_namespace = self.php_namespace

        php_namespace_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.php_namespace_bytes, Unset):
            php_namespace_bytes = self.php_namespace_bytes.to_dict()

        php_metadata_namespace = self.php_metadata_namespace

        php_metadata_namespace_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.php_metadata_namespace_bytes, Unset):
            php_metadata_namespace_bytes = self.php_metadata_namespace_bytes.to_dict()

        ruby_package = self.ruby_package

        ruby_package_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ruby_package_bytes, Unset):
            ruby_package_bytes = self.ruby_package_bytes.to_dict()

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
        if features is not UNSET:
            field_dict["features"] = features
        if java_string_check_utf_8 is not UNSET:
            field_dict["javaStringCheckUtf8"] = java_string_check_utf_8
        if java_package_bytes is not UNSET:
            field_dict["javaPackageBytes"] = java_package_bytes
        if java_outer_classname is not UNSET:
            field_dict["javaOuterClassname"] = java_outer_classname
        if java_outer_classname_bytes is not UNSET:
            field_dict["javaOuterClassnameBytes"] = java_outer_classname_bytes
        if java_multiple_files is not UNSET:
            field_dict["javaMultipleFiles"] = java_multiple_files
        if java_generate_equals_and_hash is not UNSET:
            field_dict["javaGenerateEqualsAndHash"] = java_generate_equals_and_hash
        if optimize_for is not UNSET:
            field_dict["optimizeFor"] = optimize_for
        if go_package is not UNSET:
            field_dict["goPackage"] = go_package
        if go_package_bytes is not UNSET:
            field_dict["goPackageBytes"] = go_package_bytes
        if java_package is not UNSET:
            field_dict["javaPackage"] = java_package
        if cc_generic_services is not UNSET:
            field_dict["ccGenericServices"] = cc_generic_services
        if java_generic_services is not UNSET:
            field_dict["javaGenericServices"] = java_generic_services
        if py_generic_services is not UNSET:
            field_dict["pyGenericServices"] = py_generic_services
        if deprecated is not UNSET:
            field_dict["deprecated"] = deprecated
        if cc_enable_arenas is not UNSET:
            field_dict["ccEnableArenas"] = cc_enable_arenas
        if objc_class_prefix is not UNSET:
            field_dict["objcClassPrefix"] = objc_class_prefix
        if objc_class_prefix_bytes is not UNSET:
            field_dict["objcClassPrefixBytes"] = objc_class_prefix_bytes
        if csharp_namespace is not UNSET:
            field_dict["csharpNamespace"] = csharp_namespace
        if csharp_namespace_bytes is not UNSET:
            field_dict["csharpNamespaceBytes"] = csharp_namespace_bytes
        if swift_prefix is not UNSET:
            field_dict["swiftPrefix"] = swift_prefix
        if swift_prefix_bytes is not UNSET:
            field_dict["swiftPrefixBytes"] = swift_prefix_bytes
        if php_class_prefix is not UNSET:
            field_dict["phpClassPrefix"] = php_class_prefix
        if php_class_prefix_bytes is not UNSET:
            field_dict["phpClassPrefixBytes"] = php_class_prefix_bytes
        if php_namespace is not UNSET:
            field_dict["phpNamespace"] = php_namespace
        if php_namespace_bytes is not UNSET:
            field_dict["phpNamespaceBytes"] = php_namespace_bytes
        if php_metadata_namespace is not UNSET:
            field_dict["phpMetadataNamespace"] = php_metadata_namespace
        if php_metadata_namespace_bytes is not UNSET:
            field_dict["phpMetadataNamespaceBytes"] = php_metadata_namespace_bytes
        if ruby_package is not UNSET:
            field_dict["rubyPackage"] = ruby_package
        if ruby_package_bytes is not UNSET:
            field_dict["rubyPackageBytes"] = ruby_package_bytes
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
        from ..models.byte_string import ByteString
        from ..models.descriptor import Descriptor
        from ..models.feature_set import FeatureSet
        from ..models.feature_set_or_builder import FeatureSetOrBuilder
        from ..models.file_options_or_builder_all_fields import FileOptionsOrBuilderAllFields
        from ..models.message import Message
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

        java_string_check_utf_8 = d.pop("javaStringCheckUtf8", UNSET)

        _java_package_bytes = d.pop("javaPackageBytes", UNSET)
        java_package_bytes: ByteString | Unset
        if isinstance(_java_package_bytes, Unset):
            java_package_bytes = UNSET
        else:
            java_package_bytes = ByteString.from_dict(_java_package_bytes)

        java_outer_classname = d.pop("javaOuterClassname", UNSET)

        _java_outer_classname_bytes = d.pop("javaOuterClassnameBytes", UNSET)
        java_outer_classname_bytes: ByteString | Unset
        if isinstance(_java_outer_classname_bytes, Unset):
            java_outer_classname_bytes = UNSET
        else:
            java_outer_classname_bytes = ByteString.from_dict(_java_outer_classname_bytes)

        java_multiple_files = d.pop("javaMultipleFiles", UNSET)

        java_generate_equals_and_hash = d.pop("javaGenerateEqualsAndHash", UNSET)

        _optimize_for = d.pop("optimizeFor", UNSET)
        optimize_for: FileOptionsOrBuilderOptimizeFor | Unset
        if isinstance(_optimize_for, Unset):
            optimize_for = UNSET
        else:
            optimize_for = check_file_options_or_builder_optimize_for(_optimize_for)

        go_package = d.pop("goPackage", UNSET)

        _go_package_bytes = d.pop("goPackageBytes", UNSET)
        go_package_bytes: ByteString | Unset
        if isinstance(_go_package_bytes, Unset):
            go_package_bytes = UNSET
        else:
            go_package_bytes = ByteString.from_dict(_go_package_bytes)

        java_package = d.pop("javaPackage", UNSET)

        cc_generic_services = d.pop("ccGenericServices", UNSET)

        java_generic_services = d.pop("javaGenericServices", UNSET)

        py_generic_services = d.pop("pyGenericServices", UNSET)

        deprecated = d.pop("deprecated", UNSET)

        cc_enable_arenas = d.pop("ccEnableArenas", UNSET)

        objc_class_prefix = d.pop("objcClassPrefix", UNSET)

        _objc_class_prefix_bytes = d.pop("objcClassPrefixBytes", UNSET)
        objc_class_prefix_bytes: ByteString | Unset
        if isinstance(_objc_class_prefix_bytes, Unset):
            objc_class_prefix_bytes = UNSET
        else:
            objc_class_prefix_bytes = ByteString.from_dict(_objc_class_prefix_bytes)

        csharp_namespace = d.pop("csharpNamespace", UNSET)

        _csharp_namespace_bytes = d.pop("csharpNamespaceBytes", UNSET)
        csharp_namespace_bytes: ByteString | Unset
        if isinstance(_csharp_namespace_bytes, Unset):
            csharp_namespace_bytes = UNSET
        else:
            csharp_namespace_bytes = ByteString.from_dict(_csharp_namespace_bytes)

        swift_prefix = d.pop("swiftPrefix", UNSET)

        _swift_prefix_bytes = d.pop("swiftPrefixBytes", UNSET)
        swift_prefix_bytes: ByteString | Unset
        if isinstance(_swift_prefix_bytes, Unset):
            swift_prefix_bytes = UNSET
        else:
            swift_prefix_bytes = ByteString.from_dict(_swift_prefix_bytes)

        php_class_prefix = d.pop("phpClassPrefix", UNSET)

        _php_class_prefix_bytes = d.pop("phpClassPrefixBytes", UNSET)
        php_class_prefix_bytes: ByteString | Unset
        if isinstance(_php_class_prefix_bytes, Unset):
            php_class_prefix_bytes = UNSET
        else:
            php_class_prefix_bytes = ByteString.from_dict(_php_class_prefix_bytes)

        php_namespace = d.pop("phpNamespace", UNSET)

        _php_namespace_bytes = d.pop("phpNamespaceBytes", UNSET)
        php_namespace_bytes: ByteString | Unset
        if isinstance(_php_namespace_bytes, Unset):
            php_namespace_bytes = UNSET
        else:
            php_namespace_bytes = ByteString.from_dict(_php_namespace_bytes)

        php_metadata_namespace = d.pop("phpMetadataNamespace", UNSET)

        _php_metadata_namespace_bytes = d.pop("phpMetadataNamespaceBytes", UNSET)
        php_metadata_namespace_bytes: ByteString | Unset
        if isinstance(_php_metadata_namespace_bytes, Unset):
            php_metadata_namespace_bytes = UNSET
        else:
            php_metadata_namespace_bytes = ByteString.from_dict(_php_metadata_namespace_bytes)

        ruby_package = d.pop("rubyPackage", UNSET)

        _ruby_package_bytes = d.pop("rubyPackageBytes", UNSET)
        ruby_package_bytes: ByteString | Unset
        if isinstance(_ruby_package_bytes, Unset):
            ruby_package_bytes = UNSET
        else:
            ruby_package_bytes = ByteString.from_dict(_ruby_package_bytes)

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

        _all_fields = d.pop("allFields", UNSET)
        all_fields: FileOptionsOrBuilderAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = FileOptionsOrBuilderAllFields.from_dict(_all_fields)

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

        file_options_or_builder = cls(
            features=features,
            java_string_check_utf_8=java_string_check_utf_8,
            java_package_bytes=java_package_bytes,
            java_outer_classname=java_outer_classname,
            java_outer_classname_bytes=java_outer_classname_bytes,
            java_multiple_files=java_multiple_files,
            java_generate_equals_and_hash=java_generate_equals_and_hash,
            optimize_for=optimize_for,
            go_package=go_package,
            go_package_bytes=go_package_bytes,
            java_package=java_package,
            cc_generic_services=cc_generic_services,
            java_generic_services=java_generic_services,
            py_generic_services=py_generic_services,
            deprecated=deprecated,
            cc_enable_arenas=cc_enable_arenas,
            objc_class_prefix=objc_class_prefix,
            objc_class_prefix_bytes=objc_class_prefix_bytes,
            csharp_namespace=csharp_namespace,
            csharp_namespace_bytes=csharp_namespace_bytes,
            swift_prefix=swift_prefix,
            swift_prefix_bytes=swift_prefix_bytes,
            php_class_prefix=php_class_prefix,
            php_class_prefix_bytes=php_class_prefix_bytes,
            php_namespace=php_namespace,
            php_namespace_bytes=php_namespace_bytes,
            php_metadata_namespace=php_metadata_namespace,
            php_metadata_namespace_bytes=php_metadata_namespace_bytes,
            ruby_package=ruby_package,
            ruby_package_bytes=ruby_package_bytes,
            features_or_builder=features_or_builder,
            uninterpreted_option_list=uninterpreted_option_list,
            uninterpreted_option_count=uninterpreted_option_count,
            uninterpreted_option_or_builder_list=uninterpreted_option_or_builder_list,
            default_instance_for_type=default_instance_for_type,
            all_fields=all_fields,
            unknown_fields=unknown_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            initialized=initialized,
        )

        file_options_or_builder.additional_properties = d
        return file_options_or_builder

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
