from typing import Literal, cast

DownloadCDUsageCSVReportUsageType = Literal["Gitops", "PipelineExecution", "ServiceDeployment"]

DOWNLOAD_CD_USAGE_CSV_REPORT_USAGE_TYPE_VALUES: set[DownloadCDUsageCSVReportUsageType] = {
    "Gitops",
    "PipelineExecution",
    "ServiceDeployment",
}


def check_download_cd_usage_csv_report_usage_type(value: str) -> DownloadCDUsageCSVReportUsageType:
    if value in DOWNLOAD_CD_USAGE_CSV_REPORT_USAGE_TYPE_VALUES:
        return cast(DownloadCDUsageCSVReportUsageType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOWNLOAD_CD_USAGE_CSV_REPORT_USAGE_TYPE_VALUES!r}")
