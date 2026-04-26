from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.strategy_info_or_builder_metadata_case import (
    StrategyInfoOrBuilderMetadataCase,
    check_strategy_info_or_builder_metadata_case,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.for_metadata import ForMetadata
    from ..models.for_metadata_or_builder import ForMetadataOrBuilder
    from ..models.message import Message
    from ..models.strategy_info_or_builder_all_fields import StrategyInfoOrBuilderAllFields
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="StrategyInfoOrBuilder")


@_attrs_define
class StrategyInfoOrBuilder:
    """
    Attributes:
        current_iteration (int | Unset):
        total_iterations (int | Unset):
        for_metadata (ForMetadata | Unset):
        identifier_post_fix (str | Unset):
        for_metadata_or_builder (ForMetadataOrBuilder | Unset):
        identifier_post_fix_bytes (ByteString | Unset):
        metadata_case (StrategyInfoOrBuilderMetadataCase | Unset):
        all_fields (StrategyInfoOrBuilderAllFields | Unset):
        default_instance_for_type (Message | Unset):
        unknown_fields (UnknownFieldSet | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        initialized (bool | Unset):
    """

    current_iteration: int | Unset = UNSET
    total_iterations: int | Unset = UNSET
    for_metadata: ForMetadata | Unset = UNSET
    identifier_post_fix: str | Unset = UNSET
    for_metadata_or_builder: ForMetadataOrBuilder | Unset = UNSET
    identifier_post_fix_bytes: ByteString | Unset = UNSET
    metadata_case: StrategyInfoOrBuilderMetadataCase | Unset = UNSET
    all_fields: StrategyInfoOrBuilderAllFields | Unset = UNSET
    default_instance_for_type: Message | Unset = UNSET
    unknown_fields: UnknownFieldSet | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    initialized: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_iteration = self.current_iteration

        total_iterations = self.total_iterations

        for_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.for_metadata, Unset):
            for_metadata = self.for_metadata.to_dict()

        identifier_post_fix = self.identifier_post_fix

        for_metadata_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.for_metadata_or_builder, Unset):
            for_metadata_or_builder = self.for_metadata_or_builder.to_dict()

        identifier_post_fix_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifier_post_fix_bytes, Unset):
            identifier_post_fix_bytes = self.identifier_post_fix_bytes.to_dict()

        metadata_case: str | Unset = UNSET
        if not isinstance(self.metadata_case, Unset):
            metadata_case = self.metadata_case

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
        if current_iteration is not UNSET:
            field_dict["currentIteration"] = current_iteration
        if total_iterations is not UNSET:
            field_dict["totalIterations"] = total_iterations
        if for_metadata is not UNSET:
            field_dict["forMetadata"] = for_metadata
        if identifier_post_fix is not UNSET:
            field_dict["identifierPostFix"] = identifier_post_fix
        if for_metadata_or_builder is not UNSET:
            field_dict["forMetadataOrBuilder"] = for_metadata_or_builder
        if identifier_post_fix_bytes is not UNSET:
            field_dict["identifierPostFixBytes"] = identifier_post_fix_bytes
        if metadata_case is not UNSET:
            field_dict["metadataCase"] = metadata_case
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
        from ..models.for_metadata import ForMetadata
        from ..models.for_metadata_or_builder import ForMetadataOrBuilder
        from ..models.message import Message
        from ..models.strategy_info_or_builder_all_fields import StrategyInfoOrBuilderAllFields
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        current_iteration = d.pop("currentIteration", UNSET)

        total_iterations = d.pop("totalIterations", UNSET)

        _for_metadata = d.pop("forMetadata", UNSET)
        for_metadata: ForMetadata | Unset
        if isinstance(_for_metadata, Unset):
            for_metadata = UNSET
        else:
            for_metadata = ForMetadata.from_dict(_for_metadata)

        identifier_post_fix = d.pop("identifierPostFix", UNSET)

        _for_metadata_or_builder = d.pop("forMetadataOrBuilder", UNSET)
        for_metadata_or_builder: ForMetadataOrBuilder | Unset
        if isinstance(_for_metadata_or_builder, Unset):
            for_metadata_or_builder = UNSET
        else:
            for_metadata_or_builder = ForMetadataOrBuilder.from_dict(_for_metadata_or_builder)

        _identifier_post_fix_bytes = d.pop("identifierPostFixBytes", UNSET)
        identifier_post_fix_bytes: ByteString | Unset
        if isinstance(_identifier_post_fix_bytes, Unset):
            identifier_post_fix_bytes = UNSET
        else:
            identifier_post_fix_bytes = ByteString.from_dict(_identifier_post_fix_bytes)

        _metadata_case = d.pop("metadataCase", UNSET)
        metadata_case: StrategyInfoOrBuilderMetadataCase | Unset
        if isinstance(_metadata_case, Unset):
            metadata_case = UNSET
        else:
            metadata_case = check_strategy_info_or_builder_metadata_case(_metadata_case)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: StrategyInfoOrBuilderAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = StrategyInfoOrBuilderAllFields.from_dict(_all_fields)

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

        strategy_info_or_builder = cls(
            current_iteration=current_iteration,
            total_iterations=total_iterations,
            for_metadata=for_metadata,
            identifier_post_fix=identifier_post_fix,
            for_metadata_or_builder=for_metadata_or_builder,
            identifier_post_fix_bytes=identifier_post_fix_bytes,
            metadata_case=metadata_case,
            all_fields=all_fields,
            default_instance_for_type=default_instance_for_type,
            unknown_fields=unknown_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            initialized=initialized,
        )

        strategy_info_or_builder.additional_properties = d
        return strategy_info_or_builder

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
