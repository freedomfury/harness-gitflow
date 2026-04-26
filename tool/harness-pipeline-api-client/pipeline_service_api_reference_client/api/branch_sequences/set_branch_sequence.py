from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import UNSET, Response


def _get_kwargs(
    pipeline_identifier: str,
    *,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    repo_url: str,
    branch: str,
    sequence_id: int,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["repoUrl"] = repo_url

    params["branch"] = branch

    params["sequenceId"] = sequence_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/pipelines/{pipeline_identifier}/branch-sequences/set".format(
            pipeline_identifier=quote(str(pipeline_identifier), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pipeline_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    repo_url: str,
    branch: str,
    sequence_id: int,
) -> Response[Any | Error]:
    """Set Branch Sequence

     Sets the branch sequence counter to a specific value for the given branch and repository. The
    repository URL will be normalized internally. If no record exists, a new one is created.

    Args:
        pipeline_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        repo_url (str):
        branch (str):
        sequence_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        pipeline_identifier=pipeline_identifier,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        repo_url=repo_url,
        branch=branch,
        sequence_id=sequence_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pipeline_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    repo_url: str,
    branch: str,
    sequence_id: int,
) -> Any | Error | None:
    """Set Branch Sequence

     Sets the branch sequence counter to a specific value for the given branch and repository. The
    repository URL will be normalized internally. If no record exists, a new one is created.

    Args:
        pipeline_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        repo_url (str):
        branch (str):
        sequence_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return sync_detailed(
        pipeline_identifier=pipeline_identifier,
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        repo_url=repo_url,
        branch=branch,
        sequence_id=sequence_id,
    ).parsed


async def asyncio_detailed(
    pipeline_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    repo_url: str,
    branch: str,
    sequence_id: int,
) -> Response[Any | Error]:
    """Set Branch Sequence

     Sets the branch sequence counter to a specific value for the given branch and repository. The
    repository URL will be normalized internally. If no record exists, a new one is created.

    Args:
        pipeline_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        repo_url (str):
        branch (str):
        sequence_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        pipeline_identifier=pipeline_identifier,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        repo_url=repo_url,
        branch=branch,
        sequence_id=sequence_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pipeline_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    repo_url: str,
    branch: str,
    sequence_id: int,
) -> Any | Error | None:
    """Set Branch Sequence

     Sets the branch sequence counter to a specific value for the given branch and repository. The
    repository URL will be normalized internally. If no record exists, a new one is created.

    Args:
        pipeline_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        repo_url (str):
        branch (str):
        sequence_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return (
        await asyncio_detailed(
            pipeline_identifier=pipeline_identifier,
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            repo_url=repo_url,
            branch=branch,
            sequence_id=sequence_id,
        )
    ).parsed
