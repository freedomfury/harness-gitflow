from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tag_hook_or_builder_action import TagHookOrBuilderAction, check_tag_hook_or_builder_action
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.descriptor import Descriptor
    from ..models.message import Message
    from ..models.reference import Reference
    from ..models.reference_or_builder import ReferenceOrBuilder
    from ..models.repository import Repository
    from ..models.repository_or_builder import RepositoryOrBuilder
    from ..models.tag_hook_or_builder_all_fields import TagHookOrBuilderAllFields
    from ..models.unknown_field_set import UnknownFieldSet
    from ..models.user import User
    from ..models.user_or_builder import UserOrBuilder


T = TypeVar("T", bound="TagHookOrBuilder")


@_attrs_define
class TagHookOrBuilder:
    """
    Attributes:
        sender (User | Unset):
        repo_or_builder (RepositoryOrBuilder | Unset):
        sender_or_builder (UserOrBuilder | Unset):
        action_value (int | Unset):
        ref_or_builder (ReferenceOrBuilder | Unset):
        ref (Reference | Unset):
        action (TagHookOrBuilderAction | Unset):
        repo (Repository | Unset):
        all_fields (TagHookOrBuilderAllFields | Unset):
        default_instance_for_type (Message | Unset):
        unknown_fields (UnknownFieldSet | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        initialized (bool | Unset):
    """

    sender: User | Unset = UNSET
    repo_or_builder: RepositoryOrBuilder | Unset = UNSET
    sender_or_builder: UserOrBuilder | Unset = UNSET
    action_value: int | Unset = UNSET
    ref_or_builder: ReferenceOrBuilder | Unset = UNSET
    ref: Reference | Unset = UNSET
    action: TagHookOrBuilderAction | Unset = UNSET
    repo: Repository | Unset = UNSET
    all_fields: TagHookOrBuilderAllFields | Unset = UNSET
    default_instance_for_type: Message | Unset = UNSET
    unknown_fields: UnknownFieldSet | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    initialized: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        ref_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ref_or_builder, Unset):
            ref_or_builder = self.ref_or_builder.to_dict()

        ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ref, Unset):
            ref = self.ref.to_dict()

        action: str | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action

        repo: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repo, Unset):
            repo = self.repo.to_dict()

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
        if sender is not UNSET:
            field_dict["sender"] = sender
        if repo_or_builder is not UNSET:
            field_dict["repoOrBuilder"] = repo_or_builder
        if sender_or_builder is not UNSET:
            field_dict["senderOrBuilder"] = sender_or_builder
        if action_value is not UNSET:
            field_dict["actionValue"] = action_value
        if ref_or_builder is not UNSET:
            field_dict["refOrBuilder"] = ref_or_builder
        if ref is not UNSET:
            field_dict["ref"] = ref
        if action is not UNSET:
            field_dict["action"] = action
        if repo is not UNSET:
            field_dict["repo"] = repo
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
        from ..models.descriptor import Descriptor
        from ..models.message import Message
        from ..models.reference import Reference
        from ..models.reference_or_builder import ReferenceOrBuilder
        from ..models.repository import Repository
        from ..models.repository_or_builder import RepositoryOrBuilder
        from ..models.tag_hook_or_builder_all_fields import TagHookOrBuilderAllFields
        from ..models.unknown_field_set import UnknownFieldSet
        from ..models.user import User
        from ..models.user_or_builder import UserOrBuilder

        d = dict(src_dict)
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

        _ref_or_builder = d.pop("refOrBuilder", UNSET)
        ref_or_builder: ReferenceOrBuilder | Unset
        if isinstance(_ref_or_builder, Unset):
            ref_or_builder = UNSET
        else:
            ref_or_builder = ReferenceOrBuilder.from_dict(_ref_or_builder)

        _ref = d.pop("ref", UNSET)
        ref: Reference | Unset
        if isinstance(_ref, Unset):
            ref = UNSET
        else:
            ref = Reference.from_dict(_ref)

        _action = d.pop("action", UNSET)
        action: TagHookOrBuilderAction | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = check_tag_hook_or_builder_action(_action)

        _repo = d.pop("repo", UNSET)
        repo: Repository | Unset
        if isinstance(_repo, Unset):
            repo = UNSET
        else:
            repo = Repository.from_dict(_repo)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: TagHookOrBuilderAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = TagHookOrBuilderAllFields.from_dict(_all_fields)

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

        tag_hook_or_builder = cls(
            sender=sender,
            repo_or_builder=repo_or_builder,
            sender_or_builder=sender_or_builder,
            action_value=action_value,
            ref_or_builder=ref_or_builder,
            ref=ref,
            action=action,
            repo=repo,
            all_fields=all_fields,
            default_instance_for_type=default_instance_for_type,
            unknown_fields=unknown_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            initialized=initialized,
        )

        tag_hook_or_builder.additional_properties = d
        return tag_hook_or_builder

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
