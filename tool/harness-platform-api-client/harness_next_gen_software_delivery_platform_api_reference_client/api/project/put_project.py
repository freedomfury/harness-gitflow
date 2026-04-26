from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.project_request import ProjectRequest
from ...models.response_dto_project_response import ResponseDTOProjectResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    identifier: str,
    *,
    body: ProjectRequest,
    account_identifier: str,
    org_identifier: str | Unset = "default",
    if_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/projects/{identifier}".format(
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
) -> Error | Failure | ResponseDTOProjectResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOProjectResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOProjectResponse]:
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
    body: ProjectRequest,
    account_identifier: str,
    org_identifier: str | Unset = "default",
    if_match: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOProjectResponse]:
    """Update a Project

     Updates Project details for the given ID.

    Args:
        identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):  Default: 'default'.
        if_match (str | Unset):
        body (ProjectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOProjectResponse]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
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
    body: ProjectRequest,
    account_identifier: str,
    org_identifier: str | Unset = "default",
    if_match: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOProjectResponse | None:
    """Update a Project

     Updates Project details for the given ID.

    Args:
        identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):  Default: 'default'.
        if_match (str | Unset):
        body (ProjectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOProjectResponse
    """

    return sync_detailed(
        identifier=identifier,
        client=client,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProjectRequest,
    account_identifier: str,
    org_identifier: str | Unset = "default",
    if_match: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOProjectResponse]:
    """Update a Project

     Updates Project details for the given ID.

    Args:
        identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):  Default: 'default'.
        if_match (str | Unset):
        body (ProjectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOProjectResponse]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProjectRequest,
    account_identifier: str,
    org_identifier: str | Unset = "default",
    if_match: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOProjectResponse | None:
    """Update a Project

     Updates Project details for the given ID.

    Args:
        identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):  Default: 'default'.
        if_match (str | Unset):
        body (ProjectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOProjectResponse
    """

    return (
        await asyncio_detailed(
            identifier=identifier,
            client=client,
            body=body,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            if_match=if_match,
        )
    ).parsed
