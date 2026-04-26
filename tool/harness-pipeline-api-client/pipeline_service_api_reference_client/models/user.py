from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.parser_user import ParserUser
    from ..models.timestamp import Timestamp
    from ..models.timestamp_or_builder import TimestampOrBuilder
    from ..models.unknown_field_set import UnknownFieldSet
    from ..models.user_all_fields import UserAllFields


T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        login (str | Unset):
        avatar (str | Unset):
        login_bytes (ByteString | Unset):
        email_bytes (ByteString | Unset):
        avatar_bytes (ByteString | Unset):
        created_or_builder (TimestampOrBuilder | Unset):
        updated_or_builder (TimestampOrBuilder | Unset):
        name (str | Unset):
        id (str | Unset):
        initialized (bool | Unset):
        default_instance_for_type (User | Unset):
        parser_for_type (ParserUser | Unset):
        serialized_size (int | Unset):
        name_bytes (ByteString | Unset):
        created (Timestamp | Unset):
        updated (Timestamp | Unset):
        id_bytes (ByteString | Unset):
        email (str | Unset):
        all_fields (UserAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    login: str | Unset = UNSET
    avatar: str | Unset = UNSET
    login_bytes: ByteString | Unset = UNSET
    email_bytes: ByteString | Unset = UNSET
    avatar_bytes: ByteString | Unset = UNSET
    created_or_builder: TimestampOrBuilder | Unset = UNSET
    updated_or_builder: TimestampOrBuilder | Unset = UNSET
    name: str | Unset = UNSET
    id: str | Unset = UNSET
    initialized: bool | Unset = UNSET
    default_instance_for_type: User | Unset = UNSET
    parser_for_type: ParserUser | Unset = UNSET
    serialized_size: int | Unset = UNSET
    name_bytes: ByteString | Unset = UNSET
    created: Timestamp | Unset = UNSET
    updated: Timestamp | Unset = UNSET
    id_bytes: ByteString | Unset = UNSET
    email: str | Unset = UNSET
    all_fields: UserAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        login = self.login

        avatar = self.avatar

        login_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.login_bytes, Unset):
            login_bytes = self.login_bytes.to_dict()

        email_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.email_bytes, Unset):
            email_bytes = self.email_bytes.to_dict()

        avatar_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avatar_bytes, Unset):
            avatar_bytes = self.avatar_bytes.to_dict()

        created_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_or_builder, Unset):
            created_or_builder = self.created_or_builder.to_dict()

        updated_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.updated_or_builder, Unset):
            updated_or_builder = self.updated_or_builder.to_dict()

        name = self.name

        id = self.id

        initialized = self.initialized

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

        email = self.email

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
        if login is not UNSET:
            field_dict["login"] = login
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if login_bytes is not UNSET:
            field_dict["loginBytes"] = login_bytes
        if email_bytes is not UNSET:
            field_dict["emailBytes"] = email_bytes
        if avatar_bytes is not UNSET:
            field_dict["avatarBytes"] = avatar_bytes
        if created_or_builder is not UNSET:
            field_dict["createdOrBuilder"] = created_or_builder
        if updated_or_builder is not UNSET:
            field_dict["updatedOrBuilder"] = updated_or_builder
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
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
        if email is not UNSET:
            field_dict["email"] = email
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
        from ..models.parser_user import ParserUser
        from ..models.timestamp import Timestamp
        from ..models.timestamp_or_builder import TimestampOrBuilder
        from ..models.unknown_field_set import UnknownFieldSet
        from ..models.user_all_fields import UserAllFields

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        login = d.pop("login", UNSET)

        avatar = d.pop("avatar", UNSET)

        _login_bytes = d.pop("loginBytes", UNSET)
        login_bytes: ByteString | Unset
        if isinstance(_login_bytes, Unset):
            login_bytes = UNSET
        else:
            login_bytes = ByteString.from_dict(_login_bytes)

        _email_bytes = d.pop("emailBytes", UNSET)
        email_bytes: ByteString | Unset
        if isinstance(_email_bytes, Unset):
            email_bytes = UNSET
        else:
            email_bytes = ByteString.from_dict(_email_bytes)

        _avatar_bytes = d.pop("avatarBytes", UNSET)
        avatar_bytes: ByteString | Unset
        if isinstance(_avatar_bytes, Unset):
            avatar_bytes = UNSET
        else:
            avatar_bytes = ByteString.from_dict(_avatar_bytes)

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

        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        initialized = d.pop("initialized", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: User | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = User.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserUser | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserUser.from_dict(_parser_for_type)

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

        email = d.pop("email", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: UserAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = UserAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        user = cls(
            unknown_fields=unknown_fields,
            login=login,
            avatar=avatar,
            login_bytes=login_bytes,
            email_bytes=email_bytes,
            avatar_bytes=avatar_bytes,
            created_or_builder=created_or_builder,
            updated_or_builder=updated_or_builder,
            name=name,
            id=id,
            initialized=initialized,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            name_bytes=name_bytes,
            created=created,
            updated=updated,
            id_bytes=id_bytes,
            email=email,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        user.additional_properties = d
        return user

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
