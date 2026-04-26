from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.login_type_response_authentication_mechanism import (
    LoginTypeResponseAuthenticationMechanism,
    check_login_type_response_authentication_mechanism,
)
from ..models.login_type_response_default_experience import (
    LoginTypeResponseDefaultExperience,
    check_login_type_response_default_experience,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sso_request import SSORequest


T = TypeVar("T", bound="LoginTypeResponse")


@_attrs_define
class LoginTypeResponse:
    """
    Attributes:
        authentication_mechanism (LoginTypeResponseAuthenticationMechanism | Unset):
        show_captcha (bool | Unset):
        default_experience (LoginTypeResponseDefaultExperience | Unset):
        ssorequest (SSORequest | Unset):
        oauth_enabled (bool | Unset):
    """

    authentication_mechanism: LoginTypeResponseAuthenticationMechanism | Unset = UNSET
    show_captcha: bool | Unset = UNSET
    default_experience: LoginTypeResponseDefaultExperience | Unset = UNSET
    ssorequest: SSORequest | Unset = UNSET
    oauth_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authentication_mechanism: str | Unset = UNSET
        if not isinstance(self.authentication_mechanism, Unset):
            authentication_mechanism = self.authentication_mechanism

        show_captcha = self.show_captcha

        default_experience: str | Unset = UNSET
        if not isinstance(self.default_experience, Unset):
            default_experience = self.default_experience

        ssorequest: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ssorequest, Unset):
            ssorequest = self.ssorequest.to_dict()

        oauth_enabled = self.oauth_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authentication_mechanism is not UNSET:
            field_dict["authenticationMechanism"] = authentication_mechanism
        if show_captcha is not UNSET:
            field_dict["showCaptcha"] = show_captcha
        if default_experience is not UNSET:
            field_dict["defaultExperience"] = default_experience
        if ssorequest is not UNSET:
            field_dict["ssorequest"] = ssorequest
        if oauth_enabled is not UNSET:
            field_dict["oauthEnabled"] = oauth_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sso_request import SSORequest

        d = dict(src_dict)
        _authentication_mechanism = d.pop("authenticationMechanism", UNSET)
        authentication_mechanism: LoginTypeResponseAuthenticationMechanism | Unset
        if isinstance(_authentication_mechanism, Unset):
            authentication_mechanism = UNSET
        else:
            authentication_mechanism = check_login_type_response_authentication_mechanism(_authentication_mechanism)

        show_captcha = d.pop("showCaptcha", UNSET)

        _default_experience = d.pop("defaultExperience", UNSET)
        default_experience: LoginTypeResponseDefaultExperience | Unset
        if isinstance(_default_experience, Unset):
            default_experience = UNSET
        else:
            default_experience = check_login_type_response_default_experience(_default_experience)

        _ssorequest = d.pop("ssorequest", UNSET)
        ssorequest: SSORequest | Unset
        if isinstance(_ssorequest, Unset):
            ssorequest = UNSET
        else:
            ssorequest = SSORequest.from_dict(_ssorequest)

        oauth_enabled = d.pop("oauthEnabled", UNSET)

        login_type_response = cls(
            authentication_mechanism=authentication_mechanism,
            show_captcha=show_captcha,
            default_experience=default_experience,
            ssorequest=ssorequest,
            oauth_enabled=oauth_enabled,
        )

        login_type_response.additional_properties = d
        return login_type_response

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
