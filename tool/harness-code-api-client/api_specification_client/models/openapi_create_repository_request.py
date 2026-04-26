from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_repo_tags_type_0 import TypesRepoTagsType0


T = TypeVar("T", bound="OpenapiCreateRepositoryRequest")


@_attrs_define
class OpenapiCreateRepositoryRequest:
    """
    Attributes:
        default_branch (str | Unset):
        description (str | Unset):
        git_ignore (str | Unset):
        identifier (str | Unset):
        is_public (bool | Unset):
        license_ (str | Unset):
        parent_ref (str | Unset):
        readme (bool | Unset):
        tags (None | TypesRepoTagsType0 | Unset):
        uid (str | Unset):
    """

    default_branch: str | Unset = UNSET
    description: str | Unset = UNSET
    git_ignore: str | Unset = UNSET
    identifier: str | Unset = UNSET
    is_public: bool | Unset = UNSET
    license_: str | Unset = UNSET
    parent_ref: str | Unset = UNSET
    readme: bool | Unset = UNSET
    tags: None | TypesRepoTagsType0 | Unset = UNSET
    uid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.types_repo_tags_type_0 import TypesRepoTagsType0

        default_branch = self.default_branch

        description = self.description

        git_ignore = self.git_ignore

        identifier = self.identifier

        is_public = self.is_public

        license_ = self.license_

        parent_ref = self.parent_ref

        readme = self.readme

        tags: dict[str, Any] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, TypesRepoTagsType0):
            tags = self.tags.to_dict()
        else:
            tags = self.tags

        uid = self.uid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_branch is not UNSET:
            field_dict["default_branch"] = default_branch
        if description is not UNSET:
            field_dict["description"] = description
        if git_ignore is not UNSET:
            field_dict["git_ignore"] = git_ignore
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if license_ is not UNSET:
            field_dict["license"] = license_
        if parent_ref is not UNSET:
            field_dict["parent_ref"] = parent_ref
        if readme is not UNSET:
            field_dict["readme"] = readme
        if tags is not UNSET:
            field_dict["tags"] = tags
        if uid is not UNSET:
            field_dict["uid"] = uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_repo_tags_type_0 import TypesRepoTagsType0

        d = dict(src_dict)
        default_branch = d.pop("default_branch", UNSET)

        description = d.pop("description", UNSET)

        git_ignore = d.pop("git_ignore", UNSET)

        identifier = d.pop("identifier", UNSET)

        is_public = d.pop("is_public", UNSET)

        license_ = d.pop("license", UNSET)

        parent_ref = d.pop("parent_ref", UNSET)

        readme = d.pop("readme", UNSET)

        def _parse_tags(data: object) -> None | TypesRepoTagsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_types_repo_tags_type_0 = TypesRepoTagsType0.from_dict(data)

                return componentsschemas_types_repo_tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TypesRepoTagsType0 | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        uid = d.pop("uid", UNSET)

        openapi_create_repository_request = cls(
            default_branch=default_branch,
            description=description,
            git_ignore=git_ignore,
            identifier=identifier,
            is_public=is_public,
            license_=license_,
            parent_ref=parent_ref,
            readme=readme,
            tags=tags,
            uid=uid,
        )

        openapi_create_repository_request.additional_properties = d
        return openapi_create_repository_request

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
