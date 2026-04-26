from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.oidc_access_token_options import OidcAccessTokenOptions


T = TypeVar("T", bound="OidcWorkloadAccessTokenRequest")


@_attrs_define
class OidcWorkloadAccessTokenRequest:
    """
    Attributes:
        audience (str | Unset):
        grant_type (str | Unset):
        requested_token_type (str | Unset):
        scope (str | Unset):
        subject_token_type (str | Unset):
        subject_token (str | Unset):
        options (OidcAccessTokenOptions | Unset):
    """

    audience: str | Unset = UNSET
    grant_type: str | Unset = UNSET
    requested_token_type: str | Unset = UNSET
    scope: str | Unset = UNSET
    subject_token_type: str | Unset = UNSET
    subject_token: str | Unset = UNSET
    options: OidcAccessTokenOptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audience = self.audience

        grant_type = self.grant_type

        requested_token_type = self.requested_token_type

        scope = self.scope

        subject_token_type = self.subject_token_type

        subject_token = self.subject_token

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if audience is not UNSET:
            field_dict["audience"] = audience
        if grant_type is not UNSET:
            field_dict["grant_type"] = grant_type
        if requested_token_type is not UNSET:
            field_dict["requested_token_type"] = requested_token_type
        if scope is not UNSET:
            field_dict["scope"] = scope
        if subject_token_type is not UNSET:
            field_dict["subject_token_type"] = subject_token_type
        if subject_token is not UNSET:
            field_dict["subject_token"] = subject_token
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.oidc_access_token_options import OidcAccessTokenOptions

        d = dict(src_dict)
        audience = d.pop("audience", UNSET)

        grant_type = d.pop("grant_type", UNSET)

        requested_token_type = d.pop("requested_token_type", UNSET)

        scope = d.pop("scope", UNSET)

        subject_token_type = d.pop("subject_token_type", UNSET)

        subject_token = d.pop("subject_token", UNSET)

        _options = d.pop("options", UNSET)
        options: OidcAccessTokenOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = OidcAccessTokenOptions.from_dict(_options)

        oidc_workload_access_token_request = cls(
            audience=audience,
            grant_type=grant_type,
            requested_token_type=requested_token_type,
            scope=scope,
            subject_token_type=subject_token_type,
            subject_token=subject_token,
            options=options,
        )

        oidc_workload_access_token_request.additional_properties = d
        return oidc_workload_access_token_request

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
