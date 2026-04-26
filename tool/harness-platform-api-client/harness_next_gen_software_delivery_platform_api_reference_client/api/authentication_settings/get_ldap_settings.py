from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.rest_response_ldap_settings import RestResponseLDAPSettings
from ...types import UNSET, Response


def _get_kwargs(
    *,
    account_identifier: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/authentication-settings/ldap/settings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | RestResponseLDAPSettings:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = RestResponseLDAPSettings.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | RestResponseLDAPSettings]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
) -> Response[Error | Failure | RestResponseLDAPSettings]:
    """Return configured Ldap settings for the account

     Returns configured Ldap settings and its details for the account.

    Args:
        account_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | RestResponseLDAPSettings]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
) -> Error | Failure | RestResponseLDAPSettings | None:
    """Return configured Ldap settings for the account

     Returns configured Ldap settings and its details for the account.

    Args:
        account_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | RestResponseLDAPSettings
    """

    return sync_detailed(
        client=client,
        account_identifier=account_identifier,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
) -> Response[Error | Failure | RestResponseLDAPSettings]:
    """Return configured Ldap settings for the account

     Returns configured Ldap settings and its details for the account.

    Args:
        account_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | RestResponseLDAPSettings]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
) -> Error | Failure | RestResponseLDAPSettings | None:
    """Return configured Ldap settings for the account

     Returns configured Ldap settings and its details for the account.

    Args:
        account_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | RestResponseLDAPSettings
    """

    return (
        await asyncio_detailed(
            client=client,
            account_identifier=account_identifier,
        )
    ).parsed
