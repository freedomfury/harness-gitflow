from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_with_git_info import EntityWithGitInfo


T = TypeVar("T", bound="InputSetTemplateRequest")


@_attrs_define
class InputSetTemplateRequest:
    """Contains Stage Identifiers to filter Runtime Input Template.

    Attributes:
        stage_identifiers (list[str] | Unset): List of Stage identifiers for which the Runtime Input template is needed
        service_with_git_info_list (list[EntityWithGitInfo] | Unset): Map of Service identifiers with their gitBranch
            for which the Runtime Input Metadata is needed
    """

    stage_identifiers: list[str] | Unset = UNSET
    service_with_git_info_list: list[EntityWithGitInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stage_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.stage_identifiers, Unset):
            stage_identifiers = self.stage_identifiers

        service_with_git_info_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.service_with_git_info_list, Unset):
            service_with_git_info_list = []
            for service_with_git_info_list_item_data in self.service_with_git_info_list:
                service_with_git_info_list_item = service_with_git_info_list_item_data.to_dict()
                service_with_git_info_list.append(service_with_git_info_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stage_identifiers is not UNSET:
            field_dict["stageIdentifiers"] = stage_identifiers
        if service_with_git_info_list is not UNSET:
            field_dict["serviceWithGitInfoList"] = service_with_git_info_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_with_git_info import EntityWithGitInfo

        d = dict(src_dict)
        stage_identifiers = cast(list[str], d.pop("stageIdentifiers", UNSET))

        _service_with_git_info_list = d.pop("serviceWithGitInfoList", UNSET)
        service_with_git_info_list: list[EntityWithGitInfo] | Unset = UNSET
        if _service_with_git_info_list is not UNSET:
            service_with_git_info_list = []
            for service_with_git_info_list_item_data in _service_with_git_info_list:
                service_with_git_info_list_item = EntityWithGitInfo.from_dict(service_with_git_info_list_item_data)

                service_with_git_info_list.append(service_with_git_info_list_item)

        input_set_template_request = cls(
            stage_identifiers=stage_identifiers,
            service_with_git_info_list=service_with_git_info_list,
        )

        input_set_template_request.additional_properties = d
        return input_set_template_request

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
