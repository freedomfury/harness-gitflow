from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_repository_core import TypesRepositoryCore


T = TypeVar("T", bound="RepoRepositoryOutput")


@_attrs_define
class RepoRepositoryOutput:
    """
    Attributes:
        archived (bool | Unset):
        created (int | Unset):
        created_by (int | Unset):
        default_branch (str | Unset):
        deleted (int | None | Unset):
        description (str | Unset):
        fork_id (int | Unset):
        git_ssh_url (str | Unset):
        git_url (str | Unset):
        id (int | Unset):
        identifier (str | Unset):
        importing (bool | Unset):
        is_empty (bool | Unset):
        is_favorite (bool | Unset):
        is_public (bool | Unset):
        language (str | Unset):
        last_git_push (int | Unset):
        num_closed_pulls (int | Unset):
        num_forks (int | Unset):
        num_merged_pulls (int | Unset):
        num_open_pulls (int | Unset):
        num_pulls (int | Unset):
        parent_id (int | Unset):
        path (str | Unset):
        repo_type (str | Unset):
        size (int | Unset): size of the repository in KiB
        size_lfs (int | Unset): size of the repository LFS in KiB
        size_updated (int | Unset):
        state (int | None | Unset):
        tags (Any | Unset):
        updated (int | Unset):
        upstream (TypesRepositoryCore | Unset):
    """

    archived: bool | Unset = UNSET
    created: int | Unset = UNSET
    created_by: int | Unset = UNSET
    default_branch: str | Unset = UNSET
    deleted: int | None | Unset = UNSET
    description: str | Unset = UNSET
    fork_id: int | Unset = UNSET
    git_ssh_url: str | Unset = UNSET
    git_url: str | Unset = UNSET
    id: int | Unset = UNSET
    identifier: str | Unset = UNSET
    importing: bool | Unset = UNSET
    is_empty: bool | Unset = UNSET
    is_favorite: bool | Unset = UNSET
    is_public: bool | Unset = UNSET
    language: str | Unset = UNSET
    last_git_push: int | Unset = UNSET
    num_closed_pulls: int | Unset = UNSET
    num_forks: int | Unset = UNSET
    num_merged_pulls: int | Unset = UNSET
    num_open_pulls: int | Unset = UNSET
    num_pulls: int | Unset = UNSET
    parent_id: int | Unset = UNSET
    path: str | Unset = UNSET
    repo_type: str | Unset = UNSET
    size: int | Unset = UNSET
    size_lfs: int | Unset = UNSET
    size_updated: int | Unset = UNSET
    state: int | None | Unset = UNSET
    tags: Any | Unset = UNSET
    updated: int | Unset = UNSET
    upstream: TypesRepositoryCore | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        archived = self.archived

        created = self.created

        created_by = self.created_by

        default_branch = self.default_branch

        deleted: int | None | Unset
        if isinstance(self.deleted, Unset):
            deleted = UNSET
        else:
            deleted = self.deleted

        description = self.description

        fork_id = self.fork_id

        git_ssh_url = self.git_ssh_url

        git_url = self.git_url

        id = self.id

        identifier = self.identifier

        importing = self.importing

        is_empty = self.is_empty

        is_favorite = self.is_favorite

        is_public = self.is_public

        language = self.language

        last_git_push = self.last_git_push

        num_closed_pulls = self.num_closed_pulls

        num_forks = self.num_forks

        num_merged_pulls = self.num_merged_pulls

        num_open_pulls = self.num_open_pulls

        num_pulls = self.num_pulls

        parent_id = self.parent_id

        path = self.path

        repo_type = self.repo_type

        size = self.size

        size_lfs = self.size_lfs

        size_updated = self.size_updated

        state: int | None | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        tags = self.tags

        updated = self.updated

        upstream: dict[str, Any] | Unset = UNSET
        if not isinstance(self.upstream, Unset):
            upstream = self.upstream.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if archived is not UNSET:
            field_dict["archived"] = archived
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if default_branch is not UNSET:
            field_dict["default_branch"] = default_branch
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if description is not UNSET:
            field_dict["description"] = description
        if fork_id is not UNSET:
            field_dict["fork_id"] = fork_id
        if git_ssh_url is not UNSET:
            field_dict["git_ssh_url"] = git_ssh_url
        if git_url is not UNSET:
            field_dict["git_url"] = git_url
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if importing is not UNSET:
            field_dict["importing"] = importing
        if is_empty is not UNSET:
            field_dict["is_empty"] = is_empty
        if is_favorite is not UNSET:
            field_dict["is_favorite"] = is_favorite
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if language is not UNSET:
            field_dict["language"] = language
        if last_git_push is not UNSET:
            field_dict["last_git_push"] = last_git_push
        if num_closed_pulls is not UNSET:
            field_dict["num_closed_pulls"] = num_closed_pulls
        if num_forks is not UNSET:
            field_dict["num_forks"] = num_forks
        if num_merged_pulls is not UNSET:
            field_dict["num_merged_pulls"] = num_merged_pulls
        if num_open_pulls is not UNSET:
            field_dict["num_open_pulls"] = num_open_pulls
        if num_pulls is not UNSET:
            field_dict["num_pulls"] = num_pulls
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if path is not UNSET:
            field_dict["path"] = path
        if repo_type is not UNSET:
            field_dict["repo_type"] = repo_type
        if size is not UNSET:
            field_dict["size"] = size
        if size_lfs is not UNSET:
            field_dict["size_lfs"] = size_lfs
        if size_updated is not UNSET:
            field_dict["size_updated"] = size_updated
        if state is not UNSET:
            field_dict["state"] = state
        if tags is not UNSET:
            field_dict["tags"] = tags
        if updated is not UNSET:
            field_dict["updated"] = updated
        if upstream is not UNSET:
            field_dict["upstream"] = upstream

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_repository_core import TypesRepositoryCore

        d = dict(src_dict)
        archived = d.pop("archived", UNSET)

        created = d.pop("created", UNSET)

        created_by = d.pop("created_by", UNSET)

        default_branch = d.pop("default_branch", UNSET)

        def _parse_deleted(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        deleted = _parse_deleted(d.pop("deleted", UNSET))

        description = d.pop("description", UNSET)

        fork_id = d.pop("fork_id", UNSET)

        git_ssh_url = d.pop("git_ssh_url", UNSET)

        git_url = d.pop("git_url", UNSET)

        id = d.pop("id", UNSET)

        identifier = d.pop("identifier", UNSET)

        importing = d.pop("importing", UNSET)

        is_empty = d.pop("is_empty", UNSET)

        is_favorite = d.pop("is_favorite", UNSET)

        is_public = d.pop("is_public", UNSET)

        language = d.pop("language", UNSET)

        last_git_push = d.pop("last_git_push", UNSET)

        num_closed_pulls = d.pop("num_closed_pulls", UNSET)

        num_forks = d.pop("num_forks", UNSET)

        num_merged_pulls = d.pop("num_merged_pulls", UNSET)

        num_open_pulls = d.pop("num_open_pulls", UNSET)

        num_pulls = d.pop("num_pulls", UNSET)

        parent_id = d.pop("parent_id", UNSET)

        path = d.pop("path", UNSET)

        repo_type = d.pop("repo_type", UNSET)

        size = d.pop("size", UNSET)

        size_lfs = d.pop("size_lfs", UNSET)

        size_updated = d.pop("size_updated", UNSET)

        def _parse_state(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        tags = d.pop("tags", UNSET)

        updated = d.pop("updated", UNSET)

        _upstream = d.pop("upstream", UNSET)
        upstream: TypesRepositoryCore | Unset
        if isinstance(_upstream, Unset):
            upstream = UNSET
        else:
            upstream = TypesRepositoryCore.from_dict(_upstream)

        repo_repository_output = cls(
            archived=archived,
            created=created,
            created_by=created_by,
            default_branch=default_branch,
            deleted=deleted,
            description=description,
            fork_id=fork_id,
            git_ssh_url=git_ssh_url,
            git_url=git_url,
            id=id,
            identifier=identifier,
            importing=importing,
            is_empty=is_empty,
            is_favorite=is_favorite,
            is_public=is_public,
            language=language,
            last_git_push=last_git_push,
            num_closed_pulls=num_closed_pulls,
            num_forks=num_forks,
            num_merged_pulls=num_merged_pulls,
            num_open_pulls=num_open_pulls,
            num_pulls=num_pulls,
            parent_id=parent_id,
            path=path,
            repo_type=repo_type,
            size=size,
            size_lfs=size_lfs,
            size_updated=size_updated,
            state=state,
            tags=tags,
            updated=updated,
            upstream=upstream,
        )

        repo_repository_output.additional_properties = d
        return repo_repository_output

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
