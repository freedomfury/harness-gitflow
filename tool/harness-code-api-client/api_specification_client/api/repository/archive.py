from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.usererror_error import UsererrorError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    repo_identifier: str,
    git_ref: str,
    format_: str,
    *,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    path: list[str] | Unset = UNSET,
    prefix: str | Unset = UNSET,
    attributes: str | Unset = UNSET,
    time: str | Unset = UNSET,
    compression: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    json_path: list[str] | Unset = UNSET
    if not isinstance(path, Unset):
        json_path = path

    params["path"] = json_path

    params["prefix"] = prefix

    params["attributes"] = attributes

    params["time"] = time

    params["compression"] = compression

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repos/{repo_identifier}/archive/{git_ref}.{format_}".format(
            repo_identifier=quote(str(repo_identifier), safe=""),
            git_ref=quote(str(git_ref), safe=""),
            format_=quote(str(format_), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UsererrorError | None:
    if response.status_code == 401:
        response_401 = UsererrorError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UsererrorError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UsererrorError.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = UsererrorError.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = UsererrorError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UsererrorError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    repo_identifier: str,
    git_ref: str,
    format_: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    path: list[str] | Unset = UNSET,
    prefix: str | Unset = UNSET,
    attributes: str | Unset = UNSET,
    time: str | Unset = UNSET,
    compression: int | Unset = UNSET,
) -> Response[UsererrorError]:
    """Download repo in archived format

    Args:
        repo_identifier (str):
        git_ref (str):
        format_ (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        path (list[str] | Unset):
        prefix (str | Unset):
        attributes (str | Unset):
        time (str | Unset):
        compression (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsererrorError]
    """

    kwargs = _get_kwargs(
        repo_identifier=repo_identifier,
        git_ref=git_ref,
        format_=format_,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        path=path,
        prefix=prefix,
        attributes=attributes,
        time=time,
        compression=compression,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    repo_identifier: str,
    git_ref: str,
    format_: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    path: list[str] | Unset = UNSET,
    prefix: str | Unset = UNSET,
    attributes: str | Unset = UNSET,
    time: str | Unset = UNSET,
    compression: int | Unset = UNSET,
) -> UsererrorError | None:
    """Download repo in archived format

    Args:
        repo_identifier (str):
        git_ref (str):
        format_ (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        path (list[str] | Unset):
        prefix (str | Unset):
        attributes (str | Unset):
        time (str | Unset):
        compression (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsererrorError
    """

    return sync_detailed(
        repo_identifier=repo_identifier,
        git_ref=git_ref,
        format_=format_,
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        path=path,
        prefix=prefix,
        attributes=attributes,
        time=time,
        compression=compression,
    ).parsed


async def asyncio_detailed(
    repo_identifier: str,
    git_ref: str,
    format_: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    path: list[str] | Unset = UNSET,
    prefix: str | Unset = UNSET,
    attributes: str | Unset = UNSET,
    time: str | Unset = UNSET,
    compression: int | Unset = UNSET,
) -> Response[UsererrorError]:
    """Download repo in archived format

    Args:
        repo_identifier (str):
        git_ref (str):
        format_ (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        path (list[str] | Unset):
        prefix (str | Unset):
        attributes (str | Unset):
        time (str | Unset):
        compression (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsererrorError]
    """

    kwargs = _get_kwargs(
        repo_identifier=repo_identifier,
        git_ref=git_ref,
        format_=format_,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        path=path,
        prefix=prefix,
        attributes=attributes,
        time=time,
        compression=compression,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    repo_identifier: str,
    git_ref: str,
    format_: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    path: list[str] | Unset = UNSET,
    prefix: str | Unset = UNSET,
    attributes: str | Unset = UNSET,
    time: str | Unset = UNSET,
    compression: int | Unset = UNSET,
) -> UsererrorError | None:
    """Download repo in archived format

    Args:
        repo_identifier (str):
        git_ref (str):
        format_ (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        path (list[str] | Unset):
        prefix (str | Unset):
        attributes (str | Unset):
        time (str | Unset):
        compression (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsererrorError
    """

    return (
        await asyncio_detailed(
            repo_identifier=repo_identifier,
            git_ref=git_ref,
            format_=format_,
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            path=path,
            prefix=prefix,
            attributes=attributes,
            time=time,
            compression=compression,
        )
    ).parsed
