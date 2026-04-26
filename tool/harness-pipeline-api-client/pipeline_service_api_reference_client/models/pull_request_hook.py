from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pull_request_hook_action import PullRequestHookAction, check_pull_request_hook_action
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.descriptor import Descriptor
    from ..models.parser_pull_request_hook import ParserPullRequestHook
    from ..models.pull_request import PullRequest
    from ..models.pull_request_hook_all_fields import PullRequestHookAllFields
    from ..models.pull_request_or_builder import PullRequestOrBuilder
    from ..models.repository import Repository
    from ..models.repository_or_builder import RepositoryOrBuilder
    from ..models.unknown_field_set import UnknownFieldSet
    from ..models.user import User
    from ..models.user_or_builder import UserOrBuilder


T = TypeVar("T", bound="PullRequestHook")


@_attrs_define
class PullRequestHook:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        pr (PullRequest | Unset):
        sender (User | Unset):
        repo_or_builder (RepositoryOrBuilder | Unset):
        sender_or_builder (UserOrBuilder | Unset):
        action_value (int | Unset):
        pr_or_builder (PullRequestOrBuilder | Unset):
        initialized (bool | Unset):
        action (PullRequestHookAction | Unset):
        default_instance_for_type (PullRequestHook | Unset):
        parser_for_type (ParserPullRequestHook | Unset):
        serialized_size (int | Unset):
        repo (Repository | Unset):
        all_fields (PullRequestHookAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    pr: PullRequest | Unset = UNSET
    sender: User | Unset = UNSET
    repo_or_builder: RepositoryOrBuilder | Unset = UNSET
    sender_or_builder: UserOrBuilder | Unset = UNSET
    action_value: int | Unset = UNSET
    pr_or_builder: PullRequestOrBuilder | Unset = UNSET
    initialized: bool | Unset = UNSET
    action: PullRequestHookAction | Unset = UNSET
    default_instance_for_type: PullRequestHook | Unset = UNSET
    parser_for_type: ParserPullRequestHook | Unset = UNSET
    serialized_size: int | Unset = UNSET
    repo: Repository | Unset = UNSET
    all_fields: PullRequestHookAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        pr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pr, Unset):
            pr = self.pr.to_dict()

        sender: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sender, Unset):
            sender = self.sender.to_dict()

        repo_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repo_or_builder, Unset):
            repo_or_builder = self.repo_or_builder.to_dict()

        sender_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sender_or_builder, Unset):
            sender_or_builder = self.sender_or_builder.to_dict()

        action_value = self.action_value

        pr_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pr_or_builder, Unset):
            pr_or_builder = self.pr_or_builder.to_dict()

        initialized = self.initialized

        action: str | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action

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
        if pr is not UNSET:
            field_dict["pr"] = pr
        if sender is not UNSET:
            field_dict["sender"] = sender
        if repo_or_builder is not UNSET:
            field_dict["repoOrBuilder"] = repo_or_builder
        if sender_or_builder is not UNSET:
            field_dict["senderOrBuilder"] = sender_or_builder
        if action_value is not UNSET:
            field_dict["actionValue"] = action_value
        if pr_or_builder is not UNSET:
            field_dict["prOrBuilder"] = pr_or_builder
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if action is not UNSET:
            field_dict["action"] = action
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
        from ..models.descriptor import Descriptor
        from ..models.parser_pull_request_hook import ParserPullRequestHook
        from ..models.pull_request import PullRequest
        from ..models.pull_request_hook_all_fields import PullRequestHookAllFields
        from ..models.pull_request_or_builder import PullRequestOrBuilder
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

        _pr = d.pop("pr", UNSET)
        pr: PullRequest | Unset
        if isinstance(_pr, Unset):
            pr = UNSET
        else:
            pr = PullRequest.from_dict(_pr)

        _sender = d.pop("sender", UNSET)
        sender: User | Unset
        if isinstance(_sender, Unset):
            sender = UNSET
        else:
            sender = User.from_dict(_sender)

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

        action_value = d.pop("actionValue", UNSET)

        _pr_or_builder = d.pop("prOrBuilder", UNSET)
        pr_or_builder: PullRequestOrBuilder | Unset
        if isinstance(_pr_or_builder, Unset):
            pr_or_builder = UNSET
        else:
            pr_or_builder = PullRequestOrBuilder.from_dict(_pr_or_builder)

        initialized = d.pop("initialized", UNSET)

        _action = d.pop("action", UNSET)
        action: PullRequestHookAction | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = check_pull_request_hook_action(_action)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: PullRequestHook | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = PullRequestHook.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserPullRequestHook | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserPullRequestHook.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _repo = d.pop("repo", UNSET)
        repo: Repository | Unset
        if isinstance(_repo, Unset):
            repo = UNSET
        else:
            repo = Repository.from_dict(_repo)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: PullRequestHookAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = PullRequestHookAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        pull_request_hook = cls(
            unknown_fields=unknown_fields,
            pr=pr,
            sender=sender,
            repo_or_builder=repo_or_builder,
            sender_or_builder=sender_or_builder,
            action_value=action_value,
            pr_or_builder=pr_or_builder,
            initialized=initialized,
            action=action,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            repo=repo,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        pull_request_hook.additional_properties = d
        return pull_request_hook

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
