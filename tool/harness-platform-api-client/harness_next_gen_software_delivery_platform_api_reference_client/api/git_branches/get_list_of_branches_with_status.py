from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.get_list_of_branches_with_status_branch_sync_status import (
    GetListOfBranchesWithStatusBranchSyncStatus,
)
from ...models.response_dto_git_branch_list import ResponseDTOGitBranchList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    yaml_git_config_identifier: str,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = UNSET,
    search_term: str | Unset = "",
    branch_sync_status: GetListOfBranchesWithStatusBranchSyncStatus | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["yamlGitConfigIdentifier"] = yaml_git_config_identifier

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["page"] = page

    params["size"] = size

    params["searchTerm"] = search_term

    json_branch_sync_status: str | Unset = UNSET
    if not isinstance(branch_sync_status, Unset):
        json_branch_sync_status = branch_sync_status

    params["branchSyncStatus"] = json_branch_sync_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/git-sync-branch/listBranchesWithStatus",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOGitBranchList:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOGitBranchList.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOGitBranchList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    yaml_git_config_identifier: str,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = UNSET,
    search_term: str | Unset = "",
    branch_sync_status: GetListOfBranchesWithStatusBranchSyncStatus | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOGitBranchList]:
    """Lists branches with their status(Synced, Unsynced) by Git Sync Config Id for the given scope

    Args:
        yaml_git_config_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):
        search_term (str | Unset):  Default: ''.
        branch_sync_status (GetListOfBranchesWithStatusBranchSyncStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOGitBranchList]
    """

    kwargs = _get_kwargs(
        yaml_git_config_identifier=yaml_git_config_identifier,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        page=page,
        size=size,
        search_term=search_term,
        branch_sync_status=branch_sync_status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    yaml_git_config_identifier: str,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = UNSET,
    search_term: str | Unset = "",
    branch_sync_status: GetListOfBranchesWithStatusBranchSyncStatus | Unset = UNSET,
) -> Error | Failure | ResponseDTOGitBranchList | None:
    """Lists branches with their status(Synced, Unsynced) by Git Sync Config Id for the given scope

    Args:
        yaml_git_config_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):
        search_term (str | Unset):  Default: ''.
        branch_sync_status (GetListOfBranchesWithStatusBranchSyncStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOGitBranchList
    """

    return sync_detailed(
        client=client,
        yaml_git_config_identifier=yaml_git_config_identifier,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        page=page,
        size=size,
        search_term=search_term,
        branch_sync_status=branch_sync_status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    yaml_git_config_identifier: str,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = UNSET,
    search_term: str | Unset = "",
    branch_sync_status: GetListOfBranchesWithStatusBranchSyncStatus | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOGitBranchList]:
    """Lists branches with their status(Synced, Unsynced) by Git Sync Config Id for the given scope

    Args:
        yaml_git_config_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):
        search_term (str | Unset):  Default: ''.
        branch_sync_status (GetListOfBranchesWithStatusBranchSyncStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOGitBranchList]
    """

    kwargs = _get_kwargs(
        yaml_git_config_identifier=yaml_git_config_identifier,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        page=page,
        size=size,
        search_term=search_term,
        branch_sync_status=branch_sync_status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    yaml_git_config_identifier: str,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = UNSET,
    search_term: str | Unset = "",
    branch_sync_status: GetListOfBranchesWithStatusBranchSyncStatus | Unset = UNSET,
) -> Error | Failure | ResponseDTOGitBranchList | None:
    """Lists branches with their status(Synced, Unsynced) by Git Sync Config Id for the given scope

    Args:
        yaml_git_config_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):
        search_term (str | Unset):  Default: ''.
        branch_sync_status (GetListOfBranchesWithStatusBranchSyncStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOGitBranchList
    """

    return (
        await asyncio_detailed(
            client=client,
            yaml_git_config_identifier=yaml_git_config_identifier,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            page=page,
            size=size,
            search_term=search_term,
            branch_sync_status=branch_sync_status,
        )
    ).parsed
