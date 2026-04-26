from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.message import Message
    from ..models.release_or_builder_all_fields import ReleaseOrBuilderAllFields
    from ..models.timestamp import Timestamp
    from ..models.timestamp_or_builder import TimestampOrBuilder
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="ReleaseOrBuilder")


@_attrs_define
class ReleaseOrBuilder:
    """
    Attributes:
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
        description (str | Unset):
        created (Timestamp | Unset):
        description_bytes (ByteString | Unset):
        title (str | Unset):
        all_fields (ReleaseOrBuilderAllFields | Unset):
        default_instance_for_type (Message | Unset):
        unknown_fields (UnknownFieldSet | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        initialized (bool | Unset):
    """

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
    description: str | Unset = UNSET
    created: Timestamp | Unset = UNSET
    description_bytes: ByteString | Unset = UNSET
    title: str | Unset = UNSET
    all_fields: ReleaseOrBuilderAllFields | Unset = UNSET
    default_instance_for_type: Message | Unset = UNSET
    unknown_fields: UnknownFieldSet | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    initialized: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        description = self.description

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
        if description is not UNSET:
            field_dict["description"] = description
        if created is not UNSET:
            field_dict["created"] = created
        if description_bytes is not UNSET:
            field_dict["descriptionBytes"] = description_bytes
        if title is not UNSET:
            field_dict["title"] = title
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
        from ..models.byte_string import ByteString
        from ..models.descriptor import Descriptor
        from ..models.message import Message
        from ..models.release_or_builder_all_fields import ReleaseOrBuilderAllFields
        from ..models.timestamp import Timestamp
        from ..models.timestamp_or_builder import TimestampOrBuilder
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
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

        description = d.pop("description", UNSET)

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
        all_fields: ReleaseOrBuilderAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = ReleaseOrBuilderAllFields.from_dict(_all_fields)

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

        release_or_builder = cls(
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
            description=description,
            created=created,
            description_bytes=description_bytes,
            title=title,
            all_fields=all_fields,
            default_instance_for_type=default_instance_for_type,
            unknown_fields=unknown_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            initialized=initialized,
        )

        release_or_builder.additional_properties = d
        return release_or_builder

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
