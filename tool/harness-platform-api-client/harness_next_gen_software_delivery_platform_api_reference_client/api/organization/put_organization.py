from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.organization_request import OrganizationRequest
from ...models.response_dto_organization_response import ResponseDTOOrganizationResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    identifier: str,
    *,
    body: OrganizationRequest,
    account_identifier: str,
    if_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/organizations/{identifier}".format(
            identifier=quote(str(identifier), safe=""),
        ),
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
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: OrganizationRequest,
    account_identifier: str,
    if_match: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOOrganizationResponse]:
    """Update an Organization

     Updates Organization settings.

    Args:
        identifier (str):
        account_identifier (str):
        if_match (str | Unset):
        body (OrganizationRequest): This contains details of the Organization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOOrganizationResponse]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        body=body,
        account_identifier=account_identifier,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: OrganizationRequest,
    account_identifier: str,
    if_match: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOOrganizationResponse | None:
    """Update an Organization

     Updates Organization settings.

    Args:
        identifier (str):
        account_identifier (str):
        if_match (str | Unset):
        body (OrganizationRequest): This contains details of the Organization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOOrganizationResponse
    """

    return sync_detailed(
        identifier=identifier,
        client=client,
        body=body,
        account_identifier=account_identifier,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: OrganizationRequest,
    account_identifier: str,
    if_match: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOOrganizationResponse]:
    """Update an Organization

     Updates Organization settings.

    Args:
        identifier (str):
        account_identifier (str):
        if_match (str | Unset):
        body (OrganizationRequest): This contains details of the Organization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOOrganizationResponse]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        body=body,
        account_identifier=account_identifier,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: OrganizationRequest,
    account_identifier: str,
    if_match: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOOrganizationResponse | None:
    """Update an Organization

     Updates Organization settings.

    Args:
        identifier (str):
        account_identifier (str):
        if_match (str | Unset):
        body (OrganizationRequest): This contains details of the Organization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOOrganizationResponse
    """

    return (
        await asyncio_detailed(
            identifier=identifier,
            client=client,
            body=body,
            account_identifier=account_identifier,
            if_match=if_match,
        )
    ).parsed
