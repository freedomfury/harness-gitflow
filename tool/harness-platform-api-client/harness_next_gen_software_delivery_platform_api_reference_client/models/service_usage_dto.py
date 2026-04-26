from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_usage_dto_cd_license_type import (
    ServiceUsageDTOCdLicenseType,
    check_service_usage_dto_cd_license_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usage_data_dto import UsageDataDTO


T = TypeVar("T", bound="ServiceUsageDTO")


@_attrs_define
class ServiceUsageDTO:
    """
    Attributes:
        account_identifier (str | Unset):
        module (str | Unset):
        timestamp (int | Unset):
        active_services (UsageDataDTO | Unset):
        active_service_instances (UsageDataDTO | Unset):
        cd_license_type (ServiceUsageDTOCdLicenseType | Unset):
        service_licenses (UsageDataDTO | Unset):
    """

    account_identifier: str | Unset = UNSET
    module: str | Unset = UNSET
    timestamp: int | Unset = UNSET
    active_services: UsageDataDTO | Unset = UNSET
    active_service_instances: UsageDataDTO | Unset = UNSET
    cd_license_type: ServiceUsageDTOCdLicenseType | Unset = UNSET
    service_licenses: UsageDataDTO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_identifier = self.account_identifier

        module = self.module

        timestamp = self.timestamp

        active_services: dict[str, Any] | Unset = UNSET
        if not isinstance(self.active_services, Unset):
            active_services = self.active_services.to_dict()

        active_service_instances: dict[str, Any] | Unset = UNSET
        if not isinstance(self.active_service_instances, Unset):
            active_service_instances = self.active_service_instances.to_dict()

        cd_license_type: str | Unset = UNSET
        if not isinstance(self.cd_license_type, Unset):
            cd_license_type = self.cd_license_type

        service_licenses: dict[str, Any] | Unset = UNSET
        if not isinstance(self.service_licenses, Unset):
            service_licenses = self.service_licenses.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_identifier is not UNSET:
            field_dict["accountIdentifier"] = account_identifier
        if module is not UNSET:
            field_dict["module"] = module
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if active_services is not UNSET:
            field_dict["activeServices"] = active_services
        if active_service_instances is not UNSET:
            field_dict["activeServiceInstances"] = active_service_instances
        if cd_license_type is not UNSET:
            field_dict["cdLicenseType"] = cd_license_type
        if service_licenses is not UNSET:
            field_dict["serviceLicenses"] = service_licenses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usage_data_dto import UsageDataDTO

        d = dict(src_dict)
        account_identifier = d.pop("accountIdentifier", UNSET)

        module = d.pop("module", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        _active_services = d.pop("activeServices", UNSET)
        active_services: UsageDataDTO | Unset
        if isinstance(_active_services, Unset):
            active_services = UNSET
        else:
            active_services = UsageDataDTO.from_dict(_active_services)

        _active_service_instances = d.pop("activeServiceInstances", UNSET)
        active_service_instances: UsageDataDTO | Unset
        if isinstance(_active_service_instances, Unset):
            active_service_instances = UNSET
        else:
            active_service_instances = UsageDataDTO.from_dict(_active_service_instances)

        _cd_license_type = d.pop("cdLicenseType", UNSET)
        cd_license_type: ServiceUsageDTOCdLicenseType | Unset
        if isinstance(_cd_license_type, Unset):
            cd_license_type = UNSET
        else:
            cd_license_type = check_service_usage_dto_cd_license_type(_cd_license_type)

        _service_licenses = d.pop("serviceLicenses", UNSET)
        service_licenses: UsageDataDTO | Unset
        if isinstance(_service_licenses, Unset):
            service_licenses = UNSET
        else:
            service_licenses = UsageDataDTO.from_dict(_service_licenses)

        service_usage_dto = cls(
            account_identifier=account_identifier,
            module=module,
            timestamp=timestamp,
            active_services=active_services,
            active_service_instances=active_service_instances,
            cd_license_type=cd_license_type,
            service_licenses=service_licenses,
        )

        service_usage_dto.additional_properties = d
        return service_usage_dto

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
