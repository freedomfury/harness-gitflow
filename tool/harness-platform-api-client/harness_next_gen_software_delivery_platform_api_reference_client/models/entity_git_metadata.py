from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.entity_git_metadata_all_fields import EntityGitMetadataAllFields
    from ..models.parser_entity_git_metadata import ParserEntityGitMetadata
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="EntityGitMetadata")


@_attrs_define
class EntityGitMetadata:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        repo (str | Unset):
        branch (str | Unset):
        parser_for_type (ParserEntityGitMetadata | Unset):
        serialized_size (int | Unset):
        repo_bytes (ByteString | Unset):
        branch_bytes (ByteString | Unset):
        default_instance_for_type (EntityGitMetadata | Unset):
        initialized (bool | Unset):
        initialization_error_string (str | Unset):
        all_fields (EntityGitMetadataAllFields | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    repo: str | Unset = UNSET
    branch: str | Unset = UNSET
    parser_for_type: ParserEntityGitMetadata | Unset = UNSET
    serialized_size: int | Unset = UNSET
    repo_bytes: ByteString | Unset = UNSET
    branch_bytes: ByteString | Unset = UNSET
    default_instance_for_type: EntityGitMetadata | Unset = UNSET
    initialized: bool | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    all_fields: EntityGitMetadataAllFields | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        repo = self.repo

        branch = self.branch

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        repo_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repo_bytes, Unset):
            repo_bytes = self.repo_bytes.to_dict()

        branch_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.branch_bytes, Unset):
            branch_bytes = self.branch_bytes.to_dict()

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        initialized = self.initialized

        initialization_error_string = self.initialization_error_string

        all_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_fields, Unset):
            all_fields = self.all_fields.to_dict()

        descriptor_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.descriptor_for_type, Unset):
            descriptor_for_type = self.descriptor_for_type.to_dict()

        memoized_serialized_size = self.memoized_serialized_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unknown_fields is not UNSET:
            field_dict["unknownFields"] = unknown_fields
        if repo is not UNSET:
            field_dict["repo"] = repo
        if branch is not UNSET:
            field_dict["branch"] = branch
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if repo_bytes is not UNSET:
            field_dict["repoBytes"] = repo_bytes
        if branch_bytes is not UNSET:
            field_dict["branchBytes"] = branch_bytes
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if initialization_error_string is not UNSET:
            field_dict["initializationErrorString"] = initialization_error_string
        if all_fields is not UNSET:
            field_dict["allFields"] = all_fields
        if descriptor_for_type is not UNSET:
            field_dict["descriptorForType"] = descriptor_for_type
        if memoized_serialized_size is not UNSET:
            field_dict["memoizedSerializedSize"] = memoized_serialized_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.byte_string import ByteString
        from ..models.descriptor import Descriptor
        from ..models.entity_git_metadata_all_fields import EntityGitMetadataAllFields
        from ..models.parser_entity_git_metadata import ParserEntityGitMetadata
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        repo = d.pop("repo", UNSET)

        branch = d.pop("branch", UNSET)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserEntityGitMetadata | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserEntityGitMetadata.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _repo_bytes = d.pop("repoBytes", UNSET)
        repo_bytes: ByteString | Unset
        if isinstance(_repo_bytes, Unset):
            repo_bytes = UNSET
        else:
            repo_bytes = ByteString.from_dict(_repo_bytes)

        _branch_bytes = d.pop("branchBytes", UNSET)
        branch_bytes: ByteString | Unset
        if isinstance(_branch_bytes, Unset):
            branch_bytes = UNSET
        else:
            branch_bytes = ByteString.from_dict(_branch_bytes)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: EntityGitMetadata | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = EntityGitMetadata.from_dict(_default_instance_for_type)

        initialized = d.pop("initialized", UNSET)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: EntityGitMetadataAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = EntityGitMetadataAllFields.from_dict(_all_fields)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        entity_git_metadata = cls(
            unknown_fields=unknown_fields,
            repo=repo,
            branch=branch,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            repo_bytes=repo_bytes,
            branch_bytes=branch_bytes,
            default_instance_for_type=default_instance_for_type,
            initialized=initialized,
            initialization_error_string=initialization_error_string,
            all_fields=all_fields,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        entity_git_metadata.additional_properties = d
        return entity_git_metadata

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
