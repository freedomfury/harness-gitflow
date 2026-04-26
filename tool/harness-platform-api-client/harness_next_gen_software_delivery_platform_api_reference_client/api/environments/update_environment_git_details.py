from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_environment_git_update_response import ResponseDTOEnvironmentGitUpdateResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    environment_identifier: str,
    *,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    connector_ref: str | Unset = UNSET,
    repo_name: str | Unset = UNSET,
    file_path: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["connectorRef"] = connector_ref

    params["repoName"] = repo_name

    params["filePath"] = file_path

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/environmentsV2/{environment_identifier}/update-git-metadata".format(
            environment_identifier=quote(str(environment_identifier), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOEnvironmentGitUpdateResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOEnvironmentGitUpdateResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOEnvironmentGitUpdateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    environment_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    connector_ref: str | Unset = UNSET,
    repo_name: str | Unset = UNSET,
    file_path: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOEnvironmentGitUpdateResponse]:
    """Update git-metadata in remote environment Entity

     Update git-metadata in remote environment and returns the identifier of updated environment

    Args:
        environment_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        connector_ref (str | Unset):
        repo_name (str | Unset):
        file_path (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOEnvironmentGitUpdateResponse]
    """

    kwargs = _get_kwargs(
        environment_identifier=environment_identifier,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        connector_ref=connector_ref,
        repo_name=repo_name,
        file_path=file_path,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    connector_ref: str | Unset = UNSET,
    repo_name: str | Unset = UNSET,
    file_path: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOEnvironmentGitUpdateResponse | None:
    """Update git-metadata in remote environment Entity

     Update git-metadata in remote environment and returns the identifier of updated environment

    Args:
        environment_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        connector_ref (str | Unset):
        repo_name (str | Unset):
        file_path (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOEnvironmentGitUpdateResponse
    """

    return sync_detailed(
        environment_identifier=environment_identifier,
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        connector_ref=connector_ref,
        repo_name=repo_name,
        file_path=file_path,
    ).parsed


async def asyncio_detailed(
    environment_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    connector_ref: str | Unset = UNSET,
    repo_name: str | Unset = UNSET,
    file_path: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOEnvironmentGitUpdateResponse]:
    """Update git-metadata in remote environment Entity

     Update git-metadata in remote environment and returns the identifier of updated environment

    Args:
        environment_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        connector_ref (str | Unset):
        repo_name (str | Unset):
        file_path (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOEnvironmentGitUpdateResponse]
    """

    kwargs = _get_kwargs(
        environment_identifier=environment_identifier,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        connector_ref=connector_ref,
        repo_name=repo_name,
        file_path=file_path,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    connector_ref: str | Unset = UNSET,
    repo_name: str | Unset = UNSET,
    file_path: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOEnvironmentGitUpdateResponse | None:
    """Update git-metadata in remote environment Entity

     Update git-metadata in remote environment and returns the identifier of updated environment

    Args:
        environment_identifier (str):
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        connector_ref (str | Unset):
        repo_name (str | Unset):
        file_path (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOEnvironmentGitUpdateResponse
    """

    return (
        await asyncio_detailed(
            environment_identifier=environment_identifier,
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            connector_ref=connector_ref,
            repo_name=repo_name,
            file_path=file_path,
        )
    ).parsed
