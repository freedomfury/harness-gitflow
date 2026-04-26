from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.git_enabled import GitEnabled
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_identifier: str,
    project_identifier: str | Unset = UNSET,
    org_identifier: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["projectIdentifier"] = project_identifier

    params["orgIdentifier"] = org_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/git-sync/git-sync-enabled",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Failure | GitEnabled:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = GitEnabled.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | GitEnabled]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    project_identifier: str | Unset = UNSET,
    org_identifier: str | Unset = UNSET,
) -> Response[Error | Failure | GitEnabled]:
    """Check whether Git Sync is enabled for given scope or not

    Args:
        account_identifier (str):
        project_identifier (str | Unset):
        org_identifier (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | GitEnabled]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        project_identifier=project_identifier,
        org_identifier=org_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    project_identifier: str | Unset = UNSET,
    org_identifier: str | Unset = UNSET,
) -> Error | Failure | GitEnabled | None:
    """Check whether Git Sync is enabled for given scope or not

    Args:
        account_identifier (str):
        project_identifier (str | Unset):
        org_identifier (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | GitEnabled
    """

    return sync_detailed(
        client=client,
        account_identifier=account_identifier,
        project_identifier=project_identifier,
        org_identifier=org_identifier,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    project_identifier: str | Unset = UNSET,
    org_identifier: str | Unset = UNSET,
) -> Response[Error | Failure | GitEnabled]:
    """Check whether Git Sync is enabled for given scope or not

    Args:
        account_identifier (str):
        project_identifier (str | Unset):
        org_identifier (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | GitEnabled]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        project_identifier=project_identifier,
        org_identifier=org_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    project_identifier: str | Unset = UNSET,
    org_identifier: str | Unset = UNSET,
) -> Error | Failure | GitEnabled | None:
    """Check whether Git Sync is enabled for given scope or not

    Args:
        account_identifier (str):
        project_identifier (str | Unset):
        org_identifier (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | GitEnabled
    """

    return (
        await asyncio_detailed(
            client=client,
            account_identifier=account_identifier,
            project_identifier=project_identifier,
            org_identifier=org_identifier,
        )
    ).parsed
