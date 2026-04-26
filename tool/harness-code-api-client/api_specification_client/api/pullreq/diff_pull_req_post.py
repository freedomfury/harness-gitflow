from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_file_diff_request import ApiFileDiffRequest
from ...models.git_file_diff import GitFileDiff
from ...models.usererror_error import UsererrorError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    repo_identifier: str,
    pullreq_number: int,
    *,
    body: list[ApiFileDiffRequest] | None | Unset = UNSET,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/repos/{repo_identifier}/pullreq/{pullreq_number}/diff".format(
            repo_identifier=quote(str(repo_identifier), safe=""),
            pullreq_number=quote(str(pullreq_number), safe=""),
        ),
        "params": params,
    }

    if isinstance(body, list):
        _kwargs["json"] = []
        for componentsschemas_openapi_post_raw_pr_diff_request_type_0_item_data in body:
            componentsschemas_openapi_post_raw_pr_diff_request_type_0_item = (
                componentsschemas_openapi_post_raw_pr_diff_request_type_0_item_data.to_dict()
            )
            _kwargs["json"].append(componentsschemas_openapi_post_raw_pr_diff_request_type_0_item)

    else:
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UsererrorError | list[GitFileDiff] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GitFileDiff.from_dict(response_200_item_data)

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
) -> Response[UsererrorError | list[GitFileDiff]]:
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
    body: list[ApiFileDiffRequest] | None | Unset = UNSET,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> Response[UsererrorError | list[GitFileDiff]]:
    """Get file changes

    Args:
        repo_identifier (str):
        pullreq_number (int):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        body (list[ApiFileDiffRequest] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsererrorError | list[GitFileDiff]]
    """

    kwargs = _get_kwargs(
        repo_identifier=repo_identifier,
        pullreq_number=pullreq_number,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
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
    body: list[ApiFileDiffRequest] | None | Unset = UNSET,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> UsererrorError | list[GitFileDiff] | None:
    """Get file changes

    Args:
        repo_identifier (str):
        pullreq_number (int):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        body (list[ApiFileDiffRequest] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsererrorError | list[GitFileDiff]
    """

    return sync_detailed(
        repo_identifier=repo_identifier,
        pullreq_number=pullreq_number,
        client=client,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
    ).parsed


async def asyncio_detailed(
    repo_identifier: str,
    pullreq_number: int,
    *,
    client: AuthenticatedClient | Client,
    body: list[ApiFileDiffRequest] | None | Unset = UNSET,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> Response[UsererrorError | list[GitFileDiff]]:
    """Get file changes

    Args:
        repo_identifier (str):
        pullreq_number (int):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        body (list[ApiFileDiffRequest] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsererrorError | list[GitFileDiff]]
    """

    kwargs = _get_kwargs(
        repo_identifier=repo_identifier,
        pullreq_number=pullreq_number,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    repo_identifier: str,
    pullreq_number: int,
    *,
    client: AuthenticatedClient | Client,
    body: list[ApiFileDiffRequest] | None | Unset = UNSET,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
) -> UsererrorError | list[GitFileDiff] | None:
    """Get file changes

    Args:
        repo_identifier (str):
        pullreq_number (int):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        body (list[ApiFileDiffRequest] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsererrorError | list[GitFileDiff]
    """

    return (
        await asyncio_detailed(
            repo_identifier=repo_identifier,
            pullreq_number=pullreq_number,
            client=client,
            body=body,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
        )
    ).parsed
