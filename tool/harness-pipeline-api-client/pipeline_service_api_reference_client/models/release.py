from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.parser_release import ParserRelease
    from ..models.release_all_fields import ReleaseAllFields
    from ..models.timestamp import Timestamp
    from ..models.timestamp_or_builder import TimestampOrBuilder
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="Release")


@_attrs_define
class Release:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        tag_bytes (ByteString | Unset):
        prerelease (bool | Unset):
        published_or_builder (TimestampOrBuilder | Unset):
        published (Timestamp | Unset):
        link (str | Unset):
        created_or_builder (TimestampOrBuilder | Unset):
        link_bytes (ByteString | Unset):
        title_bytes (ByteString | Unset):
        draft (bool | Unset):
        tag (str | Unset):
        initialized (bool | Unset):
        description (str | Unset):
        default_instance_for_type (Release | Unset):
        parser_for_type (ParserRelease | Unset):
        serialized_size (int | Unset):
        created (Timestamp | Unset):
        description_bytes (ByteString | Unset):
        title (str | Unset):
        all_fields (ReleaseAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    tag_bytes: ByteString | Unset = UNSET
    prerelease: bool | Unset = UNSET
    published_or_builder: TimestampOrBuilder | Unset = UNSET
    published: Timestamp | Unset = UNSET
    link: str | Unset = UNSET
    created_or_builder: TimestampOrBuilder | Unset = UNSET
    link_bytes: ByteString | Unset = UNSET
    title_bytes: ByteString | Unset = UNSET
    draft: bool | Unset = UNSET
    tag: str | Unset = UNSET
    initialized: bool | Unset = UNSET
    description: str | Unset = UNSET
    default_instance_for_type: Release | Unset = UNSET
    parser_for_type: ParserRelease | Unset = UNSET
    serialized_size: int | Unset = UNSET
    created: Timestamp | Unset = UNSET
    description_bytes: ByteString | Unset = UNSET
    title: str | Unset = UNSET
    all_fields: ReleaseAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        tag_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tag_bytes, Unset):
            tag_bytes = self.tag_bytes.to_dict()

        prerelease = self.prerelease

        published_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.published_or_builder, Unset):
            published_or_builder = self.published_or_builder.to_dict()

        published: dict[str, Any] | Unset = UNSET
        if not isinstance(self.published, Unset):
            published = self.published.to_dict()

        link = self.link

        created_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_or_builder, Unset):
            created_or_builder = self.created_or_builder.to_dict()

        link_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.link_bytes, Unset):
            link_bytes = self.link_bytes.to_dict()

        title_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.title_bytes, Unset):
            title_bytes = self.title_bytes.to_dict()

        draft = self.draft

        tag = self.tag

        initialized = self.initialized

        description = self.description

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

        description_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.description_bytes, Unset):
            description_bytes = self.description_bytes.to_dict()

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
        if tag_bytes is not UNSET:
            field_dict["tagBytes"] = tag_bytes
        if prerelease is not UNSET:
            field_dict["prerelease"] = prerelease
        if published_or_builder is not UNSET:
            field_dict["publishedOrBuilder"] = published_or_builder
        if published is not UNSET:
            field_dict["published"] = published
        if link is not UNSET:
            field_dict["link"] = link
        if created_or_builder is not UNSET:
            field_dict["createdOrBuilder"] = created_or_builder
        if link_bytes is not UNSET:
            field_dict["linkBytes"] = link_bytes
        if title_bytes is not UNSET:
            field_dict["titleBytes"] = title_bytes
        if draft is not UNSET:
            field_dict["draft"] = draft
        if tag is not UNSET:
            field_dict["tag"] = tag
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if description is not UNSET:
            field_dict["description"] = description
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if created is not UNSET:
            field_dict["created"] = created
        if description_bytes is not UNSET:
            field_dict["descriptionBytes"] = description_bytes
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
        from ..models.descriptor import Descriptor
        from ..models.parser_release import ParserRelease
        from ..models.release_all_fields import ReleaseAllFields
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

        _tag_bytes = d.pop("tagBytes", UNSET)
        tag_bytes: ByteString | Unset
        if isinstance(_tag_bytes, Unset):
            tag_bytes = UNSET
        else:
            tag_bytes = ByteString.from_dict(_tag_bytes)

        prerelease = d.pop("prerelease", UNSET)

        _published_or_builder = d.pop("publishedOrBuilder", UNSET)
        published_or_builder: TimestampOrBuilder | Unset
        if isinstance(_published_or_builder, Unset):
            published_or_builder = UNSET
        else:
            published_or_builder = TimestampOrBuilder.from_dict(_published_or_builder)

        _published = d.pop("published", UNSET)
        published: Timestamp | Unset
        if isinstance(_published, Unset):
            published = UNSET
        else:
            published = Timestamp.from_dict(_published)

        link = d.pop("link", UNSET)

        _created_or_builder = d.pop("createdOrBuilder", UNSET)
        created_or_builder: TimestampOrBuilder | Unset
        if isinstance(_created_or_builder, Unset):
            created_or_builder = UNSET
        else:
            created_or_builder = TimestampOrBuilder.from_dict(_created_or_builder)

        _link_bytes = d.pop("linkBytes", UNSET)
        link_bytes: ByteString | Unset
        if isinstance(_link_bytes, Unset):
            link_bytes = UNSET
        else:
            link_bytes = ByteString.from_dict(_link_bytes)

        _title_bytes = d.pop("titleBytes", UNSET)
        title_bytes: ByteString | Unset
        if isinstance(_title_bytes, Unset):
            title_bytes = UNSET
        else:
            title_bytes = ByteString.from_dict(_title_bytes)

        draft = d.pop("draft", UNSET)

        tag = d.pop("tag", UNSET)

        initialized = d.pop("initialized", UNSET)

        description = d.pop("description", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: Release | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = Release.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserRelease | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserRelease.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _created = d.pop("created", UNSET)
        created: Timestamp | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = Timestamp.from_dict(_created)

        _description_bytes = d.pop("descriptionBytes", UNSET)
        description_bytes: ByteString | Unset
        if isinstance(_description_bytes, Unset):
            description_bytes = UNSET
        else:
            description_bytes = ByteString.from_dict(_description_bytes)

        title = d.pop("title", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: ReleaseAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = ReleaseAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        release = cls(
            unknown_fields=unknown_fields,
            tag_bytes=tag_bytes,
            prerelease=prerelease,
            published_or_builder=published_or_builder,
            published=published,
            link=link,
            created_or_builder=created_or_builder,
            link_bytes=link_bytes,
            title_bytes=title_bytes,
            draft=draft,
            tag=tag,
            initialized=initialized,
            description=description,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            created=created,
            description_bytes=description_bytes,
            title=title,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        release.additional_properties = d
        return release

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
