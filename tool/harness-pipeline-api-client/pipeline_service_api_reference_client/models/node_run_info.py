from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.expression_block import ExpressionBlock
    from ..models.expression_block_or_builder import ExpressionBlockOrBuilder
    from ..models.node_run_info_all_fields import NodeRunInfoAllFields
    from ..models.parser_node_run_info import ParserNodeRunInfo
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="NodeRunInfo")


@_attrs_define
class NodeRunInfo:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        initialized (bool | Unset):
        default_instance_for_type (NodeRunInfo | Unset):
        parser_for_type (ParserNodeRunInfo | Unset):
        serialized_size (int | Unset):
        evaluated_condition (bool | Unset):
        when_condition_bytes (ByteString | Unset):
        expressions_list (list[ExpressionBlock] | Unset):
        expressions_count (int | Unset):
        expressions_or_builder_list (list[ExpressionBlockOrBuilder] | Unset):
        is_manual_execution (bool | Unset):
        when_condition (str | Unset):
        all_fields (NodeRunInfoAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    initialized: bool | Unset = UNSET
    default_instance_for_type: NodeRunInfo | Unset = UNSET
    parser_for_type: ParserNodeRunInfo | Unset = UNSET
    serialized_size: int | Unset = UNSET
    evaluated_condition: bool | Unset = UNSET
    when_condition_bytes: ByteString | Unset = UNSET
    expressions_list: list[ExpressionBlock] | Unset = UNSET
    expressions_count: int | Unset = UNSET
    expressions_or_builder_list: list[ExpressionBlockOrBuilder] | Unset = UNSET
    is_manual_execution: bool | Unset = UNSET
    when_condition: str | Unset = UNSET
    all_fields: NodeRunInfoAllFields | Unset = UNSET
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

        evaluated_condition = self.evaluated_condition

        when_condition_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.when_condition_bytes, Unset):
            when_condition_bytes = self.when_condition_bytes.to_dict()

        expressions_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.expressions_list, Unset):
            expressions_list = []
            for expressions_list_item_data in self.expressions_list:
                expressions_list_item = expressions_list_item_data.to_dict()
                expressions_list.append(expressions_list_item)

        expressions_count = self.expressions_count

        expressions_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.expressions_or_builder_list, Unset):
            expressions_or_builder_list = []
            for expressions_or_builder_list_item_data in self.expressions_or_builder_list:
                expressions_or_builder_list_item = expressions_or_builder_list_item_data.to_dict()
                expressions_or_builder_list.append(expressions_or_builder_list_item)

        is_manual_execution = self.is_manual_execution

        when_condition = self.when_condition

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
        if evaluated_condition is not UNSET:
            field_dict["evaluatedCondition"] = evaluated_condition
        if when_condition_bytes is not UNSET:
            field_dict["whenConditionBytes"] = when_condition_bytes
        if expressions_list is not UNSET:
            field_dict["expressionsList"] = expressions_list
        if expressions_count is not UNSET:
            field_dict["expressionsCount"] = expressions_count
        if expressions_or_builder_list is not UNSET:
            field_dict["expressionsOrBuilderList"] = expressions_or_builder_list
        if is_manual_execution is not UNSET:
            field_dict["isManualExecution"] = is_manual_execution
        if when_condition is not UNSET:
            field_dict["whenCondition"] = when_condition
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
        from ..models.expression_block import ExpressionBlock
        from ..models.expression_block_or_builder import ExpressionBlockOrBuilder
        from ..models.node_run_info_all_fields import NodeRunInfoAllFields
        from ..models.parser_node_run_info import ParserNodeRunInfo
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
        default_instance_for_type: NodeRunInfo | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = NodeRunInfo.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserNodeRunInfo | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserNodeRunInfo.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        evaluated_condition = d.pop("evaluatedCondition", UNSET)

        _when_condition_bytes = d.pop("whenConditionBytes", UNSET)
        when_condition_bytes: ByteString | Unset
        if isinstance(_when_condition_bytes, Unset):
            when_condition_bytes = UNSET
        else:
            when_condition_bytes = ByteString.from_dict(_when_condition_bytes)

        _expressions_list = d.pop("expressionsList", UNSET)
        expressions_list: list[ExpressionBlock] | Unset = UNSET
        if _expressions_list is not UNSET:
            expressions_list = []
            for expressions_list_item_data in _expressions_list:
                expressions_list_item = ExpressionBlock.from_dict(expressions_list_item_data)

                expressions_list.append(expressions_list_item)

        expressions_count = d.pop("expressionsCount", UNSET)

        _expressions_or_builder_list = d.pop("expressionsOrBuilderList", UNSET)
        expressions_or_builder_list: list[ExpressionBlockOrBuilder] | Unset = UNSET
        if _expressions_or_builder_list is not UNSET:
            expressions_or_builder_list = []
            for expressions_or_builder_list_item_data in _expressions_or_builder_list:
                expressions_or_builder_list_item = ExpressionBlockOrBuilder.from_dict(
                    expressions_or_builder_list_item_data
                )

                expressions_or_builder_list.append(expressions_or_builder_list_item)

        is_manual_execution = d.pop("isManualExecution", UNSET)

        when_condition = d.pop("whenCondition", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: NodeRunInfoAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = NodeRunInfoAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        node_run_info = cls(
            unknown_fields=unknown_fields,
            initialized=initialized,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            evaluated_condition=evaluated_condition,
            when_condition_bytes=when_condition_bytes,
            expressions_list=expressions_list,
            expressions_count=expressions_count,
            expressions_or_builder_list=expressions_or_builder_list,
            is_manual_execution=is_manual_execution,
            when_condition=when_condition,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        node_run_info.additional_properties = d
        return node_run_info

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
