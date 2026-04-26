from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cd_module_properties_dto import CDModulePropertiesDTO
    from ..models.ci_module_properties_dto import CIModulePropertiesDTO


T = TypeVar("T", bound="ModulePropertiesDTO")


@_attrs_define
class ModulePropertiesDTO:
    """Module-specific filter properties (e.g. CD service/environment filters, CI build event filters).

    Attributes:
        cd (CDModulePropertiesDTO | Unset):
        ci (CIModulePropertiesDTO | Unset):
    """

    cd: CDModulePropertiesDTO | Unset = UNSET
    ci: CIModulePropertiesDTO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cd: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cd, Unset):
            cd = self.cd.to_dict()

        ci: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cd is not UNSET:
            field_dict["cd"] = cd
        if ci is not UNSET:
            field_dict["ci"] = ci

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cd_module_properties_dto import CDModulePropertiesDTO
        from ..models.ci_module_properties_dto import CIModulePropertiesDTO

        d = dict(src_dict)
        _cd = d.pop("cd", UNSET)
        cd: CDModulePropertiesDTO | Unset
        if isinstance(_cd, Unset):
            cd = UNSET
        else:
            cd = CDModulePropertiesDTO.from_dict(_cd)

        _ci = d.pop("ci", UNSET)
        ci: CIModulePropertiesDTO | Unset
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = CIModulePropertiesDTO.from_dict(_ci)

        module_properties_dto = cls(
            cd=cd,
            ci=ci,
        )

        module_properties_dto.additional_properties = d
        return module_properties_dto

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
