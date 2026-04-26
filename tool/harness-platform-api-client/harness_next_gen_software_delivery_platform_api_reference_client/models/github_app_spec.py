from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubAppSpec")


@_attrs_define
class GithubAppSpec:
    """This contains details of the Github API access credentials Specs such as references of private key

    Attributes:
        private_key_ref (str):
        installation_id (str | Unset):
        application_id (str | Unset):
        installation_id_ref (str | Unset):
        application_id_ref (str | Unset):
    """

    private_key_ref: str
    installation_id: str | Unset = UNSET
    application_id: str | Unset = UNSET
    installation_id_ref: str | Unset = UNSET
    application_id_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        private_key_ref = self.private_key_ref

        installation_id = self.installation_id

        application_id = self.application_id

        installation_id_ref = self.installation_id_ref

        application_id_ref = self.application_id_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "privateKeyRef": private_key_ref,
            }
        )
        if installation_id is not UNSET:
            field_dict["installationId"] = installation_id
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if installation_id_ref is not UNSET:
            field_dict["installationIdRef"] = installation_id_ref
        if application_id_ref is not UNSET:
            field_dict["applicationIdRef"] = application_id_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        private_key_ref = d.pop("privateKeyRef")

        installation_id = d.pop("installationId", UNSET)

        application_id = d.pop("applicationId", UNSET)

        installation_id_ref = d.pop("installationIdRef", UNSET)

        application_id_ref = d.pop("applicationIdRef", UNSET)

        github_app_spec = cls(
            private_key_ref=private_key_ref,
            installation_id=installation_id,
            application_id=application_id,
            installation_id_ref=installation_id_ref,
            application_id_ref=application_id_ref,
        )

        github_app_spec.additional_properties = d
        return github_app_spec

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
