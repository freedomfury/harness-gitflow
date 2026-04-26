from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.harness_connector_type import HarnessConnectorType, check_harness_connector_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.harness_api_access import HarnessApiAccess
    from ..models.harness_authentication import HarnessAuthentication


T = TypeVar("T", bound="HarnessConnector")


@_attrs_define
class HarnessConnector:
    """This contains details of Harness connectors

    Attributes:
        connector_type (str):
        url (str):
        authentication (HarnessAuthentication): This contains details of the information needed for Harness access
        type_ (HarnessConnectorType):
        validation_repo (str | Unset):
        api_access (HarnessApiAccess | Unset): This contains details of the information needed for Harness API access
        execute_on_delegate (bool | Unset):
        api_url (str | Unset):
        git_base_url (str | Unset):
        vanity_git_base_url (str | Unset):
        repo_ui_url (str | Unset):
        slug (str | Unset):
        account_id (str | Unset):
        project_id (str | Unset):
        org_id (str | Unset):
        api_external_url (str | Unset):
        scoped_repo_identifier (str | Unset):
        ignore_test_connection (bool | Unset):
    """

    connector_type: str
    url: str
    authentication: HarnessAuthentication
    type_: HarnessConnectorType
    validation_repo: str | Unset = UNSET
    api_access: HarnessApiAccess | Unset = UNSET
    execute_on_delegate: bool | Unset = UNSET
    api_url: str | Unset = UNSET
    git_base_url: str | Unset = UNSET
    vanity_git_base_url: str | Unset = UNSET
    repo_ui_url: str | Unset = UNSET
    slug: str | Unset = UNSET
    account_id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    org_id: str | Unset = UNSET
    api_external_url: str | Unset = UNSET
    scoped_repo_identifier: str | Unset = UNSET
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

        execute_on_delegate = self.execute_on_delegate

        api_url = self.api_url

        git_base_url = self.git_base_url

        vanity_git_base_url = self.vanity_git_base_url

        repo_ui_url = self.repo_ui_url

        slug = self.slug

        account_id = self.account_id

        project_id = self.project_id

        org_id = self.org_id

        api_external_url = self.api_external_url

        scoped_repo_identifier = self.scoped_repo_identifier

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
        if execute_on_delegate is not UNSET:
            field_dict["executeOnDelegate"] = execute_on_delegate
        if api_url is not UNSET:
            field_dict["apiUrl"] = api_url
        if git_base_url is not UNSET:
            field_dict["gitBaseUrl"] = git_base_url
        if vanity_git_base_url is not UNSET:
            field_dict["vanityGitBaseUrl"] = vanity_git_base_url
        if repo_ui_url is not UNSET:
            field_dict["repoUiUrl"] = repo_ui_url
        if slug is not UNSET:
            field_dict["slug"] = slug
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if org_id is not UNSET:
            field_dict["orgId"] = org_id
        if api_external_url is not UNSET:
            field_dict["apiExternalUrl"] = api_external_url
        if scoped_repo_identifier is not UNSET:
            field_dict["scopedRepoIdentifier"] = scoped_repo_identifier
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harness_api_access import HarnessApiAccess
        from ..models.harness_authentication import HarnessAuthentication

        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        url = d.pop("url")

        authentication = HarnessAuthentication.from_dict(d.pop("authentication"))

        type_ = check_harness_connector_type(d.pop("type"))

        validation_repo = d.pop("validationRepo", UNSET)

        _api_access = d.pop("apiAccess", UNSET)
        api_access: HarnessApiAccess | Unset
        if isinstance(_api_access, Unset):
            api_access = UNSET
        else:
            api_access = HarnessApiAccess.from_dict(_api_access)

        execute_on_delegate = d.pop("executeOnDelegate", UNSET)

        api_url = d.pop("apiUrl", UNSET)

        git_base_url = d.pop("gitBaseUrl", UNSET)

        vanity_git_base_url = d.pop("vanityGitBaseUrl", UNSET)

        repo_ui_url = d.pop("repoUiUrl", UNSET)

        slug = d.pop("slug", UNSET)

        account_id = d.pop("accountId", UNSET)

        project_id = d.pop("projectId", UNSET)

        org_id = d.pop("orgId", UNSET)

        api_external_url = d.pop("apiExternalUrl", UNSET)

        scoped_repo_identifier = d.pop("scopedRepoIdentifier", UNSET)

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        harness_connector = cls(
            connector_type=connector_type,
            url=url,
            authentication=authentication,
            type_=type_,
            validation_repo=validation_repo,
            api_access=api_access,
            execute_on_delegate=execute_on_delegate,
            api_url=api_url,
            git_base_url=git_base_url,
            vanity_git_base_url=vanity_git_base_url,
            repo_ui_url=repo_ui_url,
            slug=slug,
            account_id=account_id,
            project_id=project_id,
            org_id=org_id,
            api_external_url=api_external_url,
            scoped_repo_identifier=scoped_repo_identifier,
            ignore_test_connection=ignore_test_connection,
        )

        harness_connector.additional_properties = d
        return harness_connector

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
