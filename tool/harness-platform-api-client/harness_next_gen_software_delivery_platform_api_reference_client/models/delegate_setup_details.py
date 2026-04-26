from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delegate_setup_details_size import DelegateSetupDetailsSize, check_delegate_setup_details_size
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.k8s_config_details import K8SConfigDetails


T = TypeVar("T", bound="DelegateSetupDetails")


@_attrs_define
class DelegateSetupDetails:
    """
    Attributes:
        name (str):
        delegate_type (str): Currently KUBERNETES and HELM_DELEGATE are supported.
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        description (str | Unset):
        size (DelegateSetupDetailsSize | Unset):
        host_name (str | Unset):
        delegate_configuration_id (str | Unset):
        identifier (str | Unset):
        k_8_s_config_details (K8SConfigDetails | Unset):
        tags (list[str] | Unset):
        token_name (str | Unset):
        run_as_root (bool | Unset):
        version (str | Unset):
    """

    name: str
    delegate_type: str
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    description: str | Unset = UNSET
    size: DelegateSetupDetailsSize | Unset = UNSET
    host_name: str | Unset = UNSET
    delegate_configuration_id: str | Unset = UNSET
    identifier: str | Unset = UNSET
    k_8_s_config_details: K8SConfigDetails | Unset = UNSET
    tags: list[str] | Unset = UNSET
    token_name: str | Unset = UNSET
    run_as_root: bool | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        delegate_type = self.delegate_type

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        description = self.description

        size: str | Unset = UNSET
        if not isinstance(self.size, Unset):
            size = self.size

        host_name = self.host_name

        delegate_configuration_id = self.delegate_configuration_id

        identifier = self.identifier

        k_8_s_config_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.k_8_s_config_details, Unset):
            k_8_s_config_details = self.k_8_s_config_details.to_dict()

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        token_name = self.token_name

        run_as_root = self.run_as_root

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "delegateType": delegate_type,
            }
        )
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if description is not UNSET:
            field_dict["description"] = description
        if size is not UNSET:
            field_dict["size"] = size
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if delegate_configuration_id is not UNSET:
            field_dict["delegateConfigurationId"] = delegate_configuration_id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if k_8_s_config_details is not UNSET:
            field_dict["k8sConfigDetails"] = k_8_s_config_details
        if tags is not UNSET:
            field_dict["tags"] = tags
        if token_name is not UNSET:
            field_dict["tokenName"] = token_name
        if run_as_root is not UNSET:
            field_dict["runAsRoot"] = run_as_root
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.k8s_config_details import K8SConfigDetails

        d = dict(src_dict)
        name = d.pop("name")

        delegate_type = d.pop("delegateType")

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        description = d.pop("description", UNSET)

        _size = d.pop("size", UNSET)
        size: DelegateSetupDetailsSize | Unset
        if isinstance(_size, Unset):
            size = UNSET
        else:
            size = check_delegate_setup_details_size(_size)

        host_name = d.pop("hostName", UNSET)

        delegate_configuration_id = d.pop("delegateConfigurationId", UNSET)

        identifier = d.pop("identifier", UNSET)

        _k_8_s_config_details = d.pop("k8sConfigDetails", UNSET)
        k_8_s_config_details: K8SConfigDetails | Unset
        if isinstance(_k_8_s_config_details, Unset):
            k_8_s_config_details = UNSET
        else:
            k_8_s_config_details = K8SConfigDetails.from_dict(_k_8_s_config_details)

        tags = cast(list[str], d.pop("tags", UNSET))

        token_name = d.pop("tokenName", UNSET)

        run_as_root = d.pop("runAsRoot", UNSET)

        version = d.pop("version", UNSET)

        delegate_setup_details = cls(
            name=name,
            delegate_type=delegate_type,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            description=description,
            size=size,
            host_name=host_name,
            delegate_configuration_id=delegate_configuration_id,
            identifier=identifier,
            k_8_s_config_details=k_8_s_config_details,
            tags=tags,
            token_name=token_name,
            run_as_root=run_as_root,
            version=version,
        )

        delegate_setup_details.additional_properties = d
        return delegate_setup_details

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
