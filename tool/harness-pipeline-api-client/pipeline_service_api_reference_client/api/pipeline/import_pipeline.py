from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.pipeline_import_request import PipelineImportRequest
from ...models.response_dto_pipeline_save_response import ResponseDTOPipelineSaveResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PipelineImportRequest | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    connector_ref: str | Unset = UNSET,
    repo_name: str,
    branch: str,
    file_path: str,
    is_force_import: bool | Unset = False,
    is_harness_code_repo: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["connectorRef"] = connector_ref

    params["repoName"] = repo_name

    params["branch"] = branch

    params["filePath"] = file_path

    params["isForceImport"] = is_force_import

    params["isHarnessCodeRepo"] = is_harness_code_repo

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/pipelines/import",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOPipelineSaveResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOPipelineSaveResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOPipelineSaveResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PipelineImportRequest | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    connector_ref: str | Unset = UNSET,
    repo_name: str,
    branch: str,
    file_path: str,
    is_force_import: bool | Unset = False,
    is_harness_code_repo: bool | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPipelineSaveResponse]:
    """Import and Create Pipeline from Git Repository

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        connector_ref (str | Unset):
        repo_name (str):
        branch (str):
        file_path (str):
        is_force_import (bool | Unset):  Default: False.
        is_harness_code_repo (bool | Unset):
        body (PipelineImportRequest | Unset): Contains basic information required to be linked
            with imported Pipeline YAML

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPipelineSaveResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        connector_ref=connector_ref,
        repo_name=repo_name,
        branch=branch,
        file_path=file_path,
        is_force_import=is_force_import,
        is_harness_code_repo=is_harness_code_repo,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: PipelineImportRequest | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    connector_ref: str | Unset = UNSET,
    repo_name: str,
    branch: str,
    file_path: str,
    is_force_import: bool | Unset = False,
    is_harness_code_repo: bool | Unset = UNSET,
) -> Error | Failure | ResponseDTOPipelineSaveResponse | None:
    """Import and Create Pipeline from Git Repository

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        connector_ref (str | Unset):
        repo_name (str):
        branch (str):
        file_path (str):
        is_force_import (bool | Unset):  Default: False.
        is_harness_code_repo (bool | Unset):
        body (PipelineImportRequest | Unset): Contains basic information required to be linked
            with imported Pipeline YAML

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPipelineSaveResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        connector_ref=connector_ref,
        repo_name=repo_name,
        branch=branch,
        file_path=file_path,
        is_force_import=is_force_import,
        is_harness_code_repo=is_harness_code_repo,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PipelineImportRequest | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    connector_ref: str | Unset = UNSET,
    repo_name: str,
    branch: str,
    file_path: str,
    is_force_import: bool | Unset = False,
    is_harness_code_repo: bool | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOPipelineSaveResponse]:
    """Import and Create Pipeline from Git Repository

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        connector_ref (str | Unset):
        repo_name (str):
        branch (str):
        file_path (str):
        is_force_import (bool | Unset):  Default: False.
        is_harness_code_repo (bool | Unset):
        body (PipelineImportRequest | Unset): Contains basic information required to be linked
            with imported Pipeline YAML

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPipelineSaveResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        connector_ref=connector_ref,
        repo_name=repo_name,
        branch=branch,
        file_path=file_path,
        is_force_import=is_force_import,
        is_harness_code_repo=is_harness_code_repo,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PipelineImportRequest | Unset = UNSET,
    account_identifier: str,
    org_identifier: str,
    project_identifier: str,
    connector_ref: str | Unset = UNSET,
    repo_name: str,
    branch: str,
    file_path: str,
    is_force_import: bool | Unset = False,
    is_harness_code_repo: bool | Unset = UNSET,
) -> Error | Failure | ResponseDTOPipelineSaveResponse | None:
    """Import and Create Pipeline from Git Repository

    Args:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        connector_ref (str | Unset):
        repo_name (str):
        branch (str):
        file_path (str):
        is_force_import (bool | Unset):  Default: False.
        is_harness_code_repo (bool | Unset):
        body (PipelineImportRequest | Unset): Contains basic information required to be linked
            with imported Pipeline YAML

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPipelineSaveResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            connector_ref=connector_ref,
            repo_name=repo_name,
            branch=branch,
            file_path=file_path,
            is_force_import=is_force_import,
            is_harness_code_repo=is_harness_code_repo,
        )
    ).parsed
