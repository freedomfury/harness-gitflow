from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.gcp_oidc_access_token_request import GcpOidcAccessTokenRequest
from ...models.response_dto_gcp_oidc_service_account_access_token_response import (
    ResponseDTOGcpOidcServiceAccountAccessTokenResponse,
)
from ...types import Response


def _get_kwargs(
    *,
    body: GcpOidcAccessTokenRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/oidc/access-token/gcp/service-account-access",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOGcpOidcServiceAccountAccessTokenResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOGcpOidcServiceAccountAccessTokenResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOGcpOidcServiceAccountAccessTokenResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GcpOidcAccessTokenRequest,
) -> Response[Error | Failure | ResponseDTOGcpOidcServiceAccountAccessTokenResponse]:
    """Generates an OIDC Service Account Access Token for GCP

    Args:
        body (GcpOidcAccessTokenRequest): This contains GCP OIDC Access Token request details

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOGcpOidcServiceAccountAccessTokenResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: GcpOidcAccessTokenRequest,
) -> Error | Failure | ResponseDTOGcpOidcServiceAccountAccessTokenResponse | None:
    """Generates an OIDC Service Account Access Token for GCP

    Args:
        body (GcpOidcAccessTokenRequest): This contains GCP OIDC Access Token request details

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOGcpOidcServiceAccountAccessTokenResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GcpOidcAccessTokenRequest,
) -> Response[Error | Failure | ResponseDTOGcpOidcServiceAccountAccessTokenResponse]:
    """Generates an OIDC Service Account Access Token for GCP

    Args:
        body (GcpOidcAccessTokenRequest): This contains GCP OIDC Access Token request details

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOGcpOidcServiceAccountAccessTokenResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GcpOidcAccessTokenRequest,
) -> Error | Failure | ResponseDTOGcpOidcServiceAccountAccessTokenResponse | None:
    """Generates an OIDC Service Account Access Token for GCP

    Args:
        body (GcpOidcAccessTokenRequest): This contains GCP OIDC Access Token request details

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOGcpOidcServiceAccountAccessTokenResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
