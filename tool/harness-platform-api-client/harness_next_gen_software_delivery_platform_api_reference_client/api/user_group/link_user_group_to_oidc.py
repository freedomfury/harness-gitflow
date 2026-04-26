from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.oidc_link_group_request import OidcLinkGroupRequest
from ...models.rest_response_user_group import RestResponseUserGroup
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_group_id: str,
    provider_id: str,
    *,
    body: OidcLinkGroupRequest,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/user-groups/{user_group_id}/link/oidc/{provider_id}".format(
            user_group_id=quote(str(user_group_id), safe=""),
            provider_id=quote(str(provider_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | RestResponseUserGroup:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = RestResponseUserGroup.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | RestResponseUserGroup]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_group_id: str,
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OidcLinkGroupRequest,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> Response[Error | Failure | RestResponseUserGroup]:
    """Link OIDC Group to the User Group in an account/org/project

    Args:
        user_group_id (str):
        provider_id (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        body (OidcLinkGroupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | RestResponseUserGroup]
    """

    kwargs = _get_kwargs(
        user_group_id=user_group_id,
        provider_id=provider_id,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_group_id: str,
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OidcLinkGroupRequest,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> Error | Failure | RestResponseUserGroup | None:
    """Link OIDC Group to the User Group in an account/org/project

    Args:
        user_group_id (str):
        provider_id (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        body (OidcLinkGroupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | RestResponseUserGroup
    """

    return sync_detailed(
        user_group_id=user_group_id,
        provider_id=provider_id,
        client=client,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
    ).parsed


async def asyncio_detailed(
    user_group_id: str,
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OidcLinkGroupRequest,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> Response[Error | Failure | RestResponseUserGroup]:
    """Link OIDC Group to the User Group in an account/org/project

    Args:
        user_group_id (str):
        provider_id (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        body (OidcLinkGroupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | RestResponseUserGroup]
    """

    kwargs = _get_kwargs(
        user_group_id=user_group_id,
        provider_id=provider_id,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_group_id: str,
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OidcLinkGroupRequest,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> Error | Failure | RestResponseUserGroup | None:
    """Link OIDC Group to the User Group in an account/org/project

    Args:
        user_group_id (str):
        provider_id (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        body (OidcLinkGroupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | RestResponseUserGroup
    """

    return (
        await asyncio_detailed(
            user_group_id=user_group_id,
            provider_id=provider_id,
            client=client,
            body=body,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
        )
    ).parsed
