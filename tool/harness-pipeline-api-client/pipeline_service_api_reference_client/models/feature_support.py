from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.feature_support_edition_deprecated import (
    FeatureSupportEditionDeprecated,
    check_feature_support_edition_deprecated,
)
from ..models.feature_support_edition_introduced import (
    FeatureSupportEditionIntroduced,
    check_feature_support_edition_introduced,
)
from ..models.feature_support_edition_removed import FeatureSupportEditionRemoved, check_feature_support_edition_removed
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.feature_support_all_fields import FeatureSupportAllFields
    from ..models.parser_feature_support import ParserFeatureSupport
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="FeatureSupport")


@_attrs_define
class FeatureSupport:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        initialized (bool | Unset):
        default_instance_for_type (FeatureSupport | Unset):
        parser_for_type (ParserFeatureSupport | Unset):
        serialized_size (int | Unset):
        edition_introduced (FeatureSupportEditionIntroduced | Unset):
        edition_deprecated (FeatureSupportEditionDeprecated | Unset):
        deprecation_warning (str | Unset):
        deprecation_warning_bytes (ByteString | Unset):
        edition_removed (FeatureSupportEditionRemoved | Unset):
        all_fields (FeatureSupportAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    initialized: bool | Unset = UNSET
    default_instance_for_type: FeatureSupport | Unset = UNSET
    parser_for_type: ParserFeatureSupport | Unset = UNSET
    serialized_size: int | Unset = UNSET
    edition_introduced: FeatureSupportEditionIntroduced | Unset = UNSET
    edition_deprecated: FeatureSupportEditionDeprecated | Unset = UNSET
    deprecation_warning: str | Unset = UNSET
    deprecation_warning_bytes: ByteString | Unset = UNSET
    edition_removed: FeatureSupportEditionRemoved | Unset = UNSET
    all_fields: FeatureSupportAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        initialized = self.initialized

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        edition_introduced: str | Unset = UNSET
        if not isinstance(self.edition_introduced, Unset):
            edition_introduced = self.edition_introduced

        edition_deprecated: str | Unset = UNSET
        if not isinstance(self.edition_deprecated, Unset):
            edition_deprecated = self.edition_deprecated

        deprecation_warning = self.deprecation_warning

        deprecation_warning_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deprecation_warning_bytes, Unset):
            deprecation_warning_bytes = self.deprecation_warning_bytes.to_dict()

        edition_removed: str | Unset = UNSET
        if not isinstance(self.edition_removed, Unset):
            edition_removed = self.edition_removed

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
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if edition_introduced is not UNSET:
            field_dict["editionIntroduced"] = edition_introduced
        if edition_deprecated is not UNSET:
            field_dict["editionDeprecated"] = edition_deprecated
        if deprecation_warning is not UNSET:
            field_dict["deprecationWarning"] = deprecation_warning
        if deprecation_warning_bytes is not UNSET:
            field_dict["deprecationWarningBytes"] = deprecation_warning_bytes
        if edition_removed is not UNSET:
            field_dict["editionRemoved"] = edition_removed
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
        from ..models.feature_support_all_fields import FeatureSupportAllFields
        from ..models.parser_feature_support import ParserFeatureSupport
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        initialized = d.pop("initialized", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: FeatureSupport | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = FeatureSupport.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserFeatureSupport | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserFeatureSupport.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _edition_introduced = d.pop("editionIntroduced", UNSET)
        edition_introduced: FeatureSupportEditionIntroduced | Unset
        if isinstance(_edition_introduced, Unset):
            edition_introduced = UNSET
        else:
            edition_introduced = check_feature_support_edition_introduced(_edition_introduced)

        _edition_deprecated = d.pop("editionDeprecated", UNSET)
        edition_deprecated: FeatureSupportEditionDeprecated | Unset
        if isinstance(_edition_deprecated, Unset):
            edition_deprecated = UNSET
        else:
            edition_deprecated = check_feature_support_edition_deprecated(_edition_deprecated)

        deprecation_warning = d.pop("deprecationWarning", UNSET)

        _deprecation_warning_bytes = d.pop("deprecationWarningBytes", UNSET)
        deprecation_warning_bytes: ByteString | Unset
        if isinstance(_deprecation_warning_bytes, Unset):
            deprecation_warning_bytes = UNSET
        else:
            deprecation_warning_bytes = ByteString.from_dict(_deprecation_warning_bytes)

        _edition_removed = d.pop("editionRemoved", UNSET)
        edition_removed: FeatureSupportEditionRemoved | Unset
        if isinstance(_edition_removed, Unset):
            edition_removed = UNSET
        else:
            edition_removed = check_feature_support_edition_removed(_edition_removed)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: FeatureSupportAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = FeatureSupportAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        feature_support = cls(
            unknown_fields=unknown_fields,
            initialized=initialized,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            edition_introduced=edition_introduced,
            edition_deprecated=edition_deprecated,
            deprecation_warning=deprecation_warning,
            deprecation_warning_bytes=deprecation_warning_bytes,
            edition_removed=edition_removed,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        feature_support.additional_properties = d
        return feature_support

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
