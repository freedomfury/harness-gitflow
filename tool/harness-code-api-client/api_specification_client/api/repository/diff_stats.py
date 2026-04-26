from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.types_diff_stats import TypesDiffStats
from ...models.usererror_error import UsererrorError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    repo_identifier: str,
    range_: str,
    *,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    path: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    json_path: list[str] | Unset = UNSET
    if not isinstance(path, Unset):
        json_path = path

    params["path"] = json_path

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repos/{repo_identifier}/diff-stats/{range_}".format(
            repo_identifier=quote(str(repo_identifier), safe=""),
            range_=quote(str(range_), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TypesDiffStats | UsererrorError | None:
    if response.status_code == 200:
        response_200 = TypesDiffStats.from_dict(response.json())

        return response_200

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
) -> Response[TypesDiffStats | UsererrorError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    repo_identifier: str,
    range_: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    path: list[str] | Unset = UNSET,
) -> Response[TypesDiffStats | UsererrorError]:
    """Get diff stats

    Args:
        repo_identifier (str):
        range_ (str):  Example: main..dev.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        path (list[str] | Unset): provide path for diff operation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TypesDiffStats | UsererrorError]
    """

    kwargs = _get_kwargs(
        repo_identifier=repo_identifier,
        range_=range_,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        path=path,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    repo_identifier: str,
    range_: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    path: list[str] | Unset = UNSET,
) -> TypesDiffStats | UsererrorError | None:
    """Get diff stats

    Args:
        repo_identifier (str):
        range_ (str):  Example: main..dev.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        path (list[str] | Unset): provide path for diff operation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TypesDiffStats | UsererrorError
    """

    return sync_detailed(
        repo_identifier=repo_identifier,
        range_=range_,
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        path=path,
    ).parsed


async def asyncio_detailed(
    repo_identifier: str,
    range_: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    path: list[str] | Unset = UNSET,
) -> Response[TypesDiffStats | UsererrorError]:
    """Get diff stats

    Args:
        repo_identifier (str):
        range_ (str):  Example: main..dev.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        path (list[str] | Unset): provide path for diff operation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TypesDiffStats | UsererrorError]
    """

    kwargs = _get_kwargs(
        repo_identifier=repo_identifier,
        range_=range_,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        path=path,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    repo_identifier: str,
    range_: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    path: list[str] | Unset = UNSET,
) -> TypesDiffStats | UsererrorError | None:
    """Get diff stats

    Args:
        repo_identifier (str):
        range_ (str):  Example: main..dev.
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        path (list[str] | Unset): provide path for diff operation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TypesDiffStats | UsererrorError
    """

    return (
        await asyncio_detailed(
            repo_identifier=repo_identifier,
            range_=range_,
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            path=path,
        )
    ).parsed
