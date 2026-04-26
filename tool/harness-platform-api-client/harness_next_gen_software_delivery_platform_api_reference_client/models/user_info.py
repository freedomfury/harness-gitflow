from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_account_request import GatewayAccountRequest
    from ..models.user_info_user_preferences import UserInfoUserPreferences
    from ..models.utm_info import UtmInfo


T = TypeVar("T", bound="UserInfo")


@_attrs_define
class UserInfo:
    """
    Attributes:
        uuid (str | Unset):
        name (str | Unset):
        email (str | Unset):
        token (str | Unset):
        default_account_id (str | Unset):
        intent (str | Unset):
        accounts (list[GatewayAccountRequest] | Unset):
        admin (bool | Unset):
        two_factor_authentication_enabled (bool | Unset):
        email_verified (bool | Unset):
        locked (bool | Unset):
        disabled (bool | Unset):
        signup_action (str | Unset):
        edition (str | Unset):
        billing_frequency (str | Unset):
        utm_info (UtmInfo | Unset):
        externally_managed (bool | Unset):
        given_name (str | Unset):
        family_name (str | Unset):
        external_id (str | Unset):
        created_at (int | Unset):
        last_updated_at (int | Unset):
        user_preferences (UserInfoUserPreferences | Unset):
        is_enriched_info_collected (bool | Unset):
        last_login (int | Unset):
    """

    uuid: str | Unset = UNSET
    name: str | Unset = UNSET
    email: str | Unset = UNSET
    token: str | Unset = UNSET
    default_account_id: str | Unset = UNSET
    intent: str | Unset = UNSET
    accounts: list[GatewayAccountRequest] | Unset = UNSET
    admin: bool | Unset = UNSET
    two_factor_authentication_enabled: bool | Unset = UNSET
    email_verified: bool | Unset = UNSET
    locked: bool | Unset = UNSET
    disabled: bool | Unset = UNSET
    signup_action: str | Unset = UNSET
    edition: str | Unset = UNSET
    billing_frequency: str | Unset = UNSET
    utm_info: UtmInfo | Unset = UNSET
    externally_managed: bool | Unset = UNSET
    given_name: str | Unset = UNSET
    family_name: str | Unset = UNSET
    external_id: str | Unset = UNSET
    created_at: int | Unset = UNSET
    last_updated_at: int | Unset = UNSET
    user_preferences: UserInfoUserPreferences | Unset = UNSET
    is_enriched_info_collected: bool | Unset = UNSET
    last_login: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        name = self.name

        email = self.email

        token = self.token

        default_account_id = self.default_account_id

        intent = self.intent

        accounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = []
            for accounts_item_data in self.accounts:
                accounts_item = accounts_item_data.to_dict()
                accounts.append(accounts_item)

        admin = self.admin

        two_factor_authentication_enabled = self.two_factor_authentication_enabled

        email_verified = self.email_verified

        locked = self.locked

        disabled = self.disabled

        signup_action = self.signup_action

        edition = self.edition

        billing_frequency = self.billing_frequency

        utm_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.utm_info, Unset):
            utm_info = self.utm_info.to_dict()

        externally_managed = self.externally_managed

        given_name = self.given_name

        family_name = self.family_name

        external_id = self.external_id

        created_at = self.created_at

        last_updated_at = self.last_updated_at

        user_preferences: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_preferences, Unset):
            user_preferences = self.user_preferences.to_dict()

        is_enriched_info_collected = self.is_enriched_info_collected

        last_login = self.last_login

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if token is not UNSET:
            field_dict["token"] = token
        if default_account_id is not UNSET:
            field_dict["defaultAccountId"] = default_account_id
        if intent is not UNSET:
            field_dict["intent"] = intent
        if accounts is not UNSET:
            field_dict["accounts"] = accounts
        if admin is not UNSET:
            field_dict["admin"] = admin
        if two_factor_authentication_enabled is not UNSET:
            field_dict["twoFactorAuthenticationEnabled"] = two_factor_authentication_enabled
        if email_verified is not UNSET:
            field_dict["emailVerified"] = email_verified
        if locked is not UNSET:
            field_dict["locked"] = locked
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if signup_action is not UNSET:
            field_dict["signupAction"] = signup_action
        if edition is not UNSET:
            field_dict["edition"] = edition
        if billing_frequency is not UNSET:
            field_dict["billingFrequency"] = billing_frequency
        if utm_info is not UNSET:
            field_dict["utmInfo"] = utm_info
        if externally_managed is not UNSET:
            field_dict["externallyManaged"] = externally_managed
        if given_name is not UNSET:
            field_dict["givenName"] = given_name
        if family_name is not UNSET:
            field_dict["familyName"] = family_name
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if last_updated_at is not UNSET:
            field_dict["lastUpdatedAt"] = last_updated_at
        if user_preferences is not UNSET:
            field_dict["userPreferences"] = user_preferences
        if is_enriched_info_collected is not UNSET:
            field_dict["isEnrichedInfoCollected"] = is_enriched_info_collected
        if last_login is not UNSET:
            field_dict["lastLogin"] = last_login

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gateway_account_request import GatewayAccountRequest
        from ..models.user_info_user_preferences import UserInfoUserPreferences
        from ..models.utm_info import UtmInfo

        d = dict(src_dict)
        uuid = d.pop("uuid", UNSET)

        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        token = d.pop("token", UNSET)

        default_account_id = d.pop("defaultAccountId", UNSET)

        intent = d.pop("intent", UNSET)

        _accounts = d.pop("accounts", UNSET)
        accounts: list[GatewayAccountRequest] | Unset = UNSET
        if _accounts is not UNSET:
            accounts = []
            for accounts_item_data in _accounts:
                accounts_item = GatewayAccountRequest.from_dict(accounts_item_data)

                accounts.append(accounts_item)

        admin = d.pop("admin", UNSET)

        two_factor_authentication_enabled = d.pop("twoFactorAuthenticationEnabled", UNSET)

        email_verified = d.pop("emailVerified", UNSET)

        locked = d.pop("locked", UNSET)

        disabled = d.pop("disabled", UNSET)

        signup_action = d.pop("signupAction", UNSET)

        edition = d.pop("edition", UNSET)

        billing_frequency = d.pop("billingFrequency", UNSET)

        _utm_info = d.pop("utmInfo", UNSET)
        utm_info: UtmInfo | Unset
        if isinstance(_utm_info, Unset):
            utm_info = UNSET
        else:
            utm_info = UtmInfo.from_dict(_utm_info)

        externally_managed = d.pop("externallyManaged", UNSET)

        given_name = d.pop("givenName", UNSET)

        family_name = d.pop("familyName", UNSET)

        external_id = d.pop("externalId", UNSET)

        created_at = d.pop("createdAt", UNSET)

        last_updated_at = d.pop("lastUpdatedAt", UNSET)

        _user_preferences = d.pop("userPreferences", UNSET)
        user_preferences: UserInfoUserPreferences | Unset
        if isinstance(_user_preferences, Unset):
            user_preferences = UNSET
        else:
            user_preferences = UserInfoUserPreferences.from_dict(_user_preferences)

        is_enriched_info_collected = d.pop("isEnrichedInfoCollected", UNSET)

        last_login = d.pop("lastLogin", UNSET)

        user_info = cls(
            uuid=uuid,
            name=name,
            email=email,
            token=token,
            default_account_id=default_account_id,
            intent=intent,
            accounts=accounts,
            admin=admin,
            two_factor_authentication_enabled=two_factor_authentication_enabled,
            email_verified=email_verified,
            locked=locked,
            disabled=disabled,
            signup_action=signup_action,
            edition=edition,
            billing_frequency=billing_frequency,
            utm_info=utm_info,
            externally_managed=externally_managed,
            given_name=given_name,
            family_name=family_name,
            external_id=external_id,
            created_at=created_at,
            last_updated_at=last_updated_at,
            user_preferences=user_preferences,
            is_enriched_info_collected=is_enriched_info_collected,
            last_login=last_login,
        )

        user_info.additional_properties = d
        return user_info

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
