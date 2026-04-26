from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.download_cd_usage_csv_report_usage_type import (
    DownloadCDUsageCSVReportUsageType,
)
from ...models.error import Error
from ...models.failure import Failure
from ...types import UNSET, Response, Unset


def _get_kwargs(
    usage_type: DownloadCDUsageCSVReportUsageType,
    *,
    account_identifier: str | Unset = UNSET,
    timestamp: int | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["timestamp"] = timestamp

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/license-usage-cd/v2/{usage_type}/csv/download".format(
            usage_type=quote(str(usage_type), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | Failure:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = cast(Any, None)
    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Error | Failure]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    usage_type: DownloadCDUsageCSVReportUsageType,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str | Unset = UNSET,
    timestamp: int | Unset = 0,
) -> Response[Any | Error | Failure]:
    """Download CD Usage CSV report

    Args:
        usage_type (DownloadCDUsageCSVReportUsageType):
        account_identifier (str | Unset):
        timestamp (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | Failure]
    """

    kwargs = _get_kwargs(
        usage_type=usage_type,
        account_identifier=account_identifier,
        timestamp=timestamp,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    usage_type: DownloadCDUsageCSVReportUsageType,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str | Unset = UNSET,
    timestamp: int | Unset = 0,
) -> Any | Error | Failure | None:
    """Download CD Usage CSV report

    Args:
        usage_type (DownloadCDUsageCSVReportUsageType):
        account_identifier (str | Unset):
        timestamp (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | Failure
    """

    return sync_detailed(
        usage_type=usage_type,
        client=client,
        account_identifier=account_identifier,
        timestamp=timestamp,
    ).parsed


async def asyncio_detailed(
    usage_type: DownloadCDUsageCSVReportUsageType,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str | Unset = UNSET,
    timestamp: int | Unset = 0,
) -> Response[Any | Error | Failure]:
    """Download CD Usage CSV report

    Args:
        usage_type (DownloadCDUsageCSVReportUsageType):
        account_identifier (str | Unset):
        timestamp (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | Failure]
    """

    kwargs = _get_kwargs(
        usage_type=usage_type,
        account_identifier=account_identifier,
        timestamp=timestamp,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    usage_type: DownloadCDUsageCSVReportUsageType,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str | Unset = UNSET,
    timestamp: int | Unset = 0,
) -> Any | Error | Failure | None:
    """Download CD Usage CSV report

    Args:
        usage_type (DownloadCDUsageCSVReportUsageType):
        account_identifier (str | Unset):
        timestamp (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | Failure
    """

    return (
        await asyncio_detailed(
            usage_type=usage_type,
            client=client,
            account_identifier=account_identifier,
            timestamp=timestamp,
        )
    ).parsed
