from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.types_scopes_labels import TypesScopesLabels
from ...models.usererror_error import UsererrorError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    repo_identifier: str,
    pullreq_number: int,
    *,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 30,
    assignable: bool | Unset = False,
    query: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["page"] = page

    params["limit"] = limit

    params["assignable"] = assignable

    params["query"] = query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repos/{repo_identifier}/pullreq/{pullreq_number}/labels".format(
            repo_identifier=quote(str(repo_identifier), safe=""),
            pullreq_number=quote(str(pullreq_number), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TypesScopesLabels | UsererrorError | None:
    if response.status_code == 200:
        response_200 = TypesScopesLabels.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UsererrorError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UsererrorError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UsererrorError.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = UsererrorError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TypesScopesLabels | UsererrorError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    repo_identifier: str,
    pullreq_number: int,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 30,
    assignable: bool | Unset = False,
    query: str | Unset = UNSET,
) -> Response[TypesScopesLabels | UsererrorError]:
    """List labels assigned to pull request

    Args:
        repo_identifier (str):
        pullreq_number (int):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.
        assignable (bool | Unset):  Default: False.
        query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TypesScopesLabels | UsererrorError]
    """

    kwargs = _get_kwargs(
        repo_identifier=repo_identifier,
        pullreq_number=pullreq_number,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        page=page,
        limit=limit,
        assignable=assignable,
        query=query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    repo_identifier: str,
    pullreq_number: int,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 30,
    assignable: bool | Unset = False,
    query: str | Unset = UNSET,
) -> TypesScopesLabels | UsererrorError | None:
    """List labels assigned to pull request

    Args:
        repo_identifier (str):
        pullreq_number (int):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.
        assignable (bool | Unset):  Default: False.
        query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TypesScopesLabels | UsererrorError
    """

    return sync_detailed(
        repo_identifier=repo_identifier,
        pullreq_number=pullreq_number,
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        page=page,
        limit=limit,
        assignable=assignable,
        query=query,
    ).parsed


async def asyncio_detailed(
    repo_identifier: str,
    pullreq_number: int,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 30,
    assignable: bool | Unset = False,
    query: str | Unset = UNSET,
) -> Response[TypesScopesLabels | UsererrorError]:
    """List labels assigned to pull request

    Args:
        repo_identifier (str):
        pullreq_number (int):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.
        assignable (bool | Unset):  Default: False.
        query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TypesScopesLabels | UsererrorError]
    """

    kwargs = _get_kwargs(
        repo_identifier=repo_identifier,
        pullreq_number=pullreq_number,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        page=page,
        limit=limit,
        assignable=assignable,
        query=query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    repo_identifier: str,
    pullreq_number: int,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 30,
    assignable: bool | Unset = False,
    query: str | Unset = UNSET,
) -> TypesScopesLabels | UsererrorError | None:
    """List labels assigned to pull request

    Args:
        repo_identifier (str):
        pullreq_number (int):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.
        assignable (bool | Unset):  Default: False.
        query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TypesScopesLabels | UsererrorError
    """

    return (
        await asyncio_detailed(
            repo_identifier=repo_identifier,
            pullreq_number=pullreq_number,
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            page=page,
            limit=limit,
            assignable=assignable,
            query=query,
        )
    ).parsed
