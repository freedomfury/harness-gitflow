from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_link_config_for_custom_secret_manager import TemplateLinkConfigForCustomSecretManager


T = TypeVar("T", bound="CustomSecretManager")


@_attrs_define
class CustomSecretManager:
    """This contains details of Custom Secret Manager connectors

    Attributes:
        connector_type (str):
        template (TemplateLinkConfigForCustomSecretManager):
        delegate_selectors (list[str] | Unset):
        on_delegate (bool | Unset):
        connector_ref (str | Unset): This is the authentication token used to connect underlying secret manager.
        host (str | Unset):
        working_directory (str | Unset):
        timeout (int | Unset):
        ignore_test_connection (bool | Unset):
        default (bool | Unset):
    """

    connector_type: str
    template: TemplateLinkConfigForCustomSecretManager
    delegate_selectors: list[str] | Unset = UNSET
    on_delegate: bool | Unset = UNSET
    connector_ref: str | Unset = UNSET
    host: str | Unset = UNSET
    working_directory: str | Unset = UNSET
    timeout: int | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    default: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        template = self.template.to_dict()

        delegate_selectors: list[str] | Unset = UNSET
        if not isinstance(self.delegate_selectors, Unset):
            delegate_selectors = self.delegate_selectors

        on_delegate = self.on_delegate

        connector_ref = self.connector_ref

        host = self.host

        working_directory = self.working_directory

        timeout = self.timeout

        ignore_test_connection = self.ignore_test_connection

        default = self.default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
                "template": template,
            }
        )
        if delegate_selectors is not UNSET:
            field_dict["delegateSelectors"] = delegate_selectors
        if on_delegate is not UNSET:
            field_dict["onDelegate"] = on_delegate
        if connector_ref is not UNSET:
            field_dict["connectorRef"] = connector_ref
        if host is not UNSET:
            field_dict["host"] = host
        if working_directory is not UNSET:
            field_dict["workingDirectory"] = working_directory
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection
        if default is not UNSET:
            field_dict["default"] = default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_link_config_for_custom_secret_manager import TemplateLinkConfigForCustomSecretManager

        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        template = TemplateLinkConfigForCustomSecretManager.from_dict(d.pop("template"))

        delegate_selectors = cast(list[str], d.pop("delegateSelectors", UNSET))

        on_delegate = d.pop("onDelegate", UNSET)

        connector_ref = d.pop("connectorRef", UNSET)

        host = d.pop("host", UNSET)

        working_directory = d.pop("workingDirectory", UNSET)

        timeout = d.pop("timeout", UNSET)

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        default = d.pop("default", UNSET)

        custom_secret_manager = cls(
            connector_type=connector_type,
            template=template,
            delegate_selectors=delegate_selectors,
            on_delegate=on_delegate,
            connector_ref=connector_ref,
            host=host,
            working_directory=working_directory,
            timeout=timeout,
            ignore_test_connection=ignore_test_connection,
            default=default,
        )

        custom_secret_manager.additional_properties = d
        return custom_secret_manager

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
