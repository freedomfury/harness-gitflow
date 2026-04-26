from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.level_all_fields import LevelAllFields
    from ..models.parser_level import ParserLevel
    from ..models.step_type import StepType
    from ..models.step_type_or_builder import StepTypeOrBuilder
    from ..models.strategy_info import StrategyInfo
    from ..models.strategy_info_or_builder import StrategyInfoOrBuilder
    from ..models.strategy_metadata import StrategyMetadata
    from ..models.strategy_metadata_or_builder import StrategyMetadataOrBuilder
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="Level")


@_attrs_define
class Level:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        skip_expression_chain (bool | Unset):
        setup_id (str | Unset):
        runtime_id_bytes (ByteString | Unset):
        retry_index (int | Unset):
        setup_id_bytes (ByteString | Unset):
        node_type_bytes (ByteString | Unset):
        strategy_metadata_or_builder (StrategyMetadataOrBuilder | Unset):
        original_identifier_bytes (ByteString | Unset):
        strategy_info (StrategyInfo | Unset):
        strategy_info_or_builder (StrategyInfoOrBuilder | Unset):
        initialized (bool | Unset):
        identifier (str | Unset):
        original_identifier (str | Unset):
        group (str | Unset):
        node_type (str | Unset):
        step_type_or_builder (StepTypeOrBuilder | Unset):
        group_bytes (ByteString | Unset):
        default_instance_for_type (Level | Unset):
        parser_for_type (ParserLevel | Unset):
        serialized_size (int | Unset):
        identifier_bytes (ByteString | Unset):
        start_ts (int | Unset):
        strategy_metadata (StrategyMetadata | Unset):
        step_type (StepType | Unset):
        runtime_id (str | Unset):
        all_fields (LevelAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    skip_expression_chain: bool | Unset = UNSET
    setup_id: str | Unset = UNSET
    runtime_id_bytes: ByteString | Unset = UNSET
    retry_index: int | Unset = UNSET
    setup_id_bytes: ByteString | Unset = UNSET
    node_type_bytes: ByteString | Unset = UNSET
    strategy_metadata_or_builder: StrategyMetadataOrBuilder | Unset = UNSET
    original_identifier_bytes: ByteString | Unset = UNSET
    strategy_info: StrategyInfo | Unset = UNSET
    strategy_info_or_builder: StrategyInfoOrBuilder | Unset = UNSET
    initialized: bool | Unset = UNSET
    identifier: str | Unset = UNSET
    original_identifier: str | Unset = UNSET
    group: str | Unset = UNSET
    node_type: str | Unset = UNSET
    step_type_or_builder: StepTypeOrBuilder | Unset = UNSET
    group_bytes: ByteString | Unset = UNSET
    default_instance_for_type: Level | Unset = UNSET
    parser_for_type: ParserLevel | Unset = UNSET
    serialized_size: int | Unset = UNSET
    identifier_bytes: ByteString | Unset = UNSET
    start_ts: int | Unset = UNSET
    strategy_metadata: StrategyMetadata | Unset = UNSET
    step_type: StepType | Unset = UNSET
    runtime_id: str | Unset = UNSET
    all_fields: LevelAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        skip_expression_chain = self.skip_expression_chain

        setup_id = self.setup_id

        runtime_id_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.runtime_id_bytes, Unset):
            runtime_id_bytes = self.runtime_id_bytes.to_dict()

        retry_index = self.retry_index

        setup_id_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.setup_id_bytes, Unset):
            setup_id_bytes = self.setup_id_bytes.to_dict()

        node_type_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.node_type_bytes, Unset):
            node_type_bytes = self.node_type_bytes.to_dict()

        strategy_metadata_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.strategy_metadata_or_builder, Unset):
            strategy_metadata_or_builder = self.strategy_metadata_or_builder.to_dict()

        original_identifier_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.original_identifier_bytes, Unset):
            original_identifier_bytes = self.original_identifier_bytes.to_dict()

        strategy_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.strategy_info, Unset):
            strategy_info = self.strategy_info.to_dict()

        strategy_info_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.strategy_info_or_builder, Unset):
            strategy_info_or_builder = self.strategy_info_or_builder.to_dict()

        initialized = self.initialized

        identifier = self.identifier

        original_identifier = self.original_identifier

        group = self.group

        node_type = self.node_type

        step_type_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.step_type_or_builder, Unset):
            step_type_or_builder = self.step_type_or_builder.to_dict()

        group_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group_bytes, Unset):
            group_bytes = self.group_bytes.to_dict()

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        identifier_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifier_bytes, Unset):
            identifier_bytes = self.identifier_bytes.to_dict()

        start_ts = self.start_ts

        strategy_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.strategy_metadata, Unset):
            strategy_metadata = self.strategy_metadata.to_dict()

        step_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.step_type, Unset):
            step_type = self.step_type.to_dict()

        runtime_id = self.runtime_id

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
        if skip_expression_chain is not UNSET:
            field_dict["skipExpressionChain"] = skip_expression_chain
        if setup_id is not UNSET:
            field_dict["setupId"] = setup_id
        if runtime_id_bytes is not UNSET:
            field_dict["runtimeIdBytes"] = runtime_id_bytes
        if retry_index is not UNSET:
            field_dict["retryIndex"] = retry_index
        if setup_id_bytes is not UNSET:
            field_dict["setupIdBytes"] = setup_id_bytes
        if node_type_bytes is not UNSET:
            field_dict["nodeTypeBytes"] = node_type_bytes
        if strategy_metadata_or_builder is not UNSET:
            field_dict["strategyMetadataOrBuilder"] = strategy_metadata_or_builder
        if original_identifier_bytes is not UNSET:
            field_dict["originalIdentifierBytes"] = original_identifier_bytes
        if strategy_info is not UNSET:
            field_dict["strategyInfo"] = strategy_info
        if strategy_info_or_builder is not UNSET:
            field_dict["strategyInfoOrBuilder"] = strategy_info_or_builder
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if original_identifier is not UNSET:
            field_dict["originalIdentifier"] = original_identifier
        if group is not UNSET:
            field_dict["group"] = group
        if node_type is not UNSET:
            field_dict["nodeType"] = node_type
        if step_type_or_builder is not UNSET:
            field_dict["stepTypeOrBuilder"] = step_type_or_builder
        if group_bytes is not UNSET:
            field_dict["groupBytes"] = group_bytes
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if identifier_bytes is not UNSET:
            field_dict["identifierBytes"] = identifier_bytes
        if start_ts is not UNSET:
            field_dict["startTs"] = start_ts
        if strategy_metadata is not UNSET:
            field_dict["strategyMetadata"] = strategy_metadata
        if step_type is not UNSET:
            field_dict["stepType"] = step_type
        if runtime_id is not UNSET:
            field_dict["runtimeId"] = runtime_id
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
        from ..models.level_all_fields import LevelAllFields
        from ..models.parser_level import ParserLevel
        from ..models.step_type import StepType
        from ..models.step_type_or_builder import StepTypeOrBuilder
        from ..models.strategy_info import StrategyInfo
        from ..models.strategy_info_or_builder import StrategyInfoOrBuilder
        from ..models.strategy_metadata import StrategyMetadata
        from ..models.strategy_metadata_or_builder import StrategyMetadataOrBuilder
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        skip_expression_chain = d.pop("skipExpressionChain", UNSET)

        setup_id = d.pop("setupId", UNSET)

        _runtime_id_bytes = d.pop("runtimeIdBytes", UNSET)
        runtime_id_bytes: ByteString | Unset
        if isinstance(_runtime_id_bytes, Unset):
            runtime_id_bytes = UNSET
        else:
            runtime_id_bytes = ByteString.from_dict(_runtime_id_bytes)

        retry_index = d.pop("retryIndex", UNSET)

        _setup_id_bytes = d.pop("setupIdBytes", UNSET)
        setup_id_bytes: ByteString | Unset
        if isinstance(_setup_id_bytes, Unset):
            setup_id_bytes = UNSET
        else:
            setup_id_bytes = ByteString.from_dict(_setup_id_bytes)

        _node_type_bytes = d.pop("nodeTypeBytes", UNSET)
        node_type_bytes: ByteString | Unset
        if isinstance(_node_type_bytes, Unset):
            node_type_bytes = UNSET
        else:
            node_type_bytes = ByteString.from_dict(_node_type_bytes)

        _strategy_metadata_or_builder = d.pop("strategyMetadataOrBuilder", UNSET)
        strategy_metadata_or_builder: StrategyMetadataOrBuilder | Unset
        if isinstance(_strategy_metadata_or_builder, Unset):
            strategy_metadata_or_builder = UNSET
        else:
            strategy_metadata_or_builder = StrategyMetadataOrBuilder.from_dict(_strategy_metadata_or_builder)

        _original_identifier_bytes = d.pop("originalIdentifierBytes", UNSET)
        original_identifier_bytes: ByteString | Unset
        if isinstance(_original_identifier_bytes, Unset):
            original_identifier_bytes = UNSET
        else:
            original_identifier_bytes = ByteString.from_dict(_original_identifier_bytes)

        _strategy_info = d.pop("strategyInfo", UNSET)
        strategy_info: StrategyInfo | Unset
        if isinstance(_strategy_info, Unset):
            strategy_info = UNSET
        else:
            strategy_info = StrategyInfo.from_dict(_strategy_info)

        _strategy_info_or_builder = d.pop("strategyInfoOrBuilder", UNSET)
        strategy_info_or_builder: StrategyInfoOrBuilder | Unset
        if isinstance(_strategy_info_or_builder, Unset):
            strategy_info_or_builder = UNSET
        else:
            strategy_info_or_builder = StrategyInfoOrBuilder.from_dict(_strategy_info_or_builder)

        initialized = d.pop("initialized", UNSET)

        identifier = d.pop("identifier", UNSET)

        original_identifier = d.pop("originalIdentifier", UNSET)

        group = d.pop("group", UNSET)

        node_type = d.pop("nodeType", UNSET)

        _step_type_or_builder = d.pop("stepTypeOrBuilder", UNSET)
        step_type_or_builder: StepTypeOrBuilder | Unset
        if isinstance(_step_type_or_builder, Unset):
            step_type_or_builder = UNSET
        else:
            step_type_or_builder = StepTypeOrBuilder.from_dict(_step_type_or_builder)

        _group_bytes = d.pop("groupBytes", UNSET)
        group_bytes: ByteString | Unset
        if isinstance(_group_bytes, Unset):
            group_bytes = UNSET
        else:
            group_bytes = ByteString.from_dict(_group_bytes)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: Level | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = Level.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserLevel | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserLevel.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _identifier_bytes = d.pop("identifierBytes", UNSET)
        identifier_bytes: ByteString | Unset
        if isinstance(_identifier_bytes, Unset):
            identifier_bytes = UNSET
        else:
            identifier_bytes = ByteString.from_dict(_identifier_bytes)

        start_ts = d.pop("startTs", UNSET)

        _strategy_metadata = d.pop("strategyMetadata", UNSET)
        strategy_metadata: StrategyMetadata | Unset
        if isinstance(_strategy_metadata, Unset):
            strategy_metadata = UNSET
        else:
            strategy_metadata = StrategyMetadata.from_dict(_strategy_metadata)

        _step_type = d.pop("stepType", UNSET)
        step_type: StepType | Unset
        if isinstance(_step_type, Unset):
            step_type = UNSET
        else:
            step_type = StepType.from_dict(_step_type)

        runtime_id = d.pop("runtimeId", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: LevelAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = LevelAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        level = cls(
            unknown_fields=unknown_fields,
            skip_expression_chain=skip_expression_chain,
            setup_id=setup_id,
            runtime_id_bytes=runtime_id_bytes,
            retry_index=retry_index,
            setup_id_bytes=setup_id_bytes,
            node_type_bytes=node_type_bytes,
            strategy_metadata_or_builder=strategy_metadata_or_builder,
            original_identifier_bytes=original_identifier_bytes,
            strategy_info=strategy_info,
            strategy_info_or_builder=strategy_info_or_builder,
            initialized=initialized,
            identifier=identifier,
            original_identifier=original_identifier,
            group=group,
            node_type=node_type,
            step_type_or_builder=step_type_or_builder,
            group_bytes=group_bytes,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            identifier_bytes=identifier_bytes,
            start_ts=start_ts,
            strategy_metadata=strategy_metadata,
            step_type=step_type,
            runtime_id=runtime_id,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        level.additional_properties = d
        return level

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
