from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_repos_order import ListReposOrder
from ...models.list_repos_sort import ListReposSort
from ...models.repo_repository_output import RepoRepositoryOutput
from ...models.usererror_error import UsererrorError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    query: str | Unset = UNSET,
    sort: ListReposSort | Unset = ListReposSort.IDENTIFIER,
    order: ListReposOrder | Unset = ListReposOrder.ASC,
    page: int | Unset = 1,
    limit: int | Unset = 30,
    only_favorites: bool | Unset = False,
    recursive: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["query"] = query

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    json_order: str | Unset = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["page"] = page

    params["limit"] = limit

    params["only_favorites"] = only_favorites

    params["recursive"] = recursive

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repos",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UsererrorError | list[RepoRepositoryOutput] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RepoRepositoryOutput.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = UsererrorError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UsererrorError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UsererrorError.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = UsererrorError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UsererrorError | list[RepoRepositoryOutput]]:
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
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    query: str | Unset = UNSET,
    sort: ListReposSort | Unset = ListReposSort.IDENTIFIER,
    order: ListReposOrder | Unset = ListReposOrder.ASC,
    page: int | Unset = 1,
    limit: int | Unset = 30,
    only_favorites: bool | Unset = False,
    recursive: bool | Unset = False,
) -> Response[UsererrorError | list[RepoRepositoryOutput]]:
    """List repositories

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        query (str | Unset):
        sort (ListReposSort | Unset):  Default: ListReposSort.IDENTIFIER.
        order (ListReposOrder | Unset):  Default: ListReposOrder.ASC.
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.
        only_favorites (bool | Unset):  Default: False.
        recursive (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsererrorError | list[RepoRepositoryOutput]]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        query=query,
        sort=sort,
        order=order,
        page=page,
        limit=limit,
        only_favorites=only_favorites,
        recursive=recursive,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    query: str | Unset = UNSET,
    sort: ListReposSort | Unset = ListReposSort.IDENTIFIER,
    order: ListReposOrder | Unset = ListReposOrder.ASC,
    page: int | Unset = 1,
    limit: int | Unset = 30,
    only_favorites: bool | Unset = False,
    recursive: bool | Unset = False,
) -> UsererrorError | list[RepoRepositoryOutput] | None:
    """List repositories

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        query (str | Unset):
        sort (ListReposSort | Unset):  Default: ListReposSort.IDENTIFIER.
        order (ListReposOrder | Unset):  Default: ListReposOrder.ASC.
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.
        only_favorites (bool | Unset):  Default: False.
        recursive (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsererrorError | list[RepoRepositoryOutput]
    """

    return sync_detailed(
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        query=query,
        sort=sort,
        order=order,
        page=page,
        limit=limit,
        only_favorites=only_favorites,
        recursive=recursive,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    query: str | Unset = UNSET,
    sort: ListReposSort | Unset = ListReposSort.IDENTIFIER,
    order: ListReposOrder | Unset = ListReposOrder.ASC,
    page: int | Unset = 1,
    limit: int | Unset = 30,
    only_favorites: bool | Unset = False,
    recursive: bool | Unset = False,
) -> Response[UsererrorError | list[RepoRepositoryOutput]]:
    """List repositories

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        query (str | Unset):
        sort (ListReposSort | Unset):  Default: ListReposSort.IDENTIFIER.
        order (ListReposOrder | Unset):  Default: ListReposOrder.ASC.
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.
        only_favorites (bool | Unset):  Default: False.
        recursive (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsererrorError | list[RepoRepositoryOutput]]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        query=query,
        sort=sort,
        order=order,
        page=page,
        limit=limit,
        only_favorites=only_favorites,
        recursive=recursive,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    query: str | Unset = UNSET,
    sort: ListReposSort | Unset = ListReposSort.IDENTIFIER,
    order: ListReposOrder | Unset = ListReposOrder.ASC,
    page: int | Unset = 1,
    limit: int | Unset = 30,
    only_favorites: bool | Unset = False,
    recursive: bool | Unset = False,
) -> UsererrorError | list[RepoRepositoryOutput] | None:
    """List repositories

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        query (str | Unset):
        sort (ListReposSort | Unset):  Default: ListReposSort.IDENTIFIER.
        order (ListReposOrder | Unset):  Default: ListReposOrder.ASC.
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.
        only_favorites (bool | Unset):  Default: False.
        recursive (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsererrorError | list[RepoRepositoryOutput]
    """

    return (
        await asyncio_detailed(
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            query=query,
            sort=sort,
            order=order,
            page=page,
            limit=limit,
            only_favorites=only_favorites,
            recursive=recursive,
        )
    ).parsed
