from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.git_sync_config import GitSyncConfig
from ...types import UNSET, Response, Unset


def _get_kwargs(
    identifier: str,
    folder_identifier: str,
    *,
    project_id: str | Unset = UNSET,
    organization_id: str | Unset = UNSET,
    account_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["projectId"] = project_id

    params["organizationId"] = organization_id

    params["accountId"] = account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/git-sync/{identifier}/folder/{folder_identifier}/default".format(
            identifier=quote(str(identifier), safe=""),
            folder_identifier=quote(str(folder_identifier), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | GitSyncConfig:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = GitSyncConfig.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | GitSyncConfig]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    identifier: str,
    folder_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
    organization_id: str | Unset = UNSET,
    account_id: str,
) -> Response[Error | Failure | GitSyncConfig]:
    """Update existing Git Sync Config default root folder by Identifier

    Args:
        identifier (str):
        folder_identifier (str):
        project_id (str | Unset):
        organization_id (str | Unset):
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | GitSyncConfig]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        folder_identifier=folder_identifier,
        project_id=project_id,
        organization_id=organization_id,
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    identifier: str,
    folder_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
    organization_id: str | Unset = UNSET,
    account_id: str,
) -> Error | Failure | GitSyncConfig | None:
    """Update existing Git Sync Config default root folder by Identifier

    Args:
        identifier (str):
        folder_identifier (str):
        project_id (str | Unset):
        organization_id (str | Unset):
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | GitSyncConfig
    """

    return sync_detailed(
        identifier=identifier,
        folder_identifier=folder_identifier,
        client=client,
        project_id=project_id,
        organization_id=organization_id,
        account_id=account_id,
    ).parsed


async def asyncio_detailed(
    identifier: str,
    folder_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
    organization_id: str | Unset = UNSET,
    account_id: str,
) -> Response[Error | Failure | GitSyncConfig]:
    """Update existing Git Sync Config default root folder by Identifier

    Args:
        identifier (str):
        folder_identifier (str):
        project_id (str | Unset):
        organization_id (str | Unset):
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | GitSyncConfig]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        folder_identifier=folder_identifier,
        project_id=project_id,
        organization_id=organization_id,
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    identifier: str,
    folder_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
    organization_id: str | Unset = UNSET,
    account_id: str,
) -> Error | Failure | GitSyncConfig | None:
    """Update existing Git Sync Config default root folder by Identifier

    Args:
        identifier (str):
        folder_identifier (str):
        project_id (str | Unset):
        organization_id (str | Unset):
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | GitSyncConfig
    """

    return (
        await asyncio_detailed(
            identifier=identifier,
            folder_identifier=folder_identifier,
            client=client,
            project_id=project_id,
            organization_id=organization_id,
            account_id=account_id,
        )
    ).parsed
