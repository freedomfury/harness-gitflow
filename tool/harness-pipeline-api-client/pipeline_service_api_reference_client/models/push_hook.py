from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.commit import Commit
    from ..models.commit_or_builder import CommitOrBuilder
    from ..models.descriptor import Descriptor
    from ..models.parser_push_hook import ParserPushHook
    from ..models.push_hook_all_fields import PushHookAllFields
    from ..models.repository import Repository
    from ..models.repository_or_builder import RepositoryOrBuilder
    from ..models.unknown_field_set import UnknownFieldSet
    from ..models.user import User
    from ..models.user_or_builder import UserOrBuilder


T = TypeVar("T", bound="PushHook")


@_attrs_define
class PushHook:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        after (str | Unset):
        sender (User | Unset):
        commit (Commit | Unset):
        commits_list (list[Commit] | Unset):
        before (str | Unset):
        ref_bytes (ByteString | Unset):
        repo_or_builder (RepositoryOrBuilder | Unset):
        sender_or_builder (UserOrBuilder | Unset):
        base_ref (str | Unset):
        before_bytes (ByteString | Unset):
        after_bytes (ByteString | Unset):
        commit_or_builder (CommitOrBuilder | Unset):
        commits_count (int | Unset):
        commits_or_builder_list (list[CommitOrBuilder] | Unset):
        base_ref_bytes (ByteString | Unset):
        ref (str | Unset):
        initialized (bool | Unset):
        default_instance_for_type (PushHook | Unset):
        parser_for_type (ParserPushHook | Unset):
        serialized_size (int | Unset):
        repo (Repository | Unset):
        all_fields (PushHookAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    after: str | Unset = UNSET
    sender: User | Unset = UNSET
    commit: Commit | Unset = UNSET
    commits_list: list[Commit] | Unset = UNSET
    before: str | Unset = UNSET
    ref_bytes: ByteString | Unset = UNSET
    repo_or_builder: RepositoryOrBuilder | Unset = UNSET
    sender_or_builder: UserOrBuilder | Unset = UNSET
    base_ref: str | Unset = UNSET
    before_bytes: ByteString | Unset = UNSET
    after_bytes: ByteString | Unset = UNSET
    commit_or_builder: CommitOrBuilder | Unset = UNSET
    commits_count: int | Unset = UNSET
    commits_or_builder_list: list[CommitOrBuilder] | Unset = UNSET
    base_ref_bytes: ByteString | Unset = UNSET
    ref: str | Unset = UNSET
    initialized: bool | Unset = UNSET
    default_instance_for_type: PushHook | Unset = UNSET
    parser_for_type: ParserPushHook | Unset = UNSET
    serialized_size: int | Unset = UNSET
    repo: Repository | Unset = UNSET
    all_fields: PushHookAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        after = self.after

        sender: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sender, Unset):
            sender = self.sender.to_dict()

        commit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.commit, Unset):
            commit = self.commit.to_dict()

        commits_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.commits_list, Unset):
            commits_list = []
            for commits_list_item_data in self.commits_list:
                commits_list_item = commits_list_item_data.to_dict()
                commits_list.append(commits_list_item)

        before = self.before

        ref_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ref_bytes, Unset):
            ref_bytes = self.ref_bytes.to_dict()

        repo_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repo_or_builder, Unset):
            repo_or_builder = self.repo_or_builder.to_dict()

        sender_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sender_or_builder, Unset):
            sender_or_builder = self.sender_or_builder.to_dict()

        base_ref = self.base_ref

        before_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.before_bytes, Unset):
            before_bytes = self.before_bytes.to_dict()

        after_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.after_bytes, Unset):
            after_bytes = self.after_bytes.to_dict()

        commit_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.commit_or_builder, Unset):
            commit_or_builder = self.commit_or_builder.to_dict()

        commits_count = self.commits_count

        commits_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.commits_or_builder_list, Unset):
            commits_or_builder_list = []
            for commits_or_builder_list_item_data in self.commits_or_builder_list:
                commits_or_builder_list_item = commits_or_builder_list_item_data.to_dict()
                commits_or_builder_list.append(commits_or_builder_list_item)

        base_ref_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.base_ref_bytes, Unset):
            base_ref_bytes = self.base_ref_bytes.to_dict()

        ref = self.ref

        initialized = self.initialized

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        repo: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repo, Unset):
            repo = self.repo.to_dict()

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
        if after is not UNSET:
            field_dict["after"] = after
        if sender is not UNSET:
            field_dict["sender"] = sender
        if commit is not UNSET:
            field_dict["commit"] = commit
        if commits_list is not UNSET:
            field_dict["commitsList"] = commits_list
        if before is not UNSET:
            field_dict["before"] = before
        if ref_bytes is not UNSET:
            field_dict["refBytes"] = ref_bytes
        if repo_or_builder is not UNSET:
            field_dict["repoOrBuilder"] = repo_or_builder
        if sender_or_builder is not UNSET:
            field_dict["senderOrBuilder"] = sender_or_builder
        if base_ref is not UNSET:
            field_dict["baseRef"] = base_ref
        if before_bytes is not UNSET:
            field_dict["beforeBytes"] = before_bytes
        if after_bytes is not UNSET:
            field_dict["afterBytes"] = after_bytes
        if commit_or_builder is not UNSET:
            field_dict["commitOrBuilder"] = commit_or_builder
        if commits_count is not UNSET:
            field_dict["commitsCount"] = commits_count
        if commits_or_builder_list is not UNSET:
            field_dict["commitsOrBuilderList"] = commits_or_builder_list
        if base_ref_bytes is not UNSET:
            field_dict["baseRefBytes"] = base_ref_bytes
        if ref is not UNSET:
            field_dict["ref"] = ref
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if repo is not UNSET:
            field_dict["repo"] = repo
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
        from ..models.commit import Commit
        from ..models.commit_or_builder import CommitOrBuilder
        from ..models.descriptor import Descriptor
        from ..models.parser_push_hook import ParserPushHook
        from ..models.push_hook_all_fields import PushHookAllFields
        from ..models.repository import Repository
        from ..models.repository_or_builder import RepositoryOrBuilder
        from ..models.unknown_field_set import UnknownFieldSet
        from ..models.user import User
        from ..models.user_or_builder import UserOrBuilder

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        after = d.pop("after", UNSET)

        _sender = d.pop("sender", UNSET)
        sender: User | Unset
        if isinstance(_sender, Unset):
            sender = UNSET
        else:
            sender = User.from_dict(_sender)

        _commit = d.pop("commit", UNSET)
        commit: Commit | Unset
        if isinstance(_commit, Unset):
            commit = UNSET
        else:
            commit = Commit.from_dict(_commit)

        _commits_list = d.pop("commitsList", UNSET)
        commits_list: list[Commit] | Unset = UNSET
        if _commits_list is not UNSET:
            commits_list = []
            for commits_list_item_data in _commits_list:
                commits_list_item = Commit.from_dict(commits_list_item_data)

                commits_list.append(commits_list_item)

        before = d.pop("before", UNSET)

        _ref_bytes = d.pop("refBytes", UNSET)
        ref_bytes: ByteString | Unset
        if isinstance(_ref_bytes, Unset):
            ref_bytes = UNSET
        else:
            ref_bytes = ByteString.from_dict(_ref_bytes)

        _repo_or_builder = d.pop("repoOrBuilder", UNSET)
        repo_or_builder: RepositoryOrBuilder | Unset
        if isinstance(_repo_or_builder, Unset):
            repo_or_builder = UNSET
        else:
            repo_or_builder = RepositoryOrBuilder.from_dict(_repo_or_builder)

        _sender_or_builder = d.pop("senderOrBuilder", UNSET)
        sender_or_builder: UserOrBuilder | Unset
        if isinstance(_sender_or_builder, Unset):
            sender_or_builder = UNSET
        else:
            sender_or_builder = UserOrBuilder.from_dict(_sender_or_builder)

        base_ref = d.pop("baseRef", UNSET)

        _before_bytes = d.pop("beforeBytes", UNSET)
        before_bytes: ByteString | Unset
        if isinstance(_before_bytes, Unset):
            before_bytes = UNSET
        else:
            before_bytes = ByteString.from_dict(_before_bytes)

        _after_bytes = d.pop("afterBytes", UNSET)
        after_bytes: ByteString | Unset
        if isinstance(_after_bytes, Unset):
            after_bytes = UNSET
        else:
            after_bytes = ByteString.from_dict(_after_bytes)

        _commit_or_builder = d.pop("commitOrBuilder", UNSET)
        commit_or_builder: CommitOrBuilder | Unset
        if isinstance(_commit_or_builder, Unset):
            commit_or_builder = UNSET
        else:
            commit_or_builder = CommitOrBuilder.from_dict(_commit_or_builder)

        commits_count = d.pop("commitsCount", UNSET)

        _commits_or_builder_list = d.pop("commitsOrBuilderList", UNSET)
        commits_or_builder_list: list[CommitOrBuilder] | Unset = UNSET
        if _commits_or_builder_list is not UNSET:
            commits_or_builder_list = []
            for commits_or_builder_list_item_data in _commits_or_builder_list:
                commits_or_builder_list_item = CommitOrBuilder.from_dict(commits_or_builder_list_item_data)

                commits_or_builder_list.append(commits_or_builder_list_item)

        _base_ref_bytes = d.pop("baseRefBytes", UNSET)
        base_ref_bytes: ByteString | Unset
        if isinstance(_base_ref_bytes, Unset):
            base_ref_bytes = UNSET
        else:
            base_ref_bytes = ByteString.from_dict(_base_ref_bytes)

        ref = d.pop("ref", UNSET)

        initialized = d.pop("initialized", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: PushHook | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = PushHook.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserPushHook | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserPushHook.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _repo = d.pop("repo", UNSET)
        repo: Repository | Unset
        if isinstance(_repo, Unset):
            repo = UNSET
        else:
            repo = Repository.from_dict(_repo)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: PushHookAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = PushHookAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        push_hook = cls(
            unknown_fields=unknown_fields,
            after=after,
            sender=sender,
            commit=commit,
            commits_list=commits_list,
            before=before,
            ref_bytes=ref_bytes,
            repo_or_builder=repo_or_builder,
            sender_or_builder=sender_or_builder,
            base_ref=base_ref,
            before_bytes=before_bytes,
            after_bytes=after_bytes,
            commit_or_builder=commit_or_builder,
            commits_count=commits_count,
            commits_or_builder_list=commits_or_builder_list,
            base_ref_bytes=base_ref_bytes,
            ref=ref,
            initialized=initialized,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            repo=repo,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        push_hook.additional_properties = d
        return push_hook

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
