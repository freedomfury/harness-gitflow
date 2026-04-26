from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_tags_order import ListTagsOrder
from ...models.list_tags_sort import ListTagsSort
from ...models.types_commit_tag import TypesCommitTag
from ...models.usererror_error import UsererrorError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    repo_identifier: str,
    *,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    include_commit: bool | Unset = False,
    query: str | Unset = UNSET,
    order: ListTagsOrder | Unset = ListTagsOrder.ASC,
    sort: ListTagsSort | Unset = ListTagsSort.NAME,
    page: int | Unset = 1,
    limit: int | Unset = 30,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["include_commit"] = include_commit

    params["query"] = query

    json_order: str | Unset = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repos/{repo_identifier}/tags".format(
            repo_identifier=quote(str(repo_identifier), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UsererrorError | list[TypesCommitTag] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TypesCommitTag.from_dict(response_200_item_data)

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
) -> Response[UsererrorError | list[TypesCommitTag]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    repo_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    include_commit: bool | Unset = False,
    query: str | Unset = UNSET,
    order: ListTagsOrder | Unset = ListTagsOrder.ASC,
    sort: ListTagsSort | Unset = ListTagsSort.NAME,
    page: int | Unset = 1,
    limit: int | Unset = 30,
) -> Response[UsererrorError | list[TypesCommitTag]]:
    """List tags

    Args:
        repo_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        include_commit (bool | Unset):  Default: False.
        query (str | Unset):
        order (ListTagsOrder | Unset):  Default: ListTagsOrder.ASC.
        sort (ListTagsSort | Unset):  Default: ListTagsSort.NAME.
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsererrorError | list[TypesCommitTag]]
    """

    kwargs = _get_kwargs(
        repo_identifier=repo_identifier,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        include_commit=include_commit,
        query=query,
        order=order,
        sort=sort,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    repo_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    include_commit: bool | Unset = False,
    query: str | Unset = UNSET,
    order: ListTagsOrder | Unset = ListTagsOrder.ASC,
    sort: ListTagsSort | Unset = ListTagsSort.NAME,
    page: int | Unset = 1,
    limit: int | Unset = 30,
) -> UsererrorError | list[TypesCommitTag] | None:
    """List tags

    Args:
        repo_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        include_commit (bool | Unset):  Default: False.
        query (str | Unset):
        order (ListTagsOrder | Unset):  Default: ListTagsOrder.ASC.
        sort (ListTagsSort | Unset):  Default: ListTagsSort.NAME.
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsererrorError | list[TypesCommitTag]
    """

    return sync_detailed(
        repo_identifier=repo_identifier,
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        include_commit=include_commit,
        query=query,
        order=order,
        sort=sort,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    repo_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    include_commit: bool | Unset = False,
    query: str | Unset = UNSET,
    order: ListTagsOrder | Unset = ListTagsOrder.ASC,
    sort: ListTagsSort | Unset = ListTagsSort.NAME,
    page: int | Unset = 1,
    limit: int | Unset = 30,
) -> Response[UsererrorError | list[TypesCommitTag]]:
    """List tags

    Args:
        repo_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        include_commit (bool | Unset):  Default: False.
        query (str | Unset):
        order (ListTagsOrder | Unset):  Default: ListTagsOrder.ASC.
        sort (ListTagsSort | Unset):  Default: ListTagsSort.NAME.
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsererrorError | list[TypesCommitTag]]
    """

    kwargs = _get_kwargs(
        repo_identifier=repo_identifier,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        include_commit=include_commit,
        query=query,
        order=order,
        sort=sort,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    repo_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    include_commit: bool | Unset = False,
    query: str | Unset = UNSET,
    order: ListTagsOrder | Unset = ListTagsOrder.ASC,
    sort: ListTagsSort | Unset = ListTagsSort.NAME,
    page: int | Unset = 1,
    limit: int | Unset = 30,
) -> UsererrorError | list[TypesCommitTag] | None:
    """List tags

    Args:
        repo_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        include_commit (bool | Unset):  Default: False.
        query (str | Unset):
        order (ListTagsOrder | Unset):  Default: ListTagsOrder.ASC.
        sort (ListTagsSort | Unset):  Default: ListTagsSort.NAME.
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsererrorError | list[TypesCommitTag]
    """

    return (
        await asyncio_detailed(
            repo_identifier=repo_identifier,
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            include_commit=include_commit,
            query=query,
            order=order,
            sort=sort,
            page=page,
            limit=limit,
        )
    ).parsed
