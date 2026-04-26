from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...types import UNSET, Response, Unset


def _get_kwargs(
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
        "url": "/usage/cd/active-services/csv/download",
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
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str | Unset = UNSET,
    timestamp: int | Unset = 0,
) -> Response[Any | Error | Failure]:
    """Download CSV Active Services report

    Args:
        account_identifier (str | Unset):
        timestamp (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | Failure]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        timestamp=timestamp,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str | Unset = UNSET,
    timestamp: int | Unset = 0,
) -> Any | Error | Failure | None:
    """Download CSV Active Services report

    Args:
        account_identifier (str | Unset):
        timestamp (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | Failure
    """

    return sync_detailed(
        client=client,
        account_identifier=account_identifier,
        timestamp=timestamp,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str | Unset = UNSET,
    timestamp: int | Unset = 0,
) -> Response[Any | Error | Failure]:
    """Download CSV Active Services report

    Args:
        account_identifier (str | Unset):
        timestamp (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | Failure]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        timestamp=timestamp,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str | Unset = UNSET,
    timestamp: int | Unset = 0,
) -> Any | Error | Failure | None:
    """Download CSV Active Services report

    Args:
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
            client=client,
            account_identifier=account_identifier,
            timestamp=timestamp,
        )
    ).parsed
