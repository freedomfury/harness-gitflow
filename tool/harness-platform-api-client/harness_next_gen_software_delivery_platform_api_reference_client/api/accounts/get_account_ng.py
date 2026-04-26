from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_account import ResponseDTOAccount
from ...types import Response


def _get_kwargs(
    account_identifier: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounts/{account_identifier}".format(
            account_identifier=quote(str(account_identifier), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOAccount:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOAccount.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOAccount]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_identifier: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | Failure | ResponseDTOAccount]:
    """Gets an account

    Args:
        account_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOAccount]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_identifier: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | Failure | ResponseDTOAccount | None:
    """Gets an account

    Args:
        account_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOAccount
    """

    return sync_detailed(
        account_identifier=account_identifier,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_identifier: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | Failure | ResponseDTOAccount]:
    """Gets an account

    Args:
        account_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOAccount]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_identifier: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | Failure | ResponseDTOAccount | None:
    """Gets an account

    Args:
        account_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOAccount
    """

    return (
        await asyncio_detailed(
            account_identifier=account_identifier,
            client=client,
        )
    ).parsed
