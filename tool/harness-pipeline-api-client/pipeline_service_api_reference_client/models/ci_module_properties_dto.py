from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ci_execution_info_dto import CIExecutionInfoDTO


T = TypeVar("T", bound="CIModulePropertiesDTO")


@_attrs_define
class CIModulePropertiesDTO:
    """
    Attributes:
        ci_execution_info_dto (CIExecutionInfoDTO | Unset):
        branch (str | Unset):
        build_type (str | Unset):
        tag (str | Unset):
        repo_name (str | Unset):
    """

    ci_execution_info_dto: CIExecutionInfoDTO | Unset = UNSET
    branch: str | Unset = UNSET
    build_type: str | Unset = UNSET
    tag: str | Unset = UNSET
    repo_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ci_execution_info_dto: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ci_execution_info_dto, Unset):
            ci_execution_info_dto = self.ci_execution_info_dto.to_dict()

        branch = self.branch

        build_type = self.build_type

        tag = self.tag

        repo_name = self.repo_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci_execution_info_dto is not UNSET:
            field_dict["ciExecutionInfoDTO"] = ci_execution_info_dto
        if branch is not UNSET:
            field_dict["branch"] = branch
        if build_type is not UNSET:
            field_dict["buildType"] = build_type
        if tag is not UNSET:
            field_dict["tag"] = tag
        if repo_name is not UNSET:
            field_dict["repoName"] = repo_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ci_execution_info_dto import CIExecutionInfoDTO

        d = dict(src_dict)
        _ci_execution_info_dto = d.pop("ciExecutionInfoDTO", UNSET)
        ci_execution_info_dto: CIExecutionInfoDTO | Unset
        if isinstance(_ci_execution_info_dto, Unset):
            ci_execution_info_dto = UNSET
        else:
            ci_execution_info_dto = CIExecutionInfoDTO.from_dict(_ci_execution_info_dto)

        branch = d.pop("branch", UNSET)

        build_type = d.pop("buildType", UNSET)

        tag = d.pop("tag", UNSET)

        repo_name = d.pop("repoName", UNSET)

        ci_module_properties_dto = cls(
            ci_execution_info_dto=ci_execution_info_dto,
            branch=branch,
            build_type=build_type,
            tag=tag,
            repo_name=repo_name,
        )

        ci_module_properties_dto.additional_properties = d
        return ci_module_properties_dto

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
