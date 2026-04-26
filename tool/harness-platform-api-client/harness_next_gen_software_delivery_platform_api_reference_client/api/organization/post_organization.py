from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.organization_request import OrganizationRequest
from ...models.response_dto_organization_response import ResponseDTOOrganizationResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: OrganizationRequest,
    account_identifier: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/organizations",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOOrganizationResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOOrganizationResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOOrganizationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: OrganizationRequest,
    account_identifier: str,
) -> Response[Error | Failure | ResponseDTOOrganizationResponse]:
    """Create an Organization

     Creates a new Organization.

    Args:
        account_identifier (str):
        body (OrganizationRequest): This contains details of the Organization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOOrganizationResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: OrganizationRequest,
    account_identifier: str,
) -> Error | Failure | ResponseDTOOrganizationResponse | None:
    """Create an Organization

     Creates a new Organization.

    Args:
        account_identifier (str):
        body (OrganizationRequest): This contains details of the Organization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOOrganizationResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        account_identifier=account_identifier,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: OrganizationRequest,
    account_identifier: str,
) -> Response[Error | Failure | ResponseDTOOrganizationResponse]:
    """Create an Organization

     Creates a new Organization.

    Args:
        account_identifier (str):
        body (OrganizationRequest): This contains details of the Organization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOOrganizationResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: OrganizationRequest,
    account_identifier: str,
) -> Error | Failure | ResponseDTOOrganizationResponse | None:
    """Create an Organization

     Creates a new Organization.

    Args:
        account_identifier (str):
        body (OrganizationRequest): This contains details of the Organization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOOrganizationResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            account_identifier=account_identifier,
        )
    ).parsed
