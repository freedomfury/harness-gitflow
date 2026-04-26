from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.azure_repo_config_type import AzureRepoConfigType, check_azure_repo_config_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_repo_api_access import AzureRepoApiAccess
    from ..models.azure_repo_authentication import AzureRepoAuthentication


T = TypeVar("T", bound="AzureRepoConfig")


@_attrs_define
class AzureRepoConfig:
    """This contains details of AzureRepo connector

    Attributes:
        connector_type (str):
        url (str): SSH | HTTP URL based on type of connection
        authentication (AzureRepoAuthentication): This contains details of the information needed for Azure DevOps
            access
        type_ (AzureRepoConfigType): Project | Repository connector type
        validation_repo (str | Unset): The repo to validate AzureRepo credentials. Only valid for Account type connector
        api_access (AzureRepoApiAccess | Unset): This contains details of the information needed for Azure Repo API
            access
        delegate_selectors (list[str] | Unset): Selected Connectivity Modes
        execute_on_delegate (bool | Unset):
        ignore_test_connection (bool | Unset):
    """

    connector_type: str
    url: str
    authentication: AzureRepoAuthentication
    type_: AzureRepoConfigType
    validation_repo: str | Unset = UNSET
    api_access: AzureRepoApiAccess | Unset = UNSET
    delegate_selectors: list[str] | Unset = UNSET
    execute_on_delegate: bool | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        url = self.url

        authentication = self.authentication.to_dict()

        type_: str = self.type_

        validation_repo = self.validation_repo

        api_access: dict[str, Any] | Unset = UNSET
        if not isinstance(self.api_access, Unset):
            api_access = self.api_access.to_dict()

        delegate_selectors: list[str] | Unset = UNSET
        if not isinstance(self.delegate_selectors, Unset):
            delegate_selectors = self.delegate_selectors

        execute_on_delegate = self.execute_on_delegate

        ignore_test_connection = self.ignore_test_connection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
                "url": url,
                "authentication": authentication,
                "type": type_,
            }
        )
        if validation_repo is not UNSET:
            field_dict["validationRepo"] = validation_repo
        if api_access is not UNSET:
            field_dict["apiAccess"] = api_access
        if delegate_selectors is not UNSET:
            field_dict["delegateSelectors"] = delegate_selectors
        if execute_on_delegate is not UNSET:
            field_dict["executeOnDelegate"] = execute_on_delegate
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_repo_api_access import AzureRepoApiAccess
        from ..models.azure_repo_authentication import AzureRepoAuthentication

        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        url = d.pop("url")

        authentication = AzureRepoAuthentication.from_dict(d.pop("authentication"))

        type_ = check_azure_repo_config_type(d.pop("type"))

        validation_repo = d.pop("validationRepo", UNSET)

        _api_access = d.pop("apiAccess", UNSET)
        api_access: AzureRepoApiAccess | Unset
        if isinstance(_api_access, Unset):
            api_access = UNSET
        else:
            api_access = AzureRepoApiAccess.from_dict(_api_access)

        delegate_selectors = cast(list[str], d.pop("delegateSelectors", UNSET))

        execute_on_delegate = d.pop("executeOnDelegate", UNSET)

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        azure_repo_config = cls(
            connector_type=connector_type,
            url=url,
            authentication=authentication,
            type_=type_,
            validation_repo=validation_repo,
            api_access=api_access,
            delegate_selectors=delegate_selectors,
            execute_on_delegate=execute_on_delegate,
            ignore_test_connection=ignore_test_connection,
        )

        azure_repo_config.additional_properties = d
        return azure_repo_config

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
