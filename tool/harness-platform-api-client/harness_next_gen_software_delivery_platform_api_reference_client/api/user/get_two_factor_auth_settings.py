from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.get_two_factor_auth_settings_auth_mechanism import (
    GetTwoFactorAuthSettingsAuthMechanism,
)
from ...models.response_dto_two_factor_auth_settings_info import ResponseDTOTwoFactorAuthSettingsInfo
from ...types import UNSET, Response


def _get_kwargs(
    auth_mechanism: GetTwoFactorAuthSettingsAuthMechanism,
    *,
    account_identifier: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/user/two-factor-auth/{auth_mechanism}".format(
            auth_mechanism=quote(str(auth_mechanism), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOTwoFactorAuthSettingsInfo:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOTwoFactorAuthSettingsInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOTwoFactorAuthSettingsInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    auth_mechanism: GetTwoFactorAuthSettingsAuthMechanism,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
) -> Response[Error | Failure | ResponseDTOTwoFactorAuthSettingsInfo]:
    """Gets Two Factor Auth Settings

     Gets two factor authentication settings information of the current logged in user

    Args:
        auth_mechanism (GetTwoFactorAuthSettingsAuthMechanism):
        account_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOTwoFactorAuthSettingsInfo]
    """

    kwargs = _get_kwargs(
        auth_mechanism=auth_mechanism,
        account_identifier=account_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    auth_mechanism: GetTwoFactorAuthSettingsAuthMechanism,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
) -> Error | Failure | ResponseDTOTwoFactorAuthSettingsInfo | None:
    """Gets Two Factor Auth Settings

     Gets two factor authentication settings information of the current logged in user

    Args:
        auth_mechanism (GetTwoFactorAuthSettingsAuthMechanism):
        account_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOTwoFactorAuthSettingsInfo
    """

    return sync_detailed(
        auth_mechanism=auth_mechanism,
        client=client,
        account_identifier=account_identifier,
    ).parsed


async def asyncio_detailed(
    auth_mechanism: GetTwoFactorAuthSettingsAuthMechanism,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
) -> Response[Error | Failure | ResponseDTOTwoFactorAuthSettingsInfo]:
    """Gets Two Factor Auth Settings

     Gets two factor authentication settings information of the current logged in user

    Args:
        auth_mechanism (GetTwoFactorAuthSettingsAuthMechanism):
        account_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOTwoFactorAuthSettingsInfo]
    """

    kwargs = _get_kwargs(
        auth_mechanism=auth_mechanism,
        account_identifier=account_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    auth_mechanism: GetTwoFactorAuthSettingsAuthMechanism,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
) -> Error | Failure | ResponseDTOTwoFactorAuthSettingsInfo | None:
    """Gets Two Factor Auth Settings

     Gets two factor authentication settings information of the current logged in user

    Args:
        auth_mechanism (GetTwoFactorAuthSettingsAuthMechanism):
        account_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOTwoFactorAuthSettingsInfo
    """

    return (
        await asyncio_detailed(
            auth_mechanism=auth_mechanism,
            client=client,
            account_identifier=account_identifier,
        )
    ).parsed
