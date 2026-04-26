from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.rest_response_sso_config import RestResponseSSOConfig
from ...types import UNSET, Response


def _get_kwargs(
    saml_sso_id: str,
    *,
    account_identifier: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/authentication-settings/saml-metadata/{saml_sso_id}/delete".format(
            saml_sso_id=quote(str(saml_sso_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | RestResponseSSOConfig:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = RestResponseSSOConfig.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | RestResponseSSOConfig]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    saml_sso_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
) -> Response[Error | Failure | RestResponseSSOConfig]:
    """Delete SAML meta data for given SAML sso id

     Deletes SAML metadata for the given Account and SAML sso id

    Args:
        saml_sso_id (str):
        account_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | RestResponseSSOConfig]
    """

    kwargs = _get_kwargs(
        saml_sso_id=saml_sso_id,
        account_identifier=account_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    saml_sso_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
) -> Error | Failure | RestResponseSSOConfig | None:
    """Delete SAML meta data for given SAML sso id

     Deletes SAML metadata for the given Account and SAML sso id

    Args:
        saml_sso_id (str):
        account_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | RestResponseSSOConfig
    """

    return sync_detailed(
        saml_sso_id=saml_sso_id,
        client=client,
        account_identifier=account_identifier,
    ).parsed


async def asyncio_detailed(
    saml_sso_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
) -> Response[Error | Failure | RestResponseSSOConfig]:
    """Delete SAML meta data for given SAML sso id

     Deletes SAML metadata for the given Account and SAML sso id

    Args:
        saml_sso_id (str):
        account_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | RestResponseSSOConfig]
    """

    kwargs = _get_kwargs(
        saml_sso_id=saml_sso_id,
        account_identifier=account_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    saml_sso_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
) -> Error | Failure | RestResponseSSOConfig | None:
    """Delete SAML meta data for given SAML sso id

     Deletes SAML metadata for the given Account and SAML sso id

    Args:
        saml_sso_id (str):
        account_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | RestResponseSSOConfig
    """

    return (
        await asyncio_detailed(
            saml_sso_id=saml_sso_id,
            client=client,
            account_identifier=account_identifier,
        )
    ).parsed
