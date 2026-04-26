from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.aws_oidc_credentials_request import AwsOidcCredentialsRequest
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_aws_oidc_credential_response_dto import ResponseDTOAwsOidcCredentialResponseDto
from ...types import Response


def _get_kwargs(
    *,
    body: AwsOidcCredentialsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/oidc/access-token/aws/webidentity-session-access",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOAwsOidcCredentialResponseDto:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOAwsOidcCredentialResponseDto.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOAwsOidcCredentialResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AwsOidcCredentialsRequest,
) -> Response[Error | Failure | ResponseDTOAwsOidcCredentialResponseDto]:
    """Generate an OIDC IAM Role Credential for AWS

    Args:
        body (AwsOidcCredentialsRequest): This contains Aws OIDC Credentials request details

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOAwsOidcCredentialResponseDto]
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
    body: AwsOidcCredentialsRequest,
) -> Error | Failure | ResponseDTOAwsOidcCredentialResponseDto | None:
    """Generate an OIDC IAM Role Credential for AWS

    Args:
        body (AwsOidcCredentialsRequest): This contains Aws OIDC Credentials request details

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOAwsOidcCredentialResponseDto
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AwsOidcCredentialsRequest,
) -> Response[Error | Failure | ResponseDTOAwsOidcCredentialResponseDto]:
    """Generate an OIDC IAM Role Credential for AWS

    Args:
        body (AwsOidcCredentialsRequest): This contains Aws OIDC Credentials request details

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOAwsOidcCredentialResponseDto]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AwsOidcCredentialsRequest,
) -> Error | Failure | ResponseDTOAwsOidcCredentialResponseDto | None:
    """Generate an OIDC IAM Role Credential for AWS

    Args:
        body (AwsOidcCredentialsRequest): This contains Aws OIDC Credentials request details

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOAwsOidcCredentialResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
