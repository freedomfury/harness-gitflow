from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.executable_response_response_case import (
    ExecutableResponseResponseCase,
    check_executable_response_response_case,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.async_chain_executable_response import AsyncChainExecutableResponse
    from ..models.async_chain_executable_response_or_builder import AsyncChainExecutableResponseOrBuilder
    from ..models.async_executable_response import AsyncExecutableResponse
    from ..models.async_executable_response_or_builder import AsyncExecutableResponseOrBuilder
    from ..models.child_chain_executable_response import ChildChainExecutableResponse
    from ..models.child_chain_executable_response_or_builder import ChildChainExecutableResponseOrBuilder
    from ..models.child_executable_response import ChildExecutableResponse
    from ..models.child_executable_response_or_builder import ChildExecutableResponseOrBuilder
    from ..models.children_executable_response import ChildrenExecutableResponse
    from ..models.children_executable_response_or_builder import ChildrenExecutableResponseOrBuilder
    from ..models.descriptor import Descriptor
    from ..models.executable_response_all_fields import ExecutableResponseAllFields
    from ..models.facilitator_executable_response import FacilitatorExecutableResponse
    from ..models.facilitator_executable_response_or_builder import FacilitatorExecutableResponseOrBuilder
    from ..models.parser_executable_response import ParserExecutableResponse
    from ..models.skip_task_executable_response import SkipTaskExecutableResponse
    from ..models.skip_task_executable_response_or_builder import SkipTaskExecutableResponseOrBuilder
    from ..models.sync_executable_response import SyncExecutableResponse
    from ..models.sync_executable_response_or_builder import SyncExecutableResponseOrBuilder
    from ..models.task_chain_executable_response import TaskChainExecutableResponse
    from ..models.task_chain_executable_response_or_builder import TaskChainExecutableResponseOrBuilder
    from ..models.task_executable_response import TaskExecutableResponse
    from ..models.task_executable_response_or_builder import TaskExecutableResponseOrBuilder
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="ExecutableResponse")


@_attrs_define
class ExecutableResponse:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        child (ChildExecutableResponse | Unset):
        children (ChildrenExecutableResponse | Unset):
        initialized (bool | Unset):
        task (TaskExecutableResponse | Unset):
        async_ (AsyncExecutableResponse | Unset):
        default_instance_for_type (ExecutableResponse | Unset):
        parser_for_type (ParserExecutableResponse | Unset):
        serialized_size (int | Unset):
        task_chain (TaskChainExecutableResponse | Unset):
        task_chain_or_builder (TaskChainExecutableResponseOrBuilder | Unset):
        sync (SyncExecutableResponse | Unset):
        sync_or_builder (SyncExecutableResponseOrBuilder | Unset):
        skip_task (SkipTaskExecutableResponse | Unset):
        skip_task_or_builder (SkipTaskExecutableResponseOrBuilder | Unset):
        async_chain (AsyncChainExecutableResponse | Unset):
        async_chain_or_builder (AsyncChainExecutableResponseOrBuilder | Unset):
        facilitator (FacilitatorExecutableResponse | Unset):
        facilitator_or_builder (FacilitatorExecutableResponseOrBuilder | Unset):
        response_case (ExecutableResponseResponseCase | Unset):
        async_or_builder (AsyncExecutableResponseOrBuilder | Unset):
        child_or_builder (ChildExecutableResponseOrBuilder | Unset):
        children_or_builder (ChildrenExecutableResponseOrBuilder | Unset):
        child_chain (ChildChainExecutableResponse | Unset):
        child_chain_or_builder (ChildChainExecutableResponseOrBuilder | Unset):
        task_or_builder (TaskExecutableResponseOrBuilder | Unset):
        all_fields (ExecutableResponseAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    child: ChildExecutableResponse | Unset = UNSET
    children: ChildrenExecutableResponse | Unset = UNSET
    initialized: bool | Unset = UNSET
    task: TaskExecutableResponse | Unset = UNSET
    async_: AsyncExecutableResponse | Unset = UNSET
    default_instance_for_type: ExecutableResponse | Unset = UNSET
    parser_for_type: ParserExecutableResponse | Unset = UNSET
    serialized_size: int | Unset = UNSET
    task_chain: TaskChainExecutableResponse | Unset = UNSET
    task_chain_or_builder: TaskChainExecutableResponseOrBuilder | Unset = UNSET
    sync: SyncExecutableResponse | Unset = UNSET
    sync_or_builder: SyncExecutableResponseOrBuilder | Unset = UNSET
    skip_task: SkipTaskExecutableResponse | Unset = UNSET
    skip_task_or_builder: SkipTaskExecutableResponseOrBuilder | Unset = UNSET
    async_chain: AsyncChainExecutableResponse | Unset = UNSET
    async_chain_or_builder: AsyncChainExecutableResponseOrBuilder | Unset = UNSET
    facilitator: FacilitatorExecutableResponse | Unset = UNSET
    facilitator_or_builder: FacilitatorExecutableResponseOrBuilder | Unset = UNSET
    response_case: ExecutableResponseResponseCase | Unset = UNSET
    async_or_builder: AsyncExecutableResponseOrBuilder | Unset = UNSET
    child_or_builder: ChildExecutableResponseOrBuilder | Unset = UNSET
    children_or_builder: ChildrenExecutableResponseOrBuilder | Unset = UNSET
    child_chain: ChildChainExecutableResponse | Unset = UNSET
    child_chain_or_builder: ChildChainExecutableResponseOrBuilder | Unset = UNSET
    task_or_builder: TaskExecutableResponseOrBuilder | Unset = UNSET
    all_fields: ExecutableResponseAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        child: dict[str, Any] | Unset = UNSET
        if not isinstance(self.child, Unset):
            child = self.child.to_dict()

        children: dict[str, Any] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = self.children.to_dict()

        initialized = self.initialized

        task: dict[str, Any] | Unset = UNSET
        if not isinstance(self.task, Unset):
            task = self.task.to_dict()

        async_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.async_, Unset):
            async_ = self.async_.to_dict()

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        task_chain: dict[str, Any] | Unset = UNSET
        if not isinstance(self.task_chain, Unset):
            task_chain = self.task_chain.to_dict()

        task_chain_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.task_chain_or_builder, Unset):
            task_chain_or_builder = self.task_chain_or_builder.to_dict()

        sync: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sync, Unset):
            sync = self.sync.to_dict()

        sync_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sync_or_builder, Unset):
            sync_or_builder = self.sync_or_builder.to_dict()

        skip_task: dict[str, Any] | Unset = UNSET
        if not isinstance(self.skip_task, Unset):
            skip_task = self.skip_task.to_dict()

        skip_task_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.skip_task_or_builder, Unset):
            skip_task_or_builder = self.skip_task_or_builder.to_dict()

        async_chain: dict[str, Any] | Unset = UNSET
        if not isinstance(self.async_chain, Unset):
            async_chain = self.async_chain.to_dict()

        async_chain_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.async_chain_or_builder, Unset):
            async_chain_or_builder = self.async_chain_or_builder.to_dict()

        facilitator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.facilitator, Unset):
            facilitator = self.facilitator.to_dict()

        facilitator_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.facilitator_or_builder, Unset):
            facilitator_or_builder = self.facilitator_or_builder.to_dict()

        response_case: str | Unset = UNSET
        if not isinstance(self.response_case, Unset):
            response_case = self.response_case

        async_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.async_or_builder, Unset):
            async_or_builder = self.async_or_builder.to_dict()

        child_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.child_or_builder, Unset):
            child_or_builder = self.child_or_builder.to_dict()

        children_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.children_or_builder, Unset):
            children_or_builder = self.children_or_builder.to_dict()

        child_chain: dict[str, Any] | Unset = UNSET
        if not isinstance(self.child_chain, Unset):
            child_chain = self.child_chain.to_dict()

        child_chain_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.child_chain_or_builder, Unset):
            child_chain_or_builder = self.child_chain_or_builder.to_dict()

        task_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.task_or_builder, Unset):
            task_or_builder = self.task_or_builder.to_dict()

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
        if child is not UNSET:
            field_dict["child"] = child
        if children is not UNSET:
            field_dict["children"] = children
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if task is not UNSET:
            field_dict["task"] = task
        if async_ is not UNSET:
            field_dict["async"] = async_
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if task_chain is not UNSET:
            field_dict["taskChain"] = task_chain
        if task_chain_or_builder is not UNSET:
            field_dict["taskChainOrBuilder"] = task_chain_or_builder
        if sync is not UNSET:
            field_dict["sync"] = sync
        if sync_or_builder is not UNSET:
            field_dict["syncOrBuilder"] = sync_or_builder
        if skip_task is not UNSET:
            field_dict["skipTask"] = skip_task
        if skip_task_or_builder is not UNSET:
            field_dict["skipTaskOrBuilder"] = skip_task_or_builder
        if async_chain is not UNSET:
            field_dict["asyncChain"] = async_chain
        if async_chain_or_builder is not UNSET:
            field_dict["asyncChainOrBuilder"] = async_chain_or_builder
        if facilitator is not UNSET:
            field_dict["facilitator"] = facilitator
        if facilitator_or_builder is not UNSET:
            field_dict["facilitatorOrBuilder"] = facilitator_or_builder
        if response_case is not UNSET:
            field_dict["responseCase"] = response_case
        if async_or_builder is not UNSET:
            field_dict["asyncOrBuilder"] = async_or_builder
        if child_or_builder is not UNSET:
            field_dict["childOrBuilder"] = child_or_builder
        if children_or_builder is not UNSET:
            field_dict["childrenOrBuilder"] = children_or_builder
        if child_chain is not UNSET:
            field_dict["childChain"] = child_chain
        if child_chain_or_builder is not UNSET:
            field_dict["childChainOrBuilder"] = child_chain_or_builder
        if task_or_builder is not UNSET:
            field_dict["taskOrBuilder"] = task_or_builder
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
        from ..models.async_chain_executable_response import AsyncChainExecutableResponse
        from ..models.async_chain_executable_response_or_builder import AsyncChainExecutableResponseOrBuilder
        from ..models.async_executable_response import AsyncExecutableResponse
        from ..models.async_executable_response_or_builder import AsyncExecutableResponseOrBuilder
        from ..models.child_chain_executable_response import ChildChainExecutableResponse
        from ..models.child_chain_executable_response_or_builder import ChildChainExecutableResponseOrBuilder
        from ..models.child_executable_response import ChildExecutableResponse
        from ..models.child_executable_response_or_builder import ChildExecutableResponseOrBuilder
        from ..models.children_executable_response import ChildrenExecutableResponse
        from ..models.children_executable_response_or_builder import ChildrenExecutableResponseOrBuilder
        from ..models.descriptor import Descriptor
        from ..models.executable_response_all_fields import ExecutableResponseAllFields
        from ..models.facilitator_executable_response import FacilitatorExecutableResponse
        from ..models.facilitator_executable_response_or_builder import FacilitatorExecutableResponseOrBuilder
        from ..models.parser_executable_response import ParserExecutableResponse
        from ..models.skip_task_executable_response import SkipTaskExecutableResponse
        from ..models.skip_task_executable_response_or_builder import SkipTaskExecutableResponseOrBuilder
        from ..models.sync_executable_response import SyncExecutableResponse
        from ..models.sync_executable_response_or_builder import SyncExecutableResponseOrBuilder
        from ..models.task_chain_executable_response import TaskChainExecutableResponse
        from ..models.task_chain_executable_response_or_builder import TaskChainExecutableResponseOrBuilder
        from ..models.task_executable_response import TaskExecutableResponse
        from ..models.task_executable_response_or_builder import TaskExecutableResponseOrBuilder
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        _child = d.pop("child", UNSET)
        child: ChildExecutableResponse | Unset
        if isinstance(_child, Unset):
            child = UNSET
        else:
            child = ChildExecutableResponse.from_dict(_child)

        _children = d.pop("children", UNSET)
        children: ChildrenExecutableResponse | Unset
        if isinstance(_children, Unset):
            children = UNSET
        else:
            children = ChildrenExecutableResponse.from_dict(_children)

        initialized = d.pop("initialized", UNSET)

        _task = d.pop("task", UNSET)
        task: TaskExecutableResponse | Unset
        if isinstance(_task, Unset):
            task = UNSET
        else:
            task = TaskExecutableResponse.from_dict(_task)

        _async_ = d.pop("async", UNSET)
        async_: AsyncExecutableResponse | Unset
        if isinstance(_async_, Unset):
            async_ = UNSET
        else:
            async_ = AsyncExecutableResponse.from_dict(_async_)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: ExecutableResponse | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = ExecutableResponse.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserExecutableResponse | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserExecutableResponse.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _task_chain = d.pop("taskChain", UNSET)
        task_chain: TaskChainExecutableResponse | Unset
        if isinstance(_task_chain, Unset):
            task_chain = UNSET
        else:
            task_chain = TaskChainExecutableResponse.from_dict(_task_chain)

        _task_chain_or_builder = d.pop("taskChainOrBuilder", UNSET)
        task_chain_or_builder: TaskChainExecutableResponseOrBuilder | Unset
        if isinstance(_task_chain_or_builder, Unset):
            task_chain_or_builder = UNSET
        else:
            task_chain_or_builder = TaskChainExecutableResponseOrBuilder.from_dict(_task_chain_or_builder)

        _sync = d.pop("sync", UNSET)
        sync: SyncExecutableResponse | Unset
        if isinstance(_sync, Unset):
            sync = UNSET
        else:
            sync = SyncExecutableResponse.from_dict(_sync)

        _sync_or_builder = d.pop("syncOrBuilder", UNSET)
        sync_or_builder: SyncExecutableResponseOrBuilder | Unset
        if isinstance(_sync_or_builder, Unset):
            sync_or_builder = UNSET
        else:
            sync_or_builder = SyncExecutableResponseOrBuilder.from_dict(_sync_or_builder)

        _skip_task = d.pop("skipTask", UNSET)
        skip_task: SkipTaskExecutableResponse | Unset
        if isinstance(_skip_task, Unset):
            skip_task = UNSET
        else:
            skip_task = SkipTaskExecutableResponse.from_dict(_skip_task)

        _skip_task_or_builder = d.pop("skipTaskOrBuilder", UNSET)
        skip_task_or_builder: SkipTaskExecutableResponseOrBuilder | Unset
        if isinstance(_skip_task_or_builder, Unset):
            skip_task_or_builder = UNSET
        else:
            skip_task_or_builder = SkipTaskExecutableResponseOrBuilder.from_dict(_skip_task_or_builder)

        _async_chain = d.pop("asyncChain", UNSET)
        async_chain: AsyncChainExecutableResponse | Unset
        if isinstance(_async_chain, Unset):
            async_chain = UNSET
        else:
            async_chain = AsyncChainExecutableResponse.from_dict(_async_chain)

        _async_chain_or_builder = d.pop("asyncChainOrBuilder", UNSET)
        async_chain_or_builder: AsyncChainExecutableResponseOrBuilder | Unset
        if isinstance(_async_chain_or_builder, Unset):
            async_chain_or_builder = UNSET
        else:
            async_chain_or_builder = AsyncChainExecutableResponseOrBuilder.from_dict(_async_chain_or_builder)

        _facilitator = d.pop("facilitator", UNSET)
        facilitator: FacilitatorExecutableResponse | Unset
        if isinstance(_facilitator, Unset):
            facilitator = UNSET
        else:
            facilitator = FacilitatorExecutableResponse.from_dict(_facilitator)

        _facilitator_or_builder = d.pop("facilitatorOrBuilder", UNSET)
        facilitator_or_builder: FacilitatorExecutableResponseOrBuilder | Unset
        if isinstance(_facilitator_or_builder, Unset):
            facilitator_or_builder = UNSET
        else:
            facilitator_or_builder = FacilitatorExecutableResponseOrBuilder.from_dict(_facilitator_or_builder)

        _response_case = d.pop("responseCase", UNSET)
        response_case: ExecutableResponseResponseCase | Unset
        if isinstance(_response_case, Unset):
            response_case = UNSET
        else:
            response_case = check_executable_response_response_case(_response_case)

        _async_or_builder = d.pop("asyncOrBuilder", UNSET)
        async_or_builder: AsyncExecutableResponseOrBuilder | Unset
        if isinstance(_async_or_builder, Unset):
            async_or_builder = UNSET
        else:
            async_or_builder = AsyncExecutableResponseOrBuilder.from_dict(_async_or_builder)

        _child_or_builder = d.pop("childOrBuilder", UNSET)
        child_or_builder: ChildExecutableResponseOrBuilder | Unset
        if isinstance(_child_or_builder, Unset):
            child_or_builder = UNSET
        else:
            child_or_builder = ChildExecutableResponseOrBuilder.from_dict(_child_or_builder)

        _children_or_builder = d.pop("childrenOrBuilder", UNSET)
        children_or_builder: ChildrenExecutableResponseOrBuilder | Unset
        if isinstance(_children_or_builder, Unset):
            children_or_builder = UNSET
        else:
            children_or_builder = ChildrenExecutableResponseOrBuilder.from_dict(_children_or_builder)

        _child_chain = d.pop("childChain", UNSET)
        child_chain: ChildChainExecutableResponse | Unset
        if isinstance(_child_chain, Unset):
            child_chain = UNSET
        else:
            child_chain = ChildChainExecutableResponse.from_dict(_child_chain)

        _child_chain_or_builder = d.pop("childChainOrBuilder", UNSET)
        child_chain_or_builder: ChildChainExecutableResponseOrBuilder | Unset
        if isinstance(_child_chain_or_builder, Unset):
            child_chain_or_builder = UNSET
        else:
            child_chain_or_builder = ChildChainExecutableResponseOrBuilder.from_dict(_child_chain_or_builder)

        _task_or_builder = d.pop("taskOrBuilder", UNSET)
        task_or_builder: TaskExecutableResponseOrBuilder | Unset
        if isinstance(_task_or_builder, Unset):
            task_or_builder = UNSET
        else:
            task_or_builder = TaskExecutableResponseOrBuilder.from_dict(_task_or_builder)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: ExecutableResponseAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = ExecutableResponseAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        executable_response = cls(
            unknown_fields=unknown_fields,
            child=child,
            children=children,
            initialized=initialized,
            task=task,
            async_=async_,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            task_chain=task_chain,
            task_chain_or_builder=task_chain_or_builder,
            sync=sync,
            sync_or_builder=sync_or_builder,
            skip_task=skip_task,
            skip_task_or_builder=skip_task_or_builder,
            async_chain=async_chain,
            async_chain_or_builder=async_chain_or_builder,
            facilitator=facilitator,
            facilitator_or_builder=facilitator_or_builder,
            response_case=response_case,
            async_or_builder=async_or_builder,
            child_or_builder=child_or_builder,
            children_or_builder=children_or_builder,
            child_chain=child_chain,
            child_chain_or_builder=child_chain_or_builder,
            task_or_builder=task_or_builder,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        executable_response.additional_properties = d
        return executable_response

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
