from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dtopms_git_update_response import ResponseDTOPMSGitUpdateResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pipeline_identifier: str,
    *,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
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
        "url": "/pipelines/{pipeline_identifier}/update-git-metadata".format(
            pipeline_identifier=quote(str(pipeline_identifier), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOPMSGitUpdateResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOPMSGitUpdateResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOPMSGitUpdateResponse]:
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
    connector_ref: str | Unset = UNSET,
    repo_name: str | Unset = UNSET,
    file_path: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPMSGitUpdateResponse]:
    """Update git-metadata in remote pipeline Entity

     Update git-metadata in remote pipeline and returns the identifier of updated pipeline

    Args:
        pipeline_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        connector_ref (str | Unset):
        repo_name (str | Unset):
        file_path (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPMSGitUpdateResponse]
    """

    kwargs = _get_kwargs(
        pipeline_identifier=pipeline_identifier,
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
    pipeline_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    connector_ref: str | Unset = UNSET,
    repo_name: str | Unset = UNSET,
    file_path: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOPMSGitUpdateResponse | None:
    """Update git-metadata in remote pipeline Entity

     Update git-metadata in remote pipeline and returns the identifier of updated pipeline

    Args:
        pipeline_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        connector_ref (str | Unset):
        repo_name (str | Unset):
        file_path (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPMSGitUpdateResponse
    """

    return sync_detailed(
        pipeline_identifier=pipeline_identifier,
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        connector_ref=connector_ref,
        repo_name=repo_name,
        file_path=file_path,
    ).parsed


async def asyncio_detailed(
    pipeline_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    connector_ref: str | Unset = UNSET,
    repo_name: str | Unset = UNSET,
    file_path: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPMSGitUpdateResponse]:
    """Update git-metadata in remote pipeline Entity

     Update git-metadata in remote pipeline and returns the identifier of updated pipeline

    Args:
        pipeline_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        connector_ref (str | Unset):
        repo_name (str | Unset):
        file_path (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPMSGitUpdateResponse]
    """

    kwargs = _get_kwargs(
        pipeline_identifier=pipeline_identifier,
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
    pipeline_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    connector_ref: str | Unset = UNSET,
    repo_name: str | Unset = UNSET,
    file_path: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOPMSGitUpdateResponse | None:
    """Update git-metadata in remote pipeline Entity

     Update git-metadata in remote pipeline and returns the identifier of updated pipeline

    Args:
        pipeline_identifier (str):
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        connector_ref (str | Unset):
        repo_name (str | Unset):
        file_path (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPMSGitUpdateResponse
    """

    return (
        await asyncio_detailed(
            pipeline_identifier=pipeline_identifier,
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            connector_ref=connector_ref,
            repo_name=repo_name,
            file_path=file_path,
        )
    ).parsed
