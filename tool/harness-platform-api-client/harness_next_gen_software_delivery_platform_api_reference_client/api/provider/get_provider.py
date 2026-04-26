from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_get_provider_response import ResponseDTOGetProviderResponse
from ...types import UNSET, Response


def _get_kwargs(
    provider_identifier: str,
    *,
    account_identifier: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/provider/{provider_identifier}".format(
            provider_identifier=quote(str(provider_identifier), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOGetProviderResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOGetProviderResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOGetProviderResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    provider_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
) -> Response[Error | Failure | ResponseDTOGetProviderResponse]:
    """Gets a Provider by identifier

    Args:
        provider_identifier (str):
        account_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOGetProviderResponse]
    """

    kwargs = _get_kwargs(
        provider_identifier=provider_identifier,
        account_identifier=account_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    provider_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
) -> Error | Failure | ResponseDTOGetProviderResponse | None:
    """Gets a Provider by identifier

    Args:
        provider_identifier (str):
        account_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOGetProviderResponse
    """

    return sync_detailed(
        provider_identifier=provider_identifier,
        client=client,
        account_identifier=account_identifier,
    ).parsed


async def asyncio_detailed(
    provider_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
) -> Response[Error | Failure | ResponseDTOGetProviderResponse]:
    """Gets a Provider by identifier

    Args:
        provider_identifier (str):
        account_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOGetProviderResponse]
    """

    kwargs = _get_kwargs(
        provider_identifier=provider_identifier,
        account_identifier=account_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    provider_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
) -> Error | Failure | ResponseDTOGetProviderResponse | None:
    """Gets a Provider by identifier

    Args:
        provider_identifier (str):
        account_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOGetProviderResponse
    """

    return (
        await asyncio_detailed(
            provider_identifier=provider_identifier,
            client=client,
            account_identifier=account_identifier,
        )
    ).parsed
