from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.rest_response_sso_config import RestResponseSSOConfig
from ...models.upload_saml_meta_data_body import UploadSamlMetaDataBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UploadSamlMetaDataBody | Unset = UNSET,
    account_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountId"] = account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/authentication-settings/saml-metadata-upload",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
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
    *,
    client: AuthenticatedClient | Client,
    body: UploadSamlMetaDataBody | Unset = UNSET,
    account_id: str,
) -> Response[Error | Failure | RestResponseSSOConfig]:
    """Upload SAML metadata

     Updates the SAML metadata for the given Account ID.

    Args:
        account_id (str):
        body (UploadSamlMetaDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | RestResponseSSOConfig]
    """

    kwargs = _get_kwargs(
        body=body,
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: UploadSamlMetaDataBody | Unset = UNSET,
    account_id: str,
) -> Error | Failure | RestResponseSSOConfig | None:
    """Upload SAML metadata

     Updates the SAML metadata for the given Account ID.

    Args:
        account_id (str):
        body (UploadSamlMetaDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | RestResponseSSOConfig
    """

    return sync_detailed(
        client=client,
        body=body,
        account_id=account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadSamlMetaDataBody | Unset = UNSET,
    account_id: str,
) -> Response[Error | Failure | RestResponseSSOConfig]:
    """Upload SAML metadata

     Updates the SAML metadata for the given Account ID.

    Args:
        account_id (str):
        body (UploadSamlMetaDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | RestResponseSSOConfig]
    """

    kwargs = _get_kwargs(
        body=body,
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UploadSamlMetaDataBody | Unset = UNSET,
    account_id: str,
) -> Error | Failure | RestResponseSSOConfig | None:
    """Upload SAML metadata

     Updates the SAML metadata for the given Account ID.

    Args:
        account_id (str):
        body (UploadSamlMetaDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | RestResponseSSOConfig
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            account_id=account_id,
        )
    ).parsed
