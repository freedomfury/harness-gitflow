from typing import Literal, cast

DelegateDownloadRequestSize = Literal["CCM_SMALL", "LAPTOP", "LARGE", "MEDIUM", "SMALL"]

DELEGATE_DOWNLOAD_REQUEST_SIZE_VALUES: set[DelegateDownloadRequestSize] = {
    "CCM_SMALL",
    "LAPTOP",
    "LARGE",
    "MEDIUM",
    "SMALL",
}


def check_delegate_download_request_size(value: str) -> DelegateDownloadRequestSize:
    if value in DELEGATE_DOWNLOAD_REQUEST_SIZE_VALUES:
        return cast(DelegateDownloadRequestSize, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DELEGATE_DOWNLOAD_REQUEST_SIZE_VALUES!r}")
