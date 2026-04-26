from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.azure_repo_api_access_type import AzureRepoApiAccessType, check_azure_repo_api_access_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_repo_api_access_spec import AzureRepoApiAccessSpec


T = TypeVar("T", bound="AzureRepoApiAccess")


@_attrs_define
class AzureRepoApiAccess:
    """This contains details of the information needed for Azure Repo API access

    Attributes:
        type_ (AzureRepoApiAccessType):
        spec (AzureRepoApiAccessSpec | Unset): This contains details of the information such as references of username
            and password needed for Azure Repo API access
    """

    type_: AzureRepoApiAccessType
    spec: AzureRepoApiAccessSpec | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if spec is not UNSET:
            field_dict["spec"] = spec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_repo_api_access_spec import AzureRepoApiAccessSpec

        d = dict(src_dict)
        type_ = check_azure_repo_api_access_type(d.pop("type"))

        _spec = d.pop("spec", UNSET)
        spec: AzureRepoApiAccessSpec | Unset
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = AzureRepoApiAccessSpec.from_dict(_spec)

        azure_repo_api_access = cls(
            type_=type_,
            spec=spec,
        )

        azure_repo_api_access.additional_properties = d
        return azure_repo_api_access

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
