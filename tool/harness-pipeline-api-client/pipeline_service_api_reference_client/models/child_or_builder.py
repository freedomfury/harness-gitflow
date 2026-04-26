from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.child_or_builder_all_fields import ChildOrBuilderAllFields
    from ..models.descriptor import Descriptor
    from ..models.message import Message
    from ..models.strategy_metadata import StrategyMetadata
    from ..models.strategy_metadata_or_builder import StrategyMetadataOrBuilder
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="ChildOrBuilder")


@_attrs_define
class ChildOrBuilder:
    """
    Attributes:
        strategy_metadata_or_builder (StrategyMetadataOrBuilder | Unset):
        child_node_id_bytes (ByteString | Unset):
        child_node_id (str | Unset):
        strategy_metadata (StrategyMetadata | Unset):
        all_fields (ChildOrBuilderAllFields | Unset):
        default_instance_for_type (Message | Unset):
        unknown_fields (UnknownFieldSet | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        initialized (bool | Unset):
    """

    strategy_metadata_or_builder: StrategyMetadataOrBuilder | Unset = UNSET
    child_node_id_bytes: ByteString | Unset = UNSET
    child_node_id: str | Unset = UNSET
    strategy_metadata: StrategyMetadata | Unset = UNSET
    all_fields: ChildOrBuilderAllFields | Unset = UNSET
    default_instance_for_type: Message | Unset = UNSET
    unknown_fields: UnknownFieldSet | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    initialized: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        strategy_metadata_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.strategy_metadata_or_builder, Unset):
            strategy_metadata_or_builder = self.strategy_metadata_or_builder.to_dict()

        child_node_id_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.child_node_id_bytes, Unset):
            child_node_id_bytes = self.child_node_id_bytes.to_dict()

        child_node_id = self.child_node_id

        strategy_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.strategy_metadata, Unset):
            strategy_metadata = self.strategy_metadata.to_dict()

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
        if strategy_metadata_or_builder is not UNSET:
            field_dict["strategyMetadataOrBuilder"] = strategy_metadata_or_builder
        if child_node_id_bytes is not UNSET:
            field_dict["childNodeIdBytes"] = child_node_id_bytes
        if child_node_id is not UNSET:
            field_dict["childNodeId"] = child_node_id
        if strategy_metadata is not UNSET:
            field_dict["strategyMetadata"] = strategy_metadata
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
        from ..models.child_or_builder_all_fields import ChildOrBuilderAllFields
        from ..models.descriptor import Descriptor
        from ..models.message import Message
        from ..models.strategy_metadata import StrategyMetadata
        from ..models.strategy_metadata_or_builder import StrategyMetadataOrBuilder
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _strategy_metadata_or_builder = d.pop("strategyMetadataOrBuilder", UNSET)
        strategy_metadata_or_builder: StrategyMetadataOrBuilder | Unset
        if isinstance(_strategy_metadata_or_builder, Unset):
            strategy_metadata_or_builder = UNSET
        else:
            strategy_metadata_or_builder = StrategyMetadataOrBuilder.from_dict(_strategy_metadata_or_builder)

        _child_node_id_bytes = d.pop("childNodeIdBytes", UNSET)
        child_node_id_bytes: ByteString | Unset
        if isinstance(_child_node_id_bytes, Unset):
            child_node_id_bytes = UNSET
        else:
            child_node_id_bytes = ByteString.from_dict(_child_node_id_bytes)

        child_node_id = d.pop("childNodeId", UNSET)

        _strategy_metadata = d.pop("strategyMetadata", UNSET)
        strategy_metadata: StrategyMetadata | Unset
        if isinstance(_strategy_metadata, Unset):
            strategy_metadata = UNSET
        else:
            strategy_metadata = StrategyMetadata.from_dict(_strategy_metadata)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: ChildOrBuilderAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = ChildOrBuilderAllFields.from_dict(_all_fields)

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

        child_or_builder = cls(
            strategy_metadata_or_builder=strategy_metadata_or_builder,
            child_node_id_bytes=child_node_id_bytes,
            child_node_id=child_node_id,
            strategy_metadata=strategy_metadata,
            all_fields=all_fields,
            default_instance_for_type=default_instance_for_type,
            unknown_fields=unknown_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            initialized=initialized,
        )

        child_or_builder.additional_properties = d
        return child_or_builder

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
