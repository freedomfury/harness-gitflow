from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_authentication_mechanism import (
    AccountAuthenticationMechanism,
    check_account_authentication_mechanism,
)
from ..models.account_default_experience import AccountDefaultExperience, check_account_default_experience
from ..models.account_edition import AccountEdition, check_account_edition
from ..models.account_pricing_type import AccountPricingType, check_account_pricing_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_account_config import ServiceAccountConfig


T = TypeVar("T", bound="Account")


@_attrs_define
class Account:
    """Account details defined in Harness.

    Attributes:
        identifier (str | Unset): Account Identifier.
        name (str | Unset): Name of the Account.
        company_name (str | Unset): Name of the Company.
        account_type (str | Unset): Type of the Account
        account_status (str | Unset): Status of the Account
        cluster (str | Unset): Name of the cluster associated with this Account.
        default_experience (AccountDefaultExperience | Unset): Default experience of the Account.
        authentication_mechanism (AccountAuthenticationMechanism | Unset): Authentication mechanism associated with the
            account.
        service_account_config (ServiceAccountConfig | Unset): Service Account configuration associated with this
            Account.
        created_at (int | Unset): Account creation time in epoch
        expiry_time (int | Unset): Account's license expiry time in epoch
        ring_name (str | Unset): Specifies delegate ring version for account
        subdomain_url (str | Unset): Specifies subdomain url for account
        session_timeout_in_minutes (int | Unset): SessionTimeout in minutes
        public_access_enabled (bool | Unset): Specifies if Account has public access enabled.
        absolute_session_timeout_in_minutes (int | Unset): Absolute SessionTimeout in minutes
        pricing_type (AccountPricingType | Unset): Specifies the pricing type of account
        edition (AccountEdition | Unset): Specified the edition of account in flex pricing model
        contract_start_date (int | Unset): Contract Start Date in epoch
        contract_end_date (int | Unset): Contract End Date in epoch
        product_led (bool | Unset):
        two_factor_admin_enforced (bool | Unset):
        oauth_enabled (bool | Unset):
        next_gen_enabled (bool | Unset):
        cross_generation_access_enabled (bool | Unset):
        canny_username_abbreviation_enabled (bool | Unset):
        harness_support_access_allowed (bool | Unset):
    """

    identifier: str | Unset = UNSET
    name: str | Unset = UNSET
    company_name: str | Unset = UNSET
    account_type: str | Unset = UNSET
    account_status: str | Unset = UNSET
    cluster: str | Unset = UNSET
    default_experience: AccountDefaultExperience | Unset = UNSET
    authentication_mechanism: AccountAuthenticationMechanism | Unset = UNSET
    service_account_config: ServiceAccountConfig | Unset = UNSET
    created_at: int | Unset = UNSET
    expiry_time: int | Unset = UNSET
    ring_name: str | Unset = UNSET
    subdomain_url: str | Unset = UNSET
    session_timeout_in_minutes: int | Unset = UNSET
    public_access_enabled: bool | Unset = UNSET
    absolute_session_timeout_in_minutes: int | Unset = UNSET
    pricing_type: AccountPricingType | Unset = UNSET
    edition: AccountEdition | Unset = UNSET
    contract_start_date: int | Unset = UNSET
    contract_end_date: int | Unset = UNSET
    product_led: bool | Unset = UNSET
    two_factor_admin_enforced: bool | Unset = UNSET
    oauth_enabled: bool | Unset = UNSET
    next_gen_enabled: bool | Unset = UNSET
    cross_generation_access_enabled: bool | Unset = UNSET
    canny_username_abbreviation_enabled: bool | Unset = UNSET
    harness_support_access_allowed: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        name = self.name

        company_name = self.company_name

        account_type = self.account_type

        account_status = self.account_status

        cluster = self.cluster

        default_experience: str | Unset = UNSET
        if not isinstance(self.default_experience, Unset):
            default_experience = self.default_experience

        authentication_mechanism: str | Unset = UNSET
        if not isinstance(self.authentication_mechanism, Unset):
            authentication_mechanism = self.authentication_mechanism

        service_account_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.service_account_config, Unset):
            service_account_config = self.service_account_config.to_dict()

        created_at = self.created_at

        expiry_time = self.expiry_time

        ring_name = self.ring_name

        subdomain_url = self.subdomain_url

        session_timeout_in_minutes = self.session_timeout_in_minutes

        public_access_enabled = self.public_access_enabled

        absolute_session_timeout_in_minutes = self.absolute_session_timeout_in_minutes

        pricing_type: str | Unset = UNSET
        if not isinstance(self.pricing_type, Unset):
            pricing_type = self.pricing_type

        edition: str | Unset = UNSET
        if not isinstance(self.edition, Unset):
            edition = self.edition

        contract_start_date = self.contract_start_date

        contract_end_date = self.contract_end_date

        product_led = self.product_led

        two_factor_admin_enforced = self.two_factor_admin_enforced

        oauth_enabled = self.oauth_enabled

        next_gen_enabled = self.next_gen_enabled

        cross_generation_access_enabled = self.cross_generation_access_enabled

        canny_username_abbreviation_enabled = self.canny_username_abbreviation_enabled

        harness_support_access_allowed = self.harness_support_access_allowed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if name is not UNSET:
            field_dict["name"] = name
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if account_status is not UNSET:
            field_dict["accountStatus"] = account_status
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if default_experience is not UNSET:
            field_dict["defaultExperience"] = default_experience
        if authentication_mechanism is not UNSET:
            field_dict["authenticationMechanism"] = authentication_mechanism
        if service_account_config is not UNSET:
            field_dict["serviceAccountConfig"] = service_account_config
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if expiry_time is not UNSET:
            field_dict["expiryTime"] = expiry_time
        if ring_name is not UNSET:
            field_dict["ringName"] = ring_name
        if subdomain_url is not UNSET:
            field_dict["subdomainURL"] = subdomain_url
        if session_timeout_in_minutes is not UNSET:
            field_dict["sessionTimeoutInMinutes"] = session_timeout_in_minutes
        if public_access_enabled is not UNSET:
            field_dict["publicAccessEnabled"] = public_access_enabled
        if absolute_session_timeout_in_minutes is not UNSET:
            field_dict["absoluteSessionTimeoutInMinutes"] = absolute_session_timeout_in_minutes
        if pricing_type is not UNSET:
            field_dict["pricingType"] = pricing_type
        if edition is not UNSET:
            field_dict["edition"] = edition
        if contract_start_date is not UNSET:
            field_dict["contractStartDate"] = contract_start_date
        if contract_end_date is not UNSET:
            field_dict["contractEndDate"] = contract_end_date
        if product_led is not UNSET:
            field_dict["productLed"] = product_led
        if two_factor_admin_enforced is not UNSET:
            field_dict["twoFactorAdminEnforced"] = two_factor_admin_enforced
        if oauth_enabled is not UNSET:
            field_dict["oauthEnabled"] = oauth_enabled
        if next_gen_enabled is not UNSET:
            field_dict["nextGenEnabled"] = next_gen_enabled
        if cross_generation_access_enabled is not UNSET:
            field_dict["crossGenerationAccessEnabled"] = cross_generation_access_enabled
        if canny_username_abbreviation_enabled is not UNSET:
            field_dict["cannyUsernameAbbreviationEnabled"] = canny_username_abbreviation_enabled
        if harness_support_access_allowed is not UNSET:
            field_dict["harnessSupportAccessAllowed"] = harness_support_access_allowed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_account_config import ServiceAccountConfig

        d = dict(src_dict)
        identifier = d.pop("identifier", UNSET)

        name = d.pop("name", UNSET)

        company_name = d.pop("companyName", UNSET)

        account_type = d.pop("accountType", UNSET)

        account_status = d.pop("accountStatus", UNSET)

        cluster = d.pop("cluster", UNSET)

        _default_experience = d.pop("defaultExperience", UNSET)
        default_experience: AccountDefaultExperience | Unset
        if isinstance(_default_experience, Unset):
            default_experience = UNSET
        else:
            default_experience = check_account_default_experience(_default_experience)

        _authentication_mechanism = d.pop("authenticationMechanism", UNSET)
        authentication_mechanism: AccountAuthenticationMechanism | Unset
        if isinstance(_authentication_mechanism, Unset):
            authentication_mechanism = UNSET
        else:
            authentication_mechanism = check_account_authentication_mechanism(_authentication_mechanism)

        _service_account_config = d.pop("serviceAccountConfig", UNSET)
        service_account_config: ServiceAccountConfig | Unset
        if isinstance(_service_account_config, Unset):
            service_account_config = UNSET
        else:
            service_account_config = ServiceAccountConfig.from_dict(_service_account_config)

        created_at = d.pop("createdAt", UNSET)

        expiry_time = d.pop("expiryTime", UNSET)

        ring_name = d.pop("ringName", UNSET)

        subdomain_url = d.pop("subdomainURL", UNSET)

        session_timeout_in_minutes = d.pop("sessionTimeoutInMinutes", UNSET)

        public_access_enabled = d.pop("publicAccessEnabled", UNSET)

        absolute_session_timeout_in_minutes = d.pop("absoluteSessionTimeoutInMinutes", UNSET)

        _pricing_type = d.pop("pricingType", UNSET)
        pricing_type: AccountPricingType | Unset
        if isinstance(_pricing_type, Unset):
            pricing_type = UNSET
        else:
            pricing_type = check_account_pricing_type(_pricing_type)

        _edition = d.pop("edition", UNSET)
        edition: AccountEdition | Unset
        if isinstance(_edition, Unset):
            edition = UNSET
        else:
            edition = check_account_edition(_edition)

        contract_start_date = d.pop("contractStartDate", UNSET)

        contract_end_date = d.pop("contractEndDate", UNSET)

        product_led = d.pop("productLed", UNSET)

        two_factor_admin_enforced = d.pop("twoFactorAdminEnforced", UNSET)

        oauth_enabled = d.pop("oauthEnabled", UNSET)

        next_gen_enabled = d.pop("nextGenEnabled", UNSET)

        cross_generation_access_enabled = d.pop("crossGenerationAccessEnabled", UNSET)

        canny_username_abbreviation_enabled = d.pop("cannyUsernameAbbreviationEnabled", UNSET)

        harness_support_access_allowed = d.pop("harnessSupportAccessAllowed", UNSET)

        account = cls(
            identifier=identifier,
            name=name,
            company_name=company_name,
            account_type=account_type,
            account_status=account_status,
            cluster=cluster,
            default_experience=default_experience,
            authentication_mechanism=authentication_mechanism,
            service_account_config=service_account_config,
            created_at=created_at,
            expiry_time=expiry_time,
            ring_name=ring_name,
            subdomain_url=subdomain_url,
            session_timeout_in_minutes=session_timeout_in_minutes,
            public_access_enabled=public_access_enabled,
            absolute_session_timeout_in_minutes=absolute_session_timeout_in_minutes,
            pricing_type=pricing_type,
            edition=edition,
            contract_start_date=contract_start_date,
            contract_end_date=contract_end_date,
            product_led=product_led,
            two_factor_admin_enforced=two_factor_admin_enforced,
            oauth_enabled=oauth_enabled,
            next_gen_enabled=next_gen_enabled,
            cross_generation_access_enabled=cross_generation_access_enabled,
            canny_username_abbreviation_enabled=canny_username_abbreviation_enabled,
            harness_support_access_allowed=harness_support_access_allowed,
        )

        account.additional_properties = d
        return account

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
