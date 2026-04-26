from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.parsed_payload_payload_case import ParsedPayloadPayloadCase, check_parsed_payload_payload_case
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.branch_hook import BranchHook
    from ..models.branch_hook_or_builder import BranchHookOrBuilder
    from ..models.descriptor import Descriptor
    from ..models.parsed_payload_all_fields import ParsedPayloadAllFields
    from ..models.parser_parsed_payload import ParserParsedPayload
    from ..models.pull_request_hook import PullRequestHook
    from ..models.pull_request_hook_or_builder import PullRequestHookOrBuilder
    from ..models.push_hook import PushHook
    from ..models.push_hook_or_builder import PushHookOrBuilder
    from ..models.release_hook import ReleaseHook
    from ..models.release_hook_or_builder import ReleaseHookOrBuilder
    from ..models.tag_hook import TagHook
    from ..models.tag_hook_or_builder import TagHookOrBuilder
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="ParsedPayload")


@_attrs_define
class ParsedPayload:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        payload_case (ParsedPayloadPayloadCase | Unset):
        pr (PullRequestHook | Unset):
        push (PushHook | Unset):
        release (ReleaseHook | Unset):
        push_or_builder (PushHookOrBuilder | Unset):
        branch_or_builder (BranchHookOrBuilder | Unset):
        release_or_builder (ReleaseHookOrBuilder | Unset):
        tag_or_builder (TagHookOrBuilder | Unset):
        pr_or_builder (PullRequestHookOrBuilder | Unset):
        tag (TagHook | Unset):
        initialized (bool | Unset):
        default_instance_for_type (ParsedPayload | Unset):
        parser_for_type (ParserParsedPayload | Unset):
        serialized_size (int | Unset):
        branch (BranchHook | Unset):
        all_fields (ParsedPayloadAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    payload_case: ParsedPayloadPayloadCase | Unset = UNSET
    pr: PullRequestHook | Unset = UNSET
    push: PushHook | Unset = UNSET
    release: ReleaseHook | Unset = UNSET
    push_or_builder: PushHookOrBuilder | Unset = UNSET
    branch_or_builder: BranchHookOrBuilder | Unset = UNSET
    release_or_builder: ReleaseHookOrBuilder | Unset = UNSET
    tag_or_builder: TagHookOrBuilder | Unset = UNSET
    pr_or_builder: PullRequestHookOrBuilder | Unset = UNSET
    tag: TagHook | Unset = UNSET
    initialized: bool | Unset = UNSET
    default_instance_for_type: ParsedPayload | Unset = UNSET
    parser_for_type: ParserParsedPayload | Unset = UNSET
    serialized_size: int | Unset = UNSET
    branch: BranchHook | Unset = UNSET
    all_fields: ParsedPayloadAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        payload_case: str | Unset = UNSET
        if not isinstance(self.payload_case, Unset):
            payload_case = self.payload_case

        pr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pr, Unset):
            pr = self.pr.to_dict()

        push: dict[str, Any] | Unset = UNSET
        if not isinstance(self.push, Unset):
            push = self.push.to_dict()

        release: dict[str, Any] | Unset = UNSET
        if not isinstance(self.release, Unset):
            release = self.release.to_dict()

        push_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.push_or_builder, Unset):
            push_or_builder = self.push_or_builder.to_dict()

        branch_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.branch_or_builder, Unset):
            branch_or_builder = self.branch_or_builder.to_dict()

        release_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.release_or_builder, Unset):
            release_or_builder = self.release_or_builder.to_dict()

        tag_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tag_or_builder, Unset):
            tag_or_builder = self.tag_or_builder.to_dict()

        pr_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pr_or_builder, Unset):
            pr_or_builder = self.pr_or_builder.to_dict()

        tag: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tag, Unset):
            tag = self.tag.to_dict()

        initialized = self.initialized

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        branch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.branch, Unset):
            branch = self.branch.to_dict()

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
        if payload_case is not UNSET:
            field_dict["payloadCase"] = payload_case
        if pr is not UNSET:
            field_dict["pr"] = pr
        if push is not UNSET:
            field_dict["push"] = push
        if release is not UNSET:
            field_dict["release"] = release
        if push_or_builder is not UNSET:
            field_dict["pushOrBuilder"] = push_or_builder
        if branch_or_builder is not UNSET:
            field_dict["branchOrBuilder"] = branch_or_builder
        if release_or_builder is not UNSET:
            field_dict["releaseOrBuilder"] = release_or_builder
        if tag_or_builder is not UNSET:
            field_dict["tagOrBuilder"] = tag_or_builder
        if pr_or_builder is not UNSET:
            field_dict["prOrBuilder"] = pr_or_builder
        if tag is not UNSET:
            field_dict["tag"] = tag
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if branch is not UNSET:
            field_dict["branch"] = branch
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
        from ..models.branch_hook import BranchHook
        from ..models.branch_hook_or_builder import BranchHookOrBuilder
        from ..models.descriptor import Descriptor
        from ..models.parsed_payload_all_fields import ParsedPayloadAllFields
        from ..models.parser_parsed_payload import ParserParsedPayload
        from ..models.pull_request_hook import PullRequestHook
        from ..models.pull_request_hook_or_builder import PullRequestHookOrBuilder
        from ..models.push_hook import PushHook
        from ..models.push_hook_or_builder import PushHookOrBuilder
        from ..models.release_hook import ReleaseHook
        from ..models.release_hook_or_builder import ReleaseHookOrBuilder
        from ..models.tag_hook import TagHook
        from ..models.tag_hook_or_builder import TagHookOrBuilder
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        _payload_case = d.pop("payloadCase", UNSET)
        payload_case: ParsedPayloadPayloadCase | Unset
        if isinstance(_payload_case, Unset):
            payload_case = UNSET
        else:
            payload_case = check_parsed_payload_payload_case(_payload_case)

        _pr = d.pop("pr", UNSET)
        pr: PullRequestHook | Unset
        if isinstance(_pr, Unset):
            pr = UNSET
        else:
            pr = PullRequestHook.from_dict(_pr)

        _push = d.pop("push", UNSET)
        push: PushHook | Unset
        if isinstance(_push, Unset):
            push = UNSET
        else:
            push = PushHook.from_dict(_push)

        _release = d.pop("release", UNSET)
        release: ReleaseHook | Unset
        if isinstance(_release, Unset):
            release = UNSET
        else:
            release = ReleaseHook.from_dict(_release)

        _push_or_builder = d.pop("pushOrBuilder", UNSET)
        push_or_builder: PushHookOrBuilder | Unset
        if isinstance(_push_or_builder, Unset):
            push_or_builder = UNSET
        else:
            push_or_builder = PushHookOrBuilder.from_dict(_push_or_builder)

        _branch_or_builder = d.pop("branchOrBuilder", UNSET)
        branch_or_builder: BranchHookOrBuilder | Unset
        if isinstance(_branch_or_builder, Unset):
            branch_or_builder = UNSET
        else:
            branch_or_builder = BranchHookOrBuilder.from_dict(_branch_or_builder)

        _release_or_builder = d.pop("releaseOrBuilder", UNSET)
        release_or_builder: ReleaseHookOrBuilder | Unset
        if isinstance(_release_or_builder, Unset):
            release_or_builder = UNSET
        else:
            release_or_builder = ReleaseHookOrBuilder.from_dict(_release_or_builder)

        _tag_or_builder = d.pop("tagOrBuilder", UNSET)
        tag_or_builder: TagHookOrBuilder | Unset
        if isinstance(_tag_or_builder, Unset):
            tag_or_builder = UNSET
        else:
            tag_or_builder = TagHookOrBuilder.from_dict(_tag_or_builder)

        _pr_or_builder = d.pop("prOrBuilder", UNSET)
        pr_or_builder: PullRequestHookOrBuilder | Unset
        if isinstance(_pr_or_builder, Unset):
            pr_or_builder = UNSET
        else:
            pr_or_builder = PullRequestHookOrBuilder.from_dict(_pr_or_builder)

        _tag = d.pop("tag", UNSET)
        tag: TagHook | Unset
        if isinstance(_tag, Unset):
            tag = UNSET
        else:
            tag = TagHook.from_dict(_tag)

        initialized = d.pop("initialized", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: ParsedPayload | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = ParsedPayload.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserParsedPayload | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserParsedPayload.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _branch = d.pop("branch", UNSET)
        branch: BranchHook | Unset
        if isinstance(_branch, Unset):
            branch = UNSET
        else:
            branch = BranchHook.from_dict(_branch)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: ParsedPayloadAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = ParsedPayloadAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        parsed_payload = cls(
            unknown_fields=unknown_fields,
            payload_case=payload_case,
            pr=pr,
            push=push,
            release=release,
            push_or_builder=push_or_builder,
            branch_or_builder=branch_or_builder,
            release_or_builder=release_or_builder,
            tag_or_builder=tag_or_builder,
            pr_or_builder=pr_or_builder,
            tag=tag,
            initialized=initialized,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            branch=branch,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        parsed_payload.additional_properties = d
        return parsed_payload

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
