from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.types_label import TypesLabel
from ...models.usererror_error import UsererrorError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    repo_identifier: str,
    *,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 30,
    inherited: bool | Unset = False,
    query: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["page"] = page

    params["limit"] = limit

    params["inherited"] = inherited

    params["query"] = query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repos/{repo_identifier}/labels".format(
            repo_identifier=quote(str(repo_identifier), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UsererrorError | list[TypesLabel] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TypesLabel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[UsererrorError | list[TypesLabel]]:
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
    page: int | Unset = 1,
    limit: int | Unset = 30,
    inherited: bool | Unset = False,
    query: str | Unset = UNSET,
) -> Response[UsererrorError | list[TypesLabel]]:
    """List labels at repo level

    Args:
        repo_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.
        inherited (bool | Unset):  Default: False.
        query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsererrorError | list[TypesLabel]]
    """

    kwargs = _get_kwargs(
        repo_identifier=repo_identifier,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        page=page,
        limit=limit,
        inherited=inherited,
        query=query,
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
    page: int | Unset = 1,
    limit: int | Unset = 30,
    inherited: bool | Unset = False,
    query: str | Unset = UNSET,
) -> UsererrorError | list[TypesLabel] | None:
    """List labels at repo level

    Args:
        repo_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.
        inherited (bool | Unset):  Default: False.
        query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsererrorError | list[TypesLabel]
    """

    return sync_detailed(
        repo_identifier=repo_identifier,
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        page=page,
        limit=limit,
        inherited=inherited,
        query=query,
    ).parsed


async def asyncio_detailed(
    repo_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 30,
    inherited: bool | Unset = False,
    query: str | Unset = UNSET,
) -> Response[UsererrorError | list[TypesLabel]]:
    """List labels at repo level

    Args:
        repo_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.
        inherited (bool | Unset):  Default: False.
        query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsererrorError | list[TypesLabel]]
    """

    kwargs = _get_kwargs(
        repo_identifier=repo_identifier,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        page=page,
        limit=limit,
        inherited=inherited,
        query=query,
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
    page: int | Unset = 1,
    limit: int | Unset = 30,
    inherited: bool | Unset = False,
    query: str | Unset = UNSET,
) -> UsererrorError | list[TypesLabel] | None:
    """List labels at repo level

    Args:
        repo_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 30.
        inherited (bool | Unset):  Default: False.
        query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsererrorError | list[TypesLabel]
    """

    return (
        await asyncio_detailed(
            repo_identifier=repo_identifier,
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            page=page,
            limit=limit,
            inherited=inherited,
            query=query,
        )
    ).parsed
