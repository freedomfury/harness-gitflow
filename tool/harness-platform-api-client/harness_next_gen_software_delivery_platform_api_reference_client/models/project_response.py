from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project import Project


T = TypeVar("T", bound="ProjectResponse")


@_attrs_define
class ProjectResponse:
    """This has Project details along with its metadata as defined in Harness .

    Attributes:
        project (Project): This is the Project Entity details defined in Harness
        is_favorite (bool):
        created_at (int | Unset): This specifies the time at which project was created.
        last_modified_at (int | Unset): This specifies the time at which project was last modified.
        last_moved_at (int | Unset): This specifies the time at which project was last moved across scopes.
    """

    project: Project
    is_favorite: bool
    created_at: int | Unset = UNSET
    last_modified_at: int | Unset = UNSET
    last_moved_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project = self.project.to_dict()

        is_favorite = self.is_favorite

        created_at = self.created_at

        last_modified_at = self.last_modified_at

        last_moved_at = self.last_moved_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project": project,
                "isFavorite": is_favorite,
            }
        )
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if last_modified_at is not UNSET:
            field_dict["lastModifiedAt"] = last_modified_at
        if last_moved_at is not UNSET:
            field_dict["lastMovedAt"] = last_moved_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project import Project

        d = dict(src_dict)
        project = Project.from_dict(d.pop("project"))

        is_favorite = d.pop("isFavorite")

        created_at = d.pop("createdAt", UNSET)

        last_modified_at = d.pop("lastModifiedAt", UNSET)

        last_moved_at = d.pop("lastMovedAt", UNSET)

        project_response = cls(
            project=project,
            is_favorite=is_favorite,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_moved_at=last_moved_at,
        )

        project_response.additional_properties = d
        return project_response

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
