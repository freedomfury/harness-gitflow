from typing import Literal, cast

GetProjectListWithMultiOrgFilterModuleType = Literal[
    "AARP",
    "AASP",
    "AAST",
    "AI_AGENT_MLOPS",
    "AI_TEST_AUTOMATION",
    "AISRE",
    "CD",
    "CE",
    "CET",
    "CF",
    "CHAOS",
    "CI",
    "CODE",
    "CORE",
    "CV",
    "DBOPS",
    "DevopsEssentials",
    "FME",
    "GOVERNANCE",
    "HAR",
    "IACM",
    "IDP",
    "PLATFORM",
    "PMS",
    "RMG",
    "SEI",
    "SRM",
    "SSCA",
    "STO",
    "TEMPLATESERVICE",
]

GET_PROJECT_LIST_WITH_MULTI_ORG_FILTER_MODULE_TYPE_VALUES: set[GetProjectListWithMultiOrgFilterModuleType] = {
    "AARP",
    "AASP",
    "AAST",
    "AI_AGENT_MLOPS",
    "AI_TEST_AUTOMATION",
    "AISRE",
    "CD",
    "CE",
    "CET",
    "CF",
    "CHAOS",
    "CI",
    "CODE",
    "CORE",
    "CV",
    "DBOPS",
    "DevopsEssentials",
    "FME",
    "GOVERNANCE",
    "HAR",
    "IACM",
    "IDP",
    "PLATFORM",
    "PMS",
    "RMG",
    "SEI",
    "SRM",
    "SSCA",
    "STO",
    "TEMPLATESERVICE",
}


def check_get_project_list_with_multi_org_filter_module_type(value: str) -> GetProjectListWithMultiOrgFilterModuleType:
    if value in GET_PROJECT_LIST_WITH_MULTI_ORG_FILTER_MODULE_TYPE_VALUES:
        return cast(GetProjectListWithMultiOrgFilterModuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_PROJECT_LIST_WITH_MULTI_ORG_FILTER_MODULE_TYPE_VALUES!r}"
    )
