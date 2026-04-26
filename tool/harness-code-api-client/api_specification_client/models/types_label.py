from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_label_color import EnumLabelColor
from ..models.enum_label_type import EnumLabelType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesLabel")


@_attrs_define
class TypesLabel:
    """
    Attributes:
        color (EnumLabelColor | Unset):
        created (int | Unset):
        created_by (int | Unset):
        description (str | Unset):
        id (int | Unset):
        key (str | Unset):
        pullreq_count (int | Unset):
        repo_id (int | None | Unset):
        scope (int | Unset):
        space_id (int | None | Unset):
        type_ (EnumLabelType | Unset):
        updated (int | Unset):
        updated_by (int | Unset):
        value_count (int | Unset):
    """

    color: EnumLabelColor | Unset = UNSET
    created: int | Unset = UNSET
    created_by: int | Unset = UNSET
    description: str | Unset = UNSET
    id: int | Unset = UNSET
    key: str | Unset = UNSET
    pullreq_count: int | Unset = UNSET
    repo_id: int | None | Unset = UNSET
    scope: int | Unset = UNSET
    space_id: int | None | Unset = UNSET
    type_: EnumLabelType | Unset = UNSET
    updated: int | Unset = UNSET
    updated_by: int | Unset = UNSET
    value_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color: str | Unset = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.value

        created = self.created

        created_by = self.created_by

        description = self.description

        id = self.id

        key = self.key

        pullreq_count = self.pullreq_count

        repo_id: int | None | Unset
        if isinstance(self.repo_id, Unset):
            repo_id = UNSET
        else:
            repo_id = self.repo_id

        scope = self.scope

        space_id: int | None | Unset
        if isinstance(self.space_id, Unset):
            space_id = UNSET
        else:
            space_id = self.space_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated = self.updated

        updated_by = self.updated_by

        value_count = self.value_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if color is not UNSET:
            field_dict["color"] = color
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if pullreq_count is not UNSET:
            field_dict["pullreq_count"] = pullreq_count
        if repo_id is not UNSET:
            field_dict["repo_id"] = repo_id
        if scope is not UNSET:
            field_dict["scope"] = scope
        if space_id is not UNSET:
            field_dict["space_id"] = space_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated is not UNSET:
            field_dict["updated"] = updated
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if value_count is not UNSET:
            field_dict["value_count"] = value_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _color = d.pop("color", UNSET)
        color: EnumLabelColor | Unset
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = EnumLabelColor(_color)

        created = d.pop("created", UNSET)

        created_by = d.pop("created_by", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        pullreq_count = d.pop("pullreq_count", UNSET)

        def _parse_repo_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        repo_id = _parse_repo_id(d.pop("repo_id", UNSET))

        scope = d.pop("scope", UNSET)

        def _parse_space_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        space_id = _parse_space_id(d.pop("space_id", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: EnumLabelType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = EnumLabelType(_type_)

        updated = d.pop("updated", UNSET)

        updated_by = d.pop("updated_by", UNSET)

        value_count = d.pop("value_count", UNSET)

        types_label = cls(
            color=color,
            created=created,
            created_by=created_by,
            description=description,
            id=id,
            key=key,
            pullreq_count=pullreq_count,
            repo_id=repo_id,
            scope=scope,
            space_id=space_id,
            type_=type_,
            updated=updated,
            updated_by=updated_by,
            value_count=value_count,
        )

        types_label.additional_properties = d
        return types_label

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
