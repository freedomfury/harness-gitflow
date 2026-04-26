from typing import Literal, cast

ServiceUsageDTOCdLicenseType = Literal[
    "CUSTOM", "DEVELOPER_360", "LEGACY_USER", "NAMED_USER", "SERVICE_INSTANCES", "SERVICES"
]

SERVICE_USAGE_DTO_CD_LICENSE_TYPE_VALUES: set[ServiceUsageDTOCdLicenseType] = {
    "CUSTOM",
    "DEVELOPER_360",
    "LEGACY_USER",
    "NAMED_USER",
    "SERVICE_INSTANCES",
    "SERVICES",
}


def check_service_usage_dto_cd_license_type(value: str) -> ServiceUsageDTOCdLicenseType:
    if value in SERVICE_USAGE_DTO_CD_LICENSE_TYPE_VALUES:
        return cast(ServiceUsageDTOCdLicenseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SERVICE_USAGE_DTO_CD_LICENSE_TYPE_VALUES!r}")
