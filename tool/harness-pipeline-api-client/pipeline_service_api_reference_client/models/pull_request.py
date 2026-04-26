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
    from ..models.label import Label
    from ..models.label_or_builder import LabelOrBuilder
    from ..models.parser_pull_request import ParserPullRequest
    from ..models.pull_request_all_fields import PullRequestAllFields
    from ..models.reference import Reference
    from ..models.reference_or_builder import ReferenceOrBuilder
    from ..models.timestamp import Timestamp
    from ..models.timestamp_or_builder import TimestampOrBuilder
    from ..models.unknown_field_set import UnknownFieldSet
    from ..models.user import User
    from ..models.user_or_builder import UserOrBuilder


T = TypeVar("T", bound="PullRequest")


@_attrs_define
class PullRequest:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        link (str | Unset):
        sha (str | Unset):
        author (User | Unset):
        closed (bool | Unset):
        merged (bool | Unset):
        commits_list (list[Commit] | Unset):
        ref_bytes (ByteString | Unset):
        target_bytes (ByteString | Unset):
        source_bytes (ByteString | Unset):
        commits_count (int | Unset):
        commits_or_builder_list (list[CommitOrBuilder] | Unset):
        created_or_builder (TimestampOrBuilder | Unset):
        updated_or_builder (TimestampOrBuilder | Unset):
        link_bytes (ByteString | Unset):
        author_or_builder (UserOrBuilder | Unset):
        sha_bytes (ByteString | Unset):
        body_bytes (ByteString | Unset):
        fork (str | Unset):
        fork_bytes (ByteString | Unset):
        base_or_builder (ReferenceOrBuilder | Unset):
        head_or_builder (ReferenceOrBuilder | Unset):
        labels_list (list[Label] | Unset):
        labels_count (int | Unset):
        labels_or_builder_list (list[LabelOrBuilder] | Unset):
        merge_sha (str | Unset):
        merge_sha_bytes (ByteString | Unset):
        title_bytes (ByteString | Unset):
        head (Reference | Unset):
        target (str | Unset):
        ref (str | Unset):
        number (int | Unset):
        base (Reference | Unset):
        source (str | Unset):
        initialized (bool | Unset):
        body (str | Unset):
        default_instance_for_type (PullRequest | Unset):
        parser_for_type (ParserPullRequest | Unset):
        serialized_size (int | Unset):
        created (Timestamp | Unset):
        updated (Timestamp | Unset):
        title (str | Unset):
        all_fields (PullRequestAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    link: str | Unset = UNSET
    sha: str | Unset = UNSET
    author: User | Unset = UNSET
    closed: bool | Unset = UNSET
    merged: bool | Unset = UNSET
    commits_list: list[Commit] | Unset = UNSET
    ref_bytes: ByteString | Unset = UNSET
    target_bytes: ByteString | Unset = UNSET
    source_bytes: ByteString | Unset = UNSET
    commits_count: int | Unset = UNSET
    commits_or_builder_list: list[CommitOrBuilder] | Unset = UNSET
    created_or_builder: TimestampOrBuilder | Unset = UNSET
    updated_or_builder: TimestampOrBuilder | Unset = UNSET
    link_bytes: ByteString | Unset = UNSET
    author_or_builder: UserOrBuilder | Unset = UNSET
    sha_bytes: ByteString | Unset = UNSET
    body_bytes: ByteString | Unset = UNSET
    fork: str | Unset = UNSET
    fork_bytes: ByteString | Unset = UNSET
    base_or_builder: ReferenceOrBuilder | Unset = UNSET
    head_or_builder: ReferenceOrBuilder | Unset = UNSET
    labels_list: list[Label] | Unset = UNSET
    labels_count: int | Unset = UNSET
    labels_or_builder_list: list[LabelOrBuilder] | Unset = UNSET
    merge_sha: str | Unset = UNSET
    merge_sha_bytes: ByteString | Unset = UNSET
    title_bytes: ByteString | Unset = UNSET
    head: Reference | Unset = UNSET
    target: str | Unset = UNSET
    ref: str | Unset = UNSET
    number: int | Unset = UNSET
    base: Reference | Unset = UNSET
    source: str | Unset = UNSET
    initialized: bool | Unset = UNSET
    body: str | Unset = UNSET
    default_instance_for_type: PullRequest | Unset = UNSET
    parser_for_type: ParserPullRequest | Unset = UNSET
    serialized_size: int | Unset = UNSET
    created: Timestamp | Unset = UNSET
    updated: Timestamp | Unset = UNSET
    title: str | Unset = UNSET
    all_fields: PullRequestAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        link = self.link

        sha = self.sha

        author: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        closed = self.closed

        merged = self.merged

        commits_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.commits_list, Unset):
            commits_list = []
            for commits_list_item_data in self.commits_list:
                commits_list_item = commits_list_item_data.to_dict()
                commits_list.append(commits_list_item)

        ref_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ref_bytes, Unset):
            ref_bytes = self.ref_bytes.to_dict()

        target_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target_bytes, Unset):
            target_bytes = self.target_bytes.to_dict()

        source_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source_bytes, Unset):
            source_bytes = self.source_bytes.to_dict()

        commits_count = self.commits_count

        commits_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.commits_or_builder_list, Unset):
            commits_or_builder_list = []
            for commits_or_builder_list_item_data in self.commits_or_builder_list:
                commits_or_builder_list_item = commits_or_builder_list_item_data.to_dict()
                commits_or_builder_list.append(commits_or_builder_list_item)

        created_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_or_builder, Unset):
            created_or_builder = self.created_or_builder.to_dict()

        updated_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.updated_or_builder, Unset):
            updated_or_builder = self.updated_or_builder.to_dict()

        link_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.link_bytes, Unset):
            link_bytes = self.link_bytes.to_dict()

        author_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author_or_builder, Unset):
            author_or_builder = self.author_or_builder.to_dict()

        sha_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sha_bytes, Unset):
            sha_bytes = self.sha_bytes.to_dict()

        body_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body_bytes, Unset):
            body_bytes = self.body_bytes.to_dict()

        fork = self.fork

        fork_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fork_bytes, Unset):
            fork_bytes = self.fork_bytes.to_dict()

        base_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.base_or_builder, Unset):
            base_or_builder = self.base_or_builder.to_dict()

        head_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.head_or_builder, Unset):
            head_or_builder = self.head_or_builder.to_dict()

        labels_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels_list, Unset):
            labels_list = []
            for labels_list_item_data in self.labels_list:
                labels_list_item = labels_list_item_data.to_dict()
                labels_list.append(labels_list_item)

        labels_count = self.labels_count

        labels_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels_or_builder_list, Unset):
            labels_or_builder_list = []
            for labels_or_builder_list_item_data in self.labels_or_builder_list:
                labels_or_builder_list_item = labels_or_builder_list_item_data.to_dict()
                labels_or_builder_list.append(labels_or_builder_list_item)

        merge_sha = self.merge_sha

        merge_sha_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merge_sha_bytes, Unset):
            merge_sha_bytes = self.merge_sha_bytes.to_dict()

        title_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.title_bytes, Unset):
            title_bytes = self.title_bytes.to_dict()

        head: dict[str, Any] | Unset = UNSET
        if not isinstance(self.head, Unset):
            head = self.head.to_dict()

        target = self.target

        ref = self.ref

        number = self.number

        base: dict[str, Any] | Unset = UNSET
        if not isinstance(self.base, Unset):
            base = self.base.to_dict()

        source = self.source

        initialized = self.initialized

        body = self.body

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        created: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.to_dict()

        updated: dict[str, Any] | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.to_dict()

        title = self.title

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
        if link is not UNSET:
            field_dict["link"] = link
        if sha is not UNSET:
            field_dict["sha"] = sha
        if author is not UNSET:
            field_dict["author"] = author
        if closed is not UNSET:
            field_dict["closed"] = closed
        if merged is not UNSET:
            field_dict["merged"] = merged
        if commits_list is not UNSET:
            field_dict["commitsList"] = commits_list
        if ref_bytes is not UNSET:
            field_dict["refBytes"] = ref_bytes
        if target_bytes is not UNSET:
            field_dict["targetBytes"] = target_bytes
        if source_bytes is not UNSET:
            field_dict["sourceBytes"] = source_bytes
        if commits_count is not UNSET:
            field_dict["commitsCount"] = commits_count
        if commits_or_builder_list is not UNSET:
            field_dict["commitsOrBuilderList"] = commits_or_builder_list
        if created_or_builder is not UNSET:
            field_dict["createdOrBuilder"] = created_or_builder
        if updated_or_builder is not UNSET:
            field_dict["updatedOrBuilder"] = updated_or_builder
        if link_bytes is not UNSET:
            field_dict["linkBytes"] = link_bytes
        if author_or_builder is not UNSET:
            field_dict["authorOrBuilder"] = author_or_builder
        if sha_bytes is not UNSET:
            field_dict["shaBytes"] = sha_bytes
        if body_bytes is not UNSET:
            field_dict["bodyBytes"] = body_bytes
        if fork is not UNSET:
            field_dict["fork"] = fork
        if fork_bytes is not UNSET:
            field_dict["forkBytes"] = fork_bytes
        if base_or_builder is not UNSET:
            field_dict["baseOrBuilder"] = base_or_builder
        if head_or_builder is not UNSET:
            field_dict["headOrBuilder"] = head_or_builder
        if labels_list is not UNSET:
            field_dict["labelsList"] = labels_list
        if labels_count is not UNSET:
            field_dict["labelsCount"] = labels_count
        if labels_or_builder_list is not UNSET:
            field_dict["labelsOrBuilderList"] = labels_or_builder_list
        if merge_sha is not UNSET:
            field_dict["mergeSha"] = merge_sha
        if merge_sha_bytes is not UNSET:
            field_dict["mergeShaBytes"] = merge_sha_bytes
        if title_bytes is not UNSET:
            field_dict["titleBytes"] = title_bytes
        if head is not UNSET:
            field_dict["head"] = head
        if target is not UNSET:
            field_dict["target"] = target
        if ref is not UNSET:
            field_dict["ref"] = ref
        if number is not UNSET:
            field_dict["number"] = number
        if base is not UNSET:
            field_dict["base"] = base
        if source is not UNSET:
            field_dict["source"] = source
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if body is not UNSET:
            field_dict["body"] = body
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if title is not UNSET:
            field_dict["title"] = title
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
        from ..models.label import Label
        from ..models.label_or_builder import LabelOrBuilder
        from ..models.parser_pull_request import ParserPullRequest
        from ..models.pull_request_all_fields import PullRequestAllFields
        from ..models.reference import Reference
        from ..models.reference_or_builder import ReferenceOrBuilder
        from ..models.timestamp import Timestamp
        from ..models.timestamp_or_builder import TimestampOrBuilder
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

        link = d.pop("link", UNSET)

        sha = d.pop("sha", UNSET)

        _author = d.pop("author", UNSET)
        author: User | Unset
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = User.from_dict(_author)

        closed = d.pop("closed", UNSET)

        merged = d.pop("merged", UNSET)

        _commits_list = d.pop("commitsList", UNSET)
        commits_list: list[Commit] | Unset = UNSET
        if _commits_list is not UNSET:
            commits_list = []
            for commits_list_item_data in _commits_list:
                commits_list_item = Commit.from_dict(commits_list_item_data)

                commits_list.append(commits_list_item)

        _ref_bytes = d.pop("refBytes", UNSET)
        ref_bytes: ByteString | Unset
        if isinstance(_ref_bytes, Unset):
            ref_bytes = UNSET
        else:
            ref_bytes = ByteString.from_dict(_ref_bytes)

        _target_bytes = d.pop("targetBytes", UNSET)
        target_bytes: ByteString | Unset
        if isinstance(_target_bytes, Unset):
            target_bytes = UNSET
        else:
            target_bytes = ByteString.from_dict(_target_bytes)

        _source_bytes = d.pop("sourceBytes", UNSET)
        source_bytes: ByteString | Unset
        if isinstance(_source_bytes, Unset):
            source_bytes = UNSET
        else:
            source_bytes = ByteString.from_dict(_source_bytes)

        commits_count = d.pop("commitsCount", UNSET)

        _commits_or_builder_list = d.pop("commitsOrBuilderList", UNSET)
        commits_or_builder_list: list[CommitOrBuilder] | Unset = UNSET
        if _commits_or_builder_list is not UNSET:
            commits_or_builder_list = []
            for commits_or_builder_list_item_data in _commits_or_builder_list:
                commits_or_builder_list_item = CommitOrBuilder.from_dict(commits_or_builder_list_item_data)

                commits_or_builder_list.append(commits_or_builder_list_item)

        _created_or_builder = d.pop("createdOrBuilder", UNSET)
        created_or_builder: TimestampOrBuilder | Unset
        if isinstance(_created_or_builder, Unset):
            created_or_builder = UNSET
        else:
            created_or_builder = TimestampOrBuilder.from_dict(_created_or_builder)

        _updated_or_builder = d.pop("updatedOrBuilder", UNSET)
        updated_or_builder: TimestampOrBuilder | Unset
        if isinstance(_updated_or_builder, Unset):
            updated_or_builder = UNSET
        else:
            updated_or_builder = TimestampOrBuilder.from_dict(_updated_or_builder)

        _link_bytes = d.pop("linkBytes", UNSET)
        link_bytes: ByteString | Unset
        if isinstance(_link_bytes, Unset):
            link_bytes = UNSET
        else:
            link_bytes = ByteString.from_dict(_link_bytes)

        _author_or_builder = d.pop("authorOrBuilder", UNSET)
        author_or_builder: UserOrBuilder | Unset
        if isinstance(_author_or_builder, Unset):
            author_or_builder = UNSET
        else:
            author_or_builder = UserOrBuilder.from_dict(_author_or_builder)

        _sha_bytes = d.pop("shaBytes", UNSET)
        sha_bytes: ByteString | Unset
        if isinstance(_sha_bytes, Unset):
            sha_bytes = UNSET
        else:
            sha_bytes = ByteString.from_dict(_sha_bytes)

        _body_bytes = d.pop("bodyBytes", UNSET)
        body_bytes: ByteString | Unset
        if isinstance(_body_bytes, Unset):
            body_bytes = UNSET
        else:
            body_bytes = ByteString.from_dict(_body_bytes)

        fork = d.pop("fork", UNSET)

        _fork_bytes = d.pop("forkBytes", UNSET)
        fork_bytes: ByteString | Unset
        if isinstance(_fork_bytes, Unset):
            fork_bytes = UNSET
        else:
            fork_bytes = ByteString.from_dict(_fork_bytes)

        _base_or_builder = d.pop("baseOrBuilder", UNSET)
        base_or_builder: ReferenceOrBuilder | Unset
        if isinstance(_base_or_builder, Unset):
            base_or_builder = UNSET
        else:
            base_or_builder = ReferenceOrBuilder.from_dict(_base_or_builder)

        _head_or_builder = d.pop("headOrBuilder", UNSET)
        head_or_builder: ReferenceOrBuilder | Unset
        if isinstance(_head_or_builder, Unset):
            head_or_builder = UNSET
        else:
            head_or_builder = ReferenceOrBuilder.from_dict(_head_or_builder)

        _labels_list = d.pop("labelsList", UNSET)
        labels_list: list[Label] | Unset = UNSET
        if _labels_list is not UNSET:
            labels_list = []
            for labels_list_item_data in _labels_list:
                labels_list_item = Label.from_dict(labels_list_item_data)

                labels_list.append(labels_list_item)

        labels_count = d.pop("labelsCount", UNSET)

        _labels_or_builder_list = d.pop("labelsOrBuilderList", UNSET)
        labels_or_builder_list: list[LabelOrBuilder] | Unset = UNSET
        if _labels_or_builder_list is not UNSET:
            labels_or_builder_list = []
            for labels_or_builder_list_item_data in _labels_or_builder_list:
                labels_or_builder_list_item = LabelOrBuilder.from_dict(labels_or_builder_list_item_data)

                labels_or_builder_list.append(labels_or_builder_list_item)

        merge_sha = d.pop("mergeSha", UNSET)

        _merge_sha_bytes = d.pop("mergeShaBytes", UNSET)
        merge_sha_bytes: ByteString | Unset
        if isinstance(_merge_sha_bytes, Unset):
            merge_sha_bytes = UNSET
        else:
            merge_sha_bytes = ByteString.from_dict(_merge_sha_bytes)

        _title_bytes = d.pop("titleBytes", UNSET)
        title_bytes: ByteString | Unset
        if isinstance(_title_bytes, Unset):
            title_bytes = UNSET
        else:
            title_bytes = ByteString.from_dict(_title_bytes)

        _head = d.pop("head", UNSET)
        head: Reference | Unset
        if isinstance(_head, Unset):
            head = UNSET
        else:
            head = Reference.from_dict(_head)

        target = d.pop("target", UNSET)

        ref = d.pop("ref", UNSET)

        number = d.pop("number", UNSET)

        _base = d.pop("base", UNSET)
        base: Reference | Unset
        if isinstance(_base, Unset):
            base = UNSET
        else:
            base = Reference.from_dict(_base)

        source = d.pop("source", UNSET)

        initialized = d.pop("initialized", UNSET)

        body = d.pop("body", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: PullRequest | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = PullRequest.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserPullRequest | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserPullRequest.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _created = d.pop("created", UNSET)
        created: Timestamp | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = Timestamp.from_dict(_created)

        _updated = d.pop("updated", UNSET)
        updated: Timestamp | Unset
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = Timestamp.from_dict(_updated)

        title = d.pop("title", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: PullRequestAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = PullRequestAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        pull_request = cls(
            unknown_fields=unknown_fields,
            link=link,
            sha=sha,
            author=author,
            closed=closed,
            merged=merged,
            commits_list=commits_list,
            ref_bytes=ref_bytes,
            target_bytes=target_bytes,
            source_bytes=source_bytes,
            commits_count=commits_count,
            commits_or_builder_list=commits_or_builder_list,
            created_or_builder=created_or_builder,
            updated_or_builder=updated_or_builder,
            link_bytes=link_bytes,
            author_or_builder=author_or_builder,
            sha_bytes=sha_bytes,
            body_bytes=body_bytes,
            fork=fork,
            fork_bytes=fork_bytes,
            base_or_builder=base_or_builder,
            head_or_builder=head_or_builder,
            labels_list=labels_list,
            labels_count=labels_count,
            labels_or_builder_list=labels_or_builder_list,
            merge_sha=merge_sha,
            merge_sha_bytes=merge_sha_bytes,
            title_bytes=title_bytes,
            head=head,
            target=target,
            ref=ref,
            number=number,
            base=base,
            source=source,
            initialized=initialized,
            body=body,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            created=created,
            updated=updated,
            title=title,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        pull_request.additional_properties = d
        return pull_request

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
