from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_pull_req_activity_kind import EnumPullReqActivityKind
from ..models.enum_pull_req_activity_type import EnumPullReqActivityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_code_comment_fields import TypesCodeCommentFields
    from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0
    from ..models.types_pull_req_activity_mentions import TypesPullReqActivityMentions
    from ..models.types_pull_req_activity_metadata import TypesPullReqActivityMetadata
    from ..models.types_pull_req_activity_user_group_mentions import TypesPullReqActivityUserGroupMentions


T = TypeVar("T", bound="TypesPullReqActivity")


@_attrs_define
class TypesPullReqActivity:
    """
    Attributes:
        author (None | TypesPrincipalInfoType0 | Unset):
        code_comment (TypesCodeCommentFields | Unset):
        created (int | Unset):
        deleted (int | None | Unset):
        edited (int | Unset):
        id (int | Unset):
        kind (EnumPullReqActivityKind | Unset):
        mentions (TypesPullReqActivityMentions | Unset):
        metadata (TypesPullReqActivityMetadata | Unset):
        order (int | Unset):
        parent_id (int | None | Unset):
        payload (Any | Unset):
        pullreq_id (int | Unset):
        repo_id (int | Unset):
        resolved (int | None | Unset):
        resolver (None | TypesPrincipalInfoType0 | Unset):
        sub_order (int | Unset):
        text (str | Unset):
        type_ (EnumPullReqActivityType | Unset):
        updated (int | Unset):
        user_group_mentions (TypesPullReqActivityUserGroupMentions | Unset):
    """

    author: None | TypesPrincipalInfoType0 | Unset = UNSET
    code_comment: TypesCodeCommentFields | Unset = UNSET
    created: int | Unset = UNSET
    deleted: int | None | Unset = UNSET
    edited: int | Unset = UNSET
    id: int | Unset = UNSET
    kind: EnumPullReqActivityKind | Unset = UNSET
    mentions: TypesPullReqActivityMentions | Unset = UNSET
    metadata: TypesPullReqActivityMetadata | Unset = UNSET
    order: int | Unset = UNSET
    parent_id: int | None | Unset = UNSET
    payload: Any | Unset = UNSET
    pullreq_id: int | Unset = UNSET
    repo_id: int | Unset = UNSET
    resolved: int | None | Unset = UNSET
    resolver: None | TypesPrincipalInfoType0 | Unset = UNSET
    sub_order: int | Unset = UNSET
    text: str | Unset = UNSET
    type_: EnumPullReqActivityType | Unset = UNSET
    updated: int | Unset = UNSET
    user_group_mentions: TypesPullReqActivityUserGroupMentions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0

        author: dict[str, Any] | None | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        elif isinstance(self.author, TypesPrincipalInfoType0):
            author = self.author.to_dict()
        else:
            author = self.author

        code_comment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.code_comment, Unset):
            code_comment = self.code_comment.to_dict()

        created = self.created

        deleted: int | None | Unset
        if isinstance(self.deleted, Unset):
            deleted = UNSET
        else:
            deleted = self.deleted

        edited = self.edited

        id = self.id

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        mentions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mentions, Unset):
            mentions = self.mentions.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        order = self.order

        parent_id: int | None | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        payload = self.payload

        pullreq_id = self.pullreq_id

        repo_id = self.repo_id

        resolved: int | None | Unset
        if isinstance(self.resolved, Unset):
            resolved = UNSET
        else:
            resolved = self.resolved

        resolver: dict[str, Any] | None | Unset
        if isinstance(self.resolver, Unset):
            resolver = UNSET
        elif isinstance(self.resolver, TypesPrincipalInfoType0):
            resolver = self.resolver.to_dict()
        else:
            resolver = self.resolver

        sub_order = self.sub_order

        text = self.text

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated = self.updated

        user_group_mentions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_group_mentions, Unset):
            user_group_mentions = self.user_group_mentions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if code_comment is not UNSET:
            field_dict["code_comment"] = code_comment
        if created is not UNSET:
            field_dict["created"] = created
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if edited is not UNSET:
            field_dict["edited"] = edited
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if mentions is not UNSET:
            field_dict["mentions"] = mentions
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if order is not UNSET:
            field_dict["order"] = order
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if payload is not UNSET:
            field_dict["payload"] = payload
        if pullreq_id is not UNSET:
            field_dict["pullreq_id"] = pullreq_id
        if repo_id is not UNSET:
            field_dict["repo_id"] = repo_id
        if resolved is not UNSET:
            field_dict["resolved"] = resolved
        if resolver is not UNSET:
            field_dict["resolver"] = resolver
        if sub_order is not UNSET:
            field_dict["sub_order"] = sub_order
        if text is not UNSET:
            field_dict["text"] = text
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated is not UNSET:
            field_dict["updated"] = updated
        if user_group_mentions is not UNSET:
            field_dict["user_group_mentions"] = user_group_mentions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_code_comment_fields import TypesCodeCommentFields
        from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0
        from ..models.types_pull_req_activity_mentions import TypesPullReqActivityMentions
        from ..models.types_pull_req_activity_metadata import TypesPullReqActivityMetadata
        from ..models.types_pull_req_activity_user_group_mentions import TypesPullReqActivityUserGroupMentions

        d = dict(src_dict)

        def _parse_author(data: object) -> None | TypesPrincipalInfoType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_types_principal_info_type_0 = TypesPrincipalInfoType0.from_dict(data)

                return componentsschemas_types_principal_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TypesPrincipalInfoType0 | Unset, data)

        author = _parse_author(d.pop("author", UNSET))

        _code_comment = d.pop("code_comment", UNSET)
        code_comment: TypesCodeCommentFields | Unset
        if isinstance(_code_comment, Unset):
            code_comment = UNSET
        else:
            code_comment = TypesCodeCommentFields.from_dict(_code_comment)

        created = d.pop("created", UNSET)

        def _parse_deleted(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        deleted = _parse_deleted(d.pop("deleted", UNSET))

        edited = d.pop("edited", UNSET)

        id = d.pop("id", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: EnumPullReqActivityKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = EnumPullReqActivityKind(_kind)

        _mentions = d.pop("mentions", UNSET)
        mentions: TypesPullReqActivityMentions | Unset
        if isinstance(_mentions, Unset):
            mentions = UNSET
        else:
            mentions = TypesPullReqActivityMentions.from_dict(_mentions)

        _metadata = d.pop("metadata", UNSET)
        metadata: TypesPullReqActivityMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = TypesPullReqActivityMetadata.from_dict(_metadata)

        order = d.pop("order", UNSET)

        def _parse_parent_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        payload = d.pop("payload", UNSET)

        pullreq_id = d.pop("pullreq_id", UNSET)

        repo_id = d.pop("repo_id", UNSET)

        def _parse_resolved(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        resolved = _parse_resolved(d.pop("resolved", UNSET))

        def _parse_resolver(data: object) -> None | TypesPrincipalInfoType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_types_principal_info_type_0 = TypesPrincipalInfoType0.from_dict(data)

                return componentsschemas_types_principal_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TypesPrincipalInfoType0 | Unset, data)

        resolver = _parse_resolver(d.pop("resolver", UNSET))

        sub_order = d.pop("sub_order", UNSET)

        text = d.pop("text", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: EnumPullReqActivityType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = EnumPullReqActivityType(_type_)

        updated = d.pop("updated", UNSET)

        _user_group_mentions = d.pop("user_group_mentions", UNSET)
        user_group_mentions: TypesPullReqActivityUserGroupMentions | Unset
        if isinstance(_user_group_mentions, Unset):
            user_group_mentions = UNSET
        else:
            user_group_mentions = TypesPullReqActivityUserGroupMentions.from_dict(_user_group_mentions)

        types_pull_req_activity = cls(
            author=author,
            code_comment=code_comment,
            created=created,
            deleted=deleted,
            edited=edited,
            id=id,
            kind=kind,
            mentions=mentions,
            metadata=metadata,
            order=order,
            parent_id=parent_id,
            payload=payload,
            pullreq_id=pullreq_id,
            repo_id=repo_id,
            resolved=resolved,
            resolver=resolver,
            sub_order=sub_order,
            text=text,
            type_=type_,
            updated=updated,
            user_group_mentions=user_group_mentions,
        )

        types_pull_req_activity.additional_properties = d
        return types_pull_req_activity

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
