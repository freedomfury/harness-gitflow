from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.filter_properties import FilterProperties
from ...models.response_dto_page_response_environment_group import ResponseDTOPageResponseEnvironmentGroup
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: FilterProperties | Unset = UNSET,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    env_group_identifiers: list[str] | Unset = UNSET,
    search_term: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 25,
    sort: list[str] | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    include_all_env_groups_accessible_at_scope: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    json_env_group_identifiers: list[str] | Unset = UNSET
    if not isinstance(env_group_identifiers, Unset):
        json_env_group_identifiers = env_group_identifiers

    params["envGroupIdentifiers"] = json_env_group_identifiers

    params["searchTerm"] = search_term

    params["page"] = page

    params["size"] = size

    json_sort: list[str] | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params["filterIdentifier"] = filter_identifier

    params["branch"] = branch

    params["repoIdentifier"] = repo_identifier

    params["getDefaultFromOtherRepo"] = get_default_from_other_repo

    params["includeAllEnvGroupsAccessibleAtScope"] = include_all_env_groups_accessible_at_scope

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/environmentGroup/list",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOPageResponseEnvironmentGroup:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOPageResponseEnvironmentGroup.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOPageResponseEnvironmentGroup]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FilterProperties | Unset = UNSET,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    env_group_identifiers: list[str] | Unset = UNSET,
    search_term: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 25,
    sort: list[str] | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    include_all_env_groups_accessible_at_scope: bool | Unset = False,
) -> Response[Error | Failure | ResponseDTOPageResponseEnvironmentGroup]:
    """Gets Environment Group list

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        env_group_identifiers (list[str] | Unset):
        search_term (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 25.
        sort (list[str] | Unset):
        filter_identifier (str | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        include_all_env_groups_accessible_at_scope (bool | Unset):  Default: False.
        body (FilterProperties | Unset): Properties of the Filter entity defined in Harness.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageResponseEnvironmentGroup]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        env_group_identifiers=env_group_identifiers,
        search_term=search_term,
        page=page,
        size=size,
        sort=sort,
        filter_identifier=filter_identifier,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
        include_all_env_groups_accessible_at_scope=include_all_env_groups_accessible_at_scope,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: FilterProperties | Unset = UNSET,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    env_group_identifiers: list[str] | Unset = UNSET,
    search_term: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 25,
    sort: list[str] | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    include_all_env_groups_accessible_at_scope: bool | Unset = False,
) -> Error | Failure | ResponseDTOPageResponseEnvironmentGroup | None:
    """Gets Environment Group list

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        env_group_identifiers (list[str] | Unset):
        search_term (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 25.
        sort (list[str] | Unset):
        filter_identifier (str | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        include_all_env_groups_accessible_at_scope (bool | Unset):  Default: False.
        body (FilterProperties | Unset): Properties of the Filter entity defined in Harness.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageResponseEnvironmentGroup
    """

    return sync_detailed(
        client=client,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        env_group_identifiers=env_group_identifiers,
        search_term=search_term,
        page=page,
        size=size,
        sort=sort,
        filter_identifier=filter_identifier,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
        include_all_env_groups_accessible_at_scope=include_all_env_groups_accessible_at_scope,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FilterProperties | Unset = UNSET,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    env_group_identifiers: list[str] | Unset = UNSET,
    search_term: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 25,
    sort: list[str] | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    include_all_env_groups_accessible_at_scope: bool | Unset = False,
) -> Response[Error | Failure | ResponseDTOPageResponseEnvironmentGroup]:
    """Gets Environment Group list

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        env_group_identifiers (list[str] | Unset):
        search_term (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 25.
        sort (list[str] | Unset):
        filter_identifier (str | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        include_all_env_groups_accessible_at_scope (bool | Unset):  Default: False.
        body (FilterProperties | Unset): Properties of the Filter entity defined in Harness.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPageResponseEnvironmentGroup]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        env_group_identifiers=env_group_identifiers,
        search_term=search_term,
        page=page,
        size=size,
        sort=sort,
        filter_identifier=filter_identifier,
        branch=branch,
        repo_identifier=repo_identifier,
        get_default_from_other_repo=get_default_from_other_repo,
        include_all_env_groups_accessible_at_scope=include_all_env_groups_accessible_at_scope,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FilterProperties | Unset = UNSET,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    env_group_identifiers: list[str] | Unset = UNSET,
    search_term: str | Unset = UNSET,
    page: int | Unset = 0,
    size: int | Unset = 25,
    sort: list[str] | Unset = UNSET,
    filter_identifier: str | Unset = UNSET,
    branch: str | Unset = UNSET,
    repo_identifier: str | Unset = UNSET,
    get_default_from_other_repo: bool | Unset = UNSET,
    include_all_env_groups_accessible_at_scope: bool | Unset = False,
) -> Error | Failure | ResponseDTOPageResponseEnvironmentGroup | None:
    """Gets Environment Group list

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        env_group_identifiers (list[str] | Unset):
        search_term (str | Unset):
        page (int | Unset):  Default: 0.
        size (int | Unset):  Default: 25.
        sort (list[str] | Unset):
        filter_identifier (str | Unset):
        branch (str | Unset):
        repo_identifier (str | Unset):
        get_default_from_other_repo (bool | Unset):
        include_all_env_groups_accessible_at_scope (bool | Unset):  Default: False.
        body (FilterProperties | Unset): Properties of the Filter entity defined in Harness.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPageResponseEnvironmentGroup
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            env_group_identifiers=env_group_identifiers,
            search_term=search_term,
            page=page,
            size=size,
            sort=sort,
            filter_identifier=filter_identifier,
            branch=branch,
            repo_identifier=repo_identifier,
            get_default_from_other_repo=get_default_from_other_repo,
            include_all_env_groups_accessible_at_scope=include_all_env_groups_accessible_at_scope,
        )
    ).parsed
