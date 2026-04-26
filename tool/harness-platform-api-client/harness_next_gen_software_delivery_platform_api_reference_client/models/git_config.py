from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.git_config_connection_type import GitConfigConnectionType, check_git_config_connection_type
from ..models.git_config_type import GitConfigType, check_git_config_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.git_authentication import GitAuthentication


T = TypeVar("T", bound="GitConfig")


@_attrs_define
class GitConfig:
    """This contains details of the Generic Git connector

    Attributes:
        connector_type (str):
        url (str):
        type_ (GitConfigType):
        connection_type (GitConfigConnectionType):
        spec (GitAuthentication): This is a interface for details of the Generic Git authentication information
        validation_repo (str | Unset):
        branch_name (str | Unset):
        delegate_selectors (list[str] | Unset):
        execute_on_delegate (bool | Unset):
        is_anonymous (bool | Unset):
        proxy (bool | Unset):
        ignore_test_connection (bool | Unset):
    """

    connector_type: str
    url: str
    type_: GitConfigType
    connection_type: GitConfigConnectionType
    spec: GitAuthentication
    validation_repo: str | Unset = UNSET
    branch_name: str | Unset = UNSET
    delegate_selectors: list[str] | Unset = UNSET
    execute_on_delegate: bool | Unset = UNSET
    is_anonymous: bool | Unset = UNSET
    proxy: bool | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        url = self.url

        type_: str = self.type_

        connection_type: str = self.connection_type

        spec = self.spec.to_dict()

        validation_repo = self.validation_repo

        branch_name = self.branch_name

        delegate_selectors: list[str] | Unset = UNSET
        if not isinstance(self.delegate_selectors, Unset):
            delegate_selectors = self.delegate_selectors

        execute_on_delegate = self.execute_on_delegate

        is_anonymous = self.is_anonymous

        proxy = self.proxy

        ignore_test_connection = self.ignore_test_connection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
                "url": url,
                "type": type_,
                "connectionType": connection_type,
                "spec": spec,
            }
        )
        if validation_repo is not UNSET:
            field_dict["validationRepo"] = validation_repo
        if branch_name is not UNSET:
            field_dict["branchName"] = branch_name
        if delegate_selectors is not UNSET:
            field_dict["delegateSelectors"] = delegate_selectors
        if execute_on_delegate is not UNSET:
            field_dict["executeOnDelegate"] = execute_on_delegate
        if is_anonymous is not UNSET:
            field_dict["isAnonymous"] = is_anonymous
        if proxy is not UNSET:
            field_dict["proxy"] = proxy
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.git_authentication import GitAuthentication

        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        url = d.pop("url")

        type_ = check_git_config_type(d.pop("type"))

        connection_type = check_git_config_connection_type(d.pop("connectionType"))

        spec = GitAuthentication.from_dict(d.pop("spec"))

        validation_repo = d.pop("validationRepo", UNSET)

        branch_name = d.pop("branchName", UNSET)

        delegate_selectors = cast(list[str], d.pop("delegateSelectors", UNSET))

        execute_on_delegate = d.pop("executeOnDelegate", UNSET)

        is_anonymous = d.pop("isAnonymous", UNSET)

        proxy = d.pop("proxy", UNSET)

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        git_config = cls(
            connector_type=connector_type,
            url=url,
            type_=type_,
            connection_type=connection_type,
            spec=spec,
            validation_repo=validation_repo,
            branch_name=branch_name,
            delegate_selectors=delegate_selectors,
            execute_on_delegate=execute_on_delegate,
            is_anonymous=is_anonymous,
            proxy=proxy,
            ignore_test_connection=ignore_test_connection,
        )

        git_config.additional_properties = d
        return git_config

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
