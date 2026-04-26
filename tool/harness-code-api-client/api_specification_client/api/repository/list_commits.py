from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.types_list_commit_response import TypesListCommitResponse
from ...models.usererror_error import UsererrorError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    repo_identifier: str,
    *,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    git_ref: str | Unset = "{Repository Default Branch}",
    after: str | Unset = UNSET,
    path: str | Unset = "",
    since: int | Unset = UNSET,
    until: int | Unset = UNSET,
    committer: str | Unset = UNSET,
    committer_id: list[int] | Unset = UNSET,
    author: str | Unset = UNSET,
    author_id: list[int] | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 30,
    include_stats: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["git_ref"] = git_ref

    params["after"] = after

    params["path"] = path

    params["since"] = since

    params["until"] = until

    params["committer"] = committer

    json_committer_id: list[int] | Unset = UNSET
    if not isinstance(committer_id, Unset):
        json_committer_id = committer_id

    params["committer_id"] = json_committer_id

    params["author"] = author

    json_author_id: list[int] | Unset = UNSET
    if not isinstance(author_id, Unset):
        json_author_id = author_id

    params["author_id"] = json_author_id

    params["page"] = page

    params["limit"] = limit

    params["include_stats"] = include_stats

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repos/{repo_identifier}/commits".format(
            repo_identifier=quote(str(repo_identifier), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TypesListCommitResponse | UsererrorError | None:
    if response.status_code == 200:
        response_200 = TypesListCommitResponse.from_dict(response.json())

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
) -> Response[TypesListCommitResponse | UsererrorError]:
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
    git_ref: str | Unset = "{Repository Default Branch}",
    after: str | Unset = UNSET,
    path: str | Unset = "",
    since: int | Unset = UNSET,
    until: int | Unset = UNSET,
    committer: str | Unset = UNSET,
    committer_id: list[int] | Unset = UNSET,
    author: str | Unset = UNSET,
    author_id: list[int] | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 30,
    include_stats: bool | Unset = False,
) -> Response[TypesListCommitResponse | UsererrorError]:
    """List commits

    Args:
        repo_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        git_ref (str | Unset):  Default: '{Repository Default Branch}'.
        after (str | Unset):
        path (str | Unset):  Default: ''.
        since (int | Unset):  Example: 1728348213.0.
        until (int | Unset):  Example: 1746668446.0.
        committer (str | Unset):
        committer_id (list[int] | Unset):
        author (str | Unset):
        author_id (list[int] | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.
        include_stats (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TypesListCommitResponse | UsererrorError]
    """

    kwargs = _get_kwargs(
        repo_identifier=repo_identifier,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        git_ref=git_ref,
        after=after,
        path=path,
        since=since,
        until=until,
        committer=committer,
        committer_id=committer_id,
        author=author,
        author_id=author_id,
        page=page,
        limit=limit,
        include_stats=include_stats,
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
    git_ref: str | Unset = "{Repository Default Branch}",
    after: str | Unset = UNSET,
    path: str | Unset = "",
    since: int | Unset = UNSET,
    until: int | Unset = UNSET,
    committer: str | Unset = UNSET,
    committer_id: list[int] | Unset = UNSET,
    author: str | Unset = UNSET,
    author_id: list[int] | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 30,
    include_stats: bool | Unset = False,
) -> TypesListCommitResponse | UsererrorError | None:
    """List commits

    Args:
        repo_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        git_ref (str | Unset):  Default: '{Repository Default Branch}'.
        after (str | Unset):
        path (str | Unset):  Default: ''.
        since (int | Unset):  Example: 1728348213.0.
        until (int | Unset):  Example: 1746668446.0.
        committer (str | Unset):
        committer_id (list[int] | Unset):
        author (str | Unset):
        author_id (list[int] | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.
        include_stats (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TypesListCommitResponse | UsererrorError
    """

    return sync_detailed(
        repo_identifier=repo_identifier,
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        git_ref=git_ref,
        after=after,
        path=path,
        since=since,
        until=until,
        committer=committer,
        committer_id=committer_id,
        author=author,
        author_id=author_id,
        page=page,
        limit=limit,
        include_stats=include_stats,
    ).parsed


async def asyncio_detailed(
    repo_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    git_ref: str | Unset = "{Repository Default Branch}",
    after: str | Unset = UNSET,
    path: str | Unset = "",
    since: int | Unset = UNSET,
    until: int | Unset = UNSET,
    committer: str | Unset = UNSET,
    committer_id: list[int] | Unset = UNSET,
    author: str | Unset = UNSET,
    author_id: list[int] | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 30,
    include_stats: bool | Unset = False,
) -> Response[TypesListCommitResponse | UsererrorError]:
    """List commits

    Args:
        repo_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        git_ref (str | Unset):  Default: '{Repository Default Branch}'.
        after (str | Unset):
        path (str | Unset):  Default: ''.
        since (int | Unset):  Example: 1728348213.0.
        until (int | Unset):  Example: 1746668446.0.
        committer (str | Unset):
        committer_id (list[int] | Unset):
        author (str | Unset):
        author_id (list[int] | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.
        include_stats (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TypesListCommitResponse | UsererrorError]
    """

    kwargs = _get_kwargs(
        repo_identifier=repo_identifier,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        git_ref=git_ref,
        after=after,
        path=path,
        since=since,
        until=until,
        committer=committer,
        committer_id=committer_id,
        author=author,
        author_id=author_id,
        page=page,
        limit=limit,
        include_stats=include_stats,
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
    git_ref: str | Unset = "{Repository Default Branch}",
    after: str | Unset = UNSET,
    path: str | Unset = "",
    since: int | Unset = UNSET,
    until: int | Unset = UNSET,
    committer: str | Unset = UNSET,
    committer_id: list[int] | Unset = UNSET,
    author: str | Unset = UNSET,
    author_id: list[int] | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 30,
    include_stats: bool | Unset = False,
) -> TypesListCommitResponse | UsererrorError | None:
    """List commits

    Args:
        repo_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        git_ref (str | Unset):  Default: '{Repository Default Branch}'.
        after (str | Unset):
        path (str | Unset):  Default: ''.
        since (int | Unset):  Example: 1728348213.0.
        until (int | Unset):  Example: 1746668446.0.
        committer (str | Unset):
        committer_id (list[int] | Unset):
        author (str | Unset):
        author_id (list[int] | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.
        include_stats (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TypesListCommitResponse | UsererrorError
    """

    return (
        await asyncio_detailed(
            repo_identifier=repo_identifier,
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            git_ref=git_ref,
            after=after,
            path=path,
            since=since,
            until=until,
            committer=committer,
            committer_id=committer_id,
            author=author,
            author_id=author_id,
            page=page,
            limit=limit,
            include_stats=include_stats,
        )
    ).parsed
