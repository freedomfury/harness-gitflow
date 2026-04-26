from typing import Literal, cast

ServiceInstanceUsageDTOCdLicenseType = Literal[
    "CUSTOM", "DEVELOPER_360", "LEGACY_USER", "NAMED_USER", "SERVICE_INSTANCES", "SERVICES"
]

SERVICE_INSTANCE_USAGE_DTO_CD_LICENSE_TYPE_VALUES: set[ServiceInstanceUsageDTOCdLicenseType] = {
    "CUSTOM",
    "DEVELOPER_360",
    "LEGACY_USER",
    "NAMED_USER",
    "SERVICE_INSTANCES",
    "SERVICES",
}


def check_service_instance_usage_dto_cd_license_type(value: str) -> ServiceInstanceUsageDTOCdLicenseType:
    if value in SERVICE_INSTANCE_USAGE_DTO_CD_LICENSE_TYPE_VALUES:
        return cast(ServiceInstanceUsageDTOCdLicenseType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SERVICE_INSTANCE_USAGE_DTO_CD_LICENSE_TYPE_VALUES!r}"
    )
