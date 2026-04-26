from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.parser_repository import ParserRepository
    from ..models.perm import Perm
    from ..models.perm_or_builder import PermOrBuilder
    from ..models.repository_all_fields import RepositoryAllFields
    from ..models.timestamp import Timestamp
    from ..models.timestamp_or_builder import TimestampOrBuilder
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="Repository")


@_attrs_define
class Repository:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        link (str | Unset):
        clone (str | Unset):
        clone_ssh (str | Unset):
        branch_bytes (ByteString | Unset):
        created_or_builder (TimestampOrBuilder | Unset):
        updated_or_builder (TimestampOrBuilder | Unset):
        namespace_bytes (ByteString | Unset):
        perm (Perm | Unset):
        perm_or_builder (PermOrBuilder | Unset):
        clone_bytes (ByteString | Unset):
        clone_ssh_bytes (ByteString | Unset):
        link_bytes (ByteString | Unset):
        private (bool | Unset):
        name (str | Unset):
        id (str | Unset):
        initialized (bool | Unset):
        namespace (str | Unset):
        default_instance_for_type (Repository | Unset):
        parser_for_type (ParserRepository | Unset):
        serialized_size (int | Unset):
        name_bytes (ByteString | Unset):
        created (Timestamp | Unset):
        updated (Timestamp | Unset):
        id_bytes (ByteString | Unset):
        branch (str | Unset):
        all_fields (RepositoryAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    link: str | Unset = UNSET
    clone: str | Unset = UNSET
    clone_ssh: str | Unset = UNSET
    branch_bytes: ByteString | Unset = UNSET
    created_or_builder: TimestampOrBuilder | Unset = UNSET
    updated_or_builder: TimestampOrBuilder | Unset = UNSET
    namespace_bytes: ByteString | Unset = UNSET
    perm: Perm | Unset = UNSET
    perm_or_builder: PermOrBuilder | Unset = UNSET
    clone_bytes: ByteString | Unset = UNSET
    clone_ssh_bytes: ByteString | Unset = UNSET
    link_bytes: ByteString | Unset = UNSET
    private: bool | Unset = UNSET
    name: str | Unset = UNSET
    id: str | Unset = UNSET
    initialized: bool | Unset = UNSET
    namespace: str | Unset = UNSET
    default_instance_for_type: Repository | Unset = UNSET
    parser_for_type: ParserRepository | Unset = UNSET
    serialized_size: int | Unset = UNSET
    name_bytes: ByteString | Unset = UNSET
    created: Timestamp | Unset = UNSET
    updated: Timestamp | Unset = UNSET
    id_bytes: ByteString | Unset = UNSET
    branch: str | Unset = UNSET
    all_fields: RepositoryAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        link = self.link

        clone = self.clone

        clone_ssh = self.clone_ssh

        branch_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.branch_bytes, Unset):
            branch_bytes = self.branch_bytes.to_dict()

        created_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_or_builder, Unset):
            created_or_builder = self.created_or_builder.to_dict()

        updated_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.updated_or_builder, Unset):
            updated_or_builder = self.updated_or_builder.to_dict()

        namespace_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.namespace_bytes, Unset):
            namespace_bytes = self.namespace_bytes.to_dict()

        perm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.perm, Unset):
            perm = self.perm.to_dict()

        perm_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.perm_or_builder, Unset):
            perm_or_builder = self.perm_or_builder.to_dict()

        clone_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.clone_bytes, Unset):
            clone_bytes = self.clone_bytes.to_dict()

        clone_ssh_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.clone_ssh_bytes, Unset):
            clone_ssh_bytes = self.clone_ssh_bytes.to_dict()

        link_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.link_bytes, Unset):
            link_bytes = self.link_bytes.to_dict()

        private = self.private

        name = self.name

        id = self.id

        initialized = self.initialized

        namespace = self.namespace

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        name_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.name_bytes, Unset):
            name_bytes = self.name_bytes.to_dict()

        created: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.to_dict()

        updated: dict[str, Any] | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.to_dict()

        id_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.id_bytes, Unset):
            id_bytes = self.id_bytes.to_dict()

        branch = self.branch

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
        if clone is not UNSET:
            field_dict["clone"] = clone
        if clone_ssh is not UNSET:
            field_dict["cloneSsh"] = clone_ssh
        if branch_bytes is not UNSET:
            field_dict["branchBytes"] = branch_bytes
        if created_or_builder is not UNSET:
            field_dict["createdOrBuilder"] = created_or_builder
        if updated_or_builder is not UNSET:
            field_dict["updatedOrBuilder"] = updated_or_builder
        if namespace_bytes is not UNSET:
            field_dict["namespaceBytes"] = namespace_bytes
        if perm is not UNSET:
            field_dict["perm"] = perm
        if perm_or_builder is not UNSET:
            field_dict["permOrBuilder"] = perm_or_builder
        if clone_bytes is not UNSET:
            field_dict["cloneBytes"] = clone_bytes
        if clone_ssh_bytes is not UNSET:
            field_dict["cloneSshBytes"] = clone_ssh_bytes
        if link_bytes is not UNSET:
            field_dict["linkBytes"] = link_bytes
        if private is not UNSET:
            field_dict["private"] = private
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if name_bytes is not UNSET:
            field_dict["nameBytes"] = name_bytes
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if id_bytes is not UNSET:
            field_dict["idBytes"] = id_bytes
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
        from ..models.byte_string import ByteString
        from ..models.descriptor import Descriptor
        from ..models.parser_repository import ParserRepository
        from ..models.perm import Perm
        from ..models.perm_or_builder import PermOrBuilder
        from ..models.repository_all_fields import RepositoryAllFields
        from ..models.timestamp import Timestamp
        from ..models.timestamp_or_builder import TimestampOrBuilder
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        link = d.pop("link", UNSET)

        clone = d.pop("clone", UNSET)

        clone_ssh = d.pop("cloneSsh", UNSET)

        _branch_bytes = d.pop("branchBytes", UNSET)
        branch_bytes: ByteString | Unset
        if isinstance(_branch_bytes, Unset):
            branch_bytes = UNSET
        else:
            branch_bytes = ByteString.from_dict(_branch_bytes)

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

        _namespace_bytes = d.pop("namespaceBytes", UNSET)
        namespace_bytes: ByteString | Unset
        if isinstance(_namespace_bytes, Unset):
            namespace_bytes = UNSET
        else:
            namespace_bytes = ByteString.from_dict(_namespace_bytes)

        _perm = d.pop("perm", UNSET)
        perm: Perm | Unset
        if isinstance(_perm, Unset):
            perm = UNSET
        else:
            perm = Perm.from_dict(_perm)

        _perm_or_builder = d.pop("permOrBuilder", UNSET)
        perm_or_builder: PermOrBuilder | Unset
        if isinstance(_perm_or_builder, Unset):
            perm_or_builder = UNSET
        else:
            perm_or_builder = PermOrBuilder.from_dict(_perm_or_builder)

        _clone_bytes = d.pop("cloneBytes", UNSET)
        clone_bytes: ByteString | Unset
        if isinstance(_clone_bytes, Unset):
            clone_bytes = UNSET
        else:
            clone_bytes = ByteString.from_dict(_clone_bytes)

        _clone_ssh_bytes = d.pop("cloneSshBytes", UNSET)
        clone_ssh_bytes: ByteString | Unset
        if isinstance(_clone_ssh_bytes, Unset):
            clone_ssh_bytes = UNSET
        else:
            clone_ssh_bytes = ByteString.from_dict(_clone_ssh_bytes)

        _link_bytes = d.pop("linkBytes", UNSET)
        link_bytes: ByteString | Unset
        if isinstance(_link_bytes, Unset):
            link_bytes = UNSET
        else:
            link_bytes = ByteString.from_dict(_link_bytes)

        private = d.pop("private", UNSET)

        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        initialized = d.pop("initialized", UNSET)

        namespace = d.pop("namespace", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: Repository | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = Repository.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserRepository | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserRepository.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _name_bytes = d.pop("nameBytes", UNSET)
        name_bytes: ByteString | Unset
        if isinstance(_name_bytes, Unset):
            name_bytes = UNSET
        else:
            name_bytes = ByteString.from_dict(_name_bytes)

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

        _id_bytes = d.pop("idBytes", UNSET)
        id_bytes: ByteString | Unset
        if isinstance(_id_bytes, Unset):
            id_bytes = UNSET
        else:
            id_bytes = ByteString.from_dict(_id_bytes)

        branch = d.pop("branch", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: RepositoryAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = RepositoryAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        repository = cls(
            unknown_fields=unknown_fields,
            link=link,
            clone=clone,
            clone_ssh=clone_ssh,
            branch_bytes=branch_bytes,
            created_or_builder=created_or_builder,
            updated_or_builder=updated_or_builder,
            namespace_bytes=namespace_bytes,
            perm=perm,
            perm_or_builder=perm_or_builder,
            clone_bytes=clone_bytes,
            clone_ssh_bytes=clone_ssh_bytes,
            link_bytes=link_bytes,
            private=private,
            name=name,
            id=id,
            initialized=initialized,
            namespace=namespace,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            name_bytes=name_bytes,
            created=created,
            updated=updated,
            id_bytes=id_bytes,
            branch=branch,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        repository.additional_properties = d
        return repository

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
