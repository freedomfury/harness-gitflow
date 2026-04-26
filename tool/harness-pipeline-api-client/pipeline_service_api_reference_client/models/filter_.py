from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.filter_filter_visibility import FilterFilterVisibility, check_filter_filter_visibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_properties import FilterProperties


T = TypeVar("T", bound="Filter")


@_attrs_define
class Filter:
    """This has details of the Filter entity defined in Harness

    Attributes:
        name (str): Name of the Filter.
        identifier (str): Identifier of the Filter.
        filter_properties (FilterProperties): Properties of the Filter entity defined in Harness.
        org_identifier (str | Unset): Organization Identifier for the Entity.
        project_identifier (str | Unset): Project Identifier for the Entity.
        filter_visibility (FilterFilterVisibility | Unset): This indicates visibility of Filter, by default it is
            Everyone.
    """

    name: str
    identifier: str
    filter_properties: FilterProperties
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    filter_visibility: FilterFilterVisibility | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        identifier = self.identifier

        filter_properties = self.filter_properties.to_dict()

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        filter_visibility: str | Unset = UNSET
        if not isinstance(self.filter_visibility, Unset):
            filter_visibility = self.filter_visibility

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "identifier": identifier,
                "filterProperties": filter_properties,
            }
        )
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if filter_visibility is not UNSET:
            field_dict["filterVisibility"] = filter_visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_properties import FilterProperties

        d = dict(src_dict)
        name = d.pop("name")

        identifier = d.pop("identifier")

        filter_properties = FilterProperties.from_dict(d.pop("filterProperties"))

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        _filter_visibility = d.pop("filterVisibility", UNSET)
        filter_visibility: FilterFilterVisibility | Unset
        if isinstance(_filter_visibility, Unset):
            filter_visibility = UNSET
        else:
            filter_visibility = check_filter_filter_visibility(_filter_visibility)

        filter_ = cls(
            name=name,
            identifier=identifier,
            filter_properties=filter_properties,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            filter_visibility=filter_visibility,
        )

        filter_.additional_properties = d
        return filter_

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
