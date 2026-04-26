from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.gcp_oidc_token_request import GcpOidcTokenRequest


T = TypeVar("T", bound="GcpOidcAccessTokenRequest")


@_attrs_define
class GcpOidcAccessTokenRequest:
    """This contains GCP OIDC Access Token request details

    Attributes:
        oidc_id_token (str): The OIDC ID Token
        gcp_oidc_token_request_dto (GcpOidcTokenRequest): This contains GCP OIDC Token request details
    """

    oidc_id_token: str
    gcp_oidc_token_request_dto: GcpOidcTokenRequest
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        oidc_id_token = self.oidc_id_token

        gcp_oidc_token_request_dto = self.gcp_oidc_token_request_dto.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "oidcIdToken": oidc_id_token,
                "gcpOidcTokenRequestDTO": gcp_oidc_token_request_dto,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gcp_oidc_token_request import GcpOidcTokenRequest

        d = dict(src_dict)
        oidc_id_token = d.pop("oidcIdToken")

        gcp_oidc_token_request_dto = GcpOidcTokenRequest.from_dict(d.pop("gcpOidcTokenRequestDTO"))

        gcp_oidc_access_token_request = cls(
            oidc_id_token=oidc_id_token,
            gcp_oidc_token_request_dto=gcp_oidc_token_request_dto,
        )

        gcp_oidc_access_token_request.additional_properties = d
        return gcp_oidc_access_token_request

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
