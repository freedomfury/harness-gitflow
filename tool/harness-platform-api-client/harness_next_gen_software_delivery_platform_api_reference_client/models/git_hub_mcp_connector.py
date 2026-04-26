from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.git_hub_mcp_authentication_dto import GitHubMcpAuthenticationDTO


T = TypeVar("T", bound="GitHubMcpConnector")


@_attrs_define
class GitHubMcpConnector:
    """GitHub MCP Server connector

    Attributes:
        connector_type (str):
        url (str):
        auth (GitHubMcpAuthenticationDTO | Unset): GitHub MCP Server Authentication
        delegate_selectors (list[str] | Unset):
        ignore_test_connection (bool | Unset):
        execute_on_delegate (bool | Unset):
    """

    connector_type: str
    url: str
    auth: GitHubMcpAuthenticationDTO | Unset = UNSET
    delegate_selectors: list[str] | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    execute_on_delegate: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        url = self.url

        auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth, Unset):
            auth = self.auth.to_dict()

        delegate_selectors: list[str] | Unset = UNSET
        if not isinstance(self.delegate_selectors, Unset):
            delegate_selectors = self.delegate_selectors

        ignore_test_connection = self.ignore_test_connection

        execute_on_delegate = self.execute_on_delegate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
                "url": url,
            }
        )
        if auth is not UNSET:
            field_dict["auth"] = auth
        if delegate_selectors is not UNSET:
            field_dict["delegateSelectors"] = delegate_selectors
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection
        if execute_on_delegate is not UNSET:
            field_dict["executeOnDelegate"] = execute_on_delegate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.git_hub_mcp_authentication_dto import GitHubMcpAuthenticationDTO

        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        url = d.pop("url")

        _auth = d.pop("auth", UNSET)
        auth: GitHubMcpAuthenticationDTO | Unset
        if isinstance(_auth, Unset):
            auth = UNSET
        else:
            auth = GitHubMcpAuthenticationDTO.from_dict(_auth)

        delegate_selectors = cast(list[str], d.pop("delegateSelectors", UNSET))

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        execute_on_delegate = d.pop("executeOnDelegate", UNSET)

        git_hub_mcp_connector = cls(
            connector_type=connector_type,
            url=url,
            auth=auth,
            delegate_selectors=delegate_selectors,
            ignore_test_connection=ignore_test_connection,
            execute_on_delegate=execute_on_delegate,
        )

        git_hub_mcp_connector.additional_properties = d
        return git_hub_mcp_connector

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
